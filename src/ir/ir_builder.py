from __future__ import annotations

from itertools import chain
from typing import assert_never

import utils
from ir.ir_nodes import (
    IRBoundIdentifier,
    IRConst,
    IRFunction,
    IRInstruction,
    IRLoop,
    IRModule,
    IROperand,
    IRReturn,
    IRStatement,
    IRTemporary,
)
from parsing.ast.ast_nodes import (
    ASTBinaryOperation,
    ASTBufferViewRead,
    ASTCall,
    ASTComparison,
    ASTExpr,
    ASTFunction,
    ASTIfElse,
    ASTInt,
    ASTLocalIdentifier,
    ASTModule,
    ASTReduction,
)
from settings import Settings
from typechecker import DSLFunctionSignature
from typesystem import (
    BufferView,
    DSLType,
    Field,
    Index,
    IRType,
)


def compile_dsl_type(type_: DSLType, vectorize: bool) -> IRType:
    match type_, vectorize:
        case Index(), False:
            return "scalar"
        case Field(), False:
            return "vector"
        case Field(), True:
            return "matrix"
        case BufferView(), False:
            return "pod"
        case _:
            assert_never((type_, vectorize))  # type: ignore


def compile_operator(operator: str) -> str:
    try:
        return utils.OP_TO_IR_TABLE[operator]
    except KeyError as ke:
        raise NotImplementedError(operator) from ke


class IRFunctionBuilder:
    def __init__(
        self,
        module_builder: IRModuleBuilder,
        ast_function: ASTFunction,
        dsl_signature: DSLFunctionSignature,
    ) -> None:
        self.module_builder = module_builder
        self.function = ast_function
        self.signature = dsl_signature

    def compile(self) -> IRFunction:
        statements, ret_val = self.compile_expr(self.function.body)
        if isinstance(ret_val, IRTemporary) and ret_val.ir_type == "vector":
            statements.append(IRInstruction(False, ret_val, "carry", (ret_val,)))
        statements.append(IRReturn(ret_val))
        return IRFunction(
            self.function.name,
            [
                IRBoundIdentifier(t, compile_dsl_type(t, False), n)
                for n, t in self.function.params
            ],
            statements,
            ret_val,
            self.function.return_type,
            compile_dsl_type(self.function.return_type, False),
        )

    def compile_expr(
        self, ast_expression: ASTExpr, lanes: int = 1
    ) -> tuple[list[IRStatement], IROperand]:
        match ast_expression:
            case ASTInt(type_, value):
                return [], IRConst(type_, compile_dsl_type(type_, lanes > 1), value)  # type: ignore
            case ASTLocalIdentifier(type_, name) if type_:
                return [], IRBoundIdentifier(
                    type_, compile_dsl_type(type_, False), name
                )  # type: ignore
            case ASTBinaryOperation(type_, _):
                return self.compile_bin_expr(ast_expression, lanes)
            case ASTComparison(type_, operator, left, right) if type_:
                left_stmt, left_ter = self.compile_expr(left)
                right_stmt, right_ter = self.compile_expr(right)
                comp = IRInstruction(
                    True,
                    IRTemporary(type_, compile_dsl_type(type_, False)),
                    utils.OP_TO_IR_TABLE[operator],
                    (left_ter, right_ter),
                )
                return left_stmt + right_stmt + [comp], comp.result
            case ASTIfElse(type_, cond, then, else_) if type_:
                cond_stmt, cond_ter = self.compile_expr(cond)
                then_stmt, then_ter = self.compile_expr(then)
                else_stmt, else_ter = self.compile_expr(else_)
                ifel_stmt = IRInstruction(
                    True,
                    IRTemporary(type_, compile_dsl_type(type_, False)),
                    "ifelse",
                    (cond_ter, then_ter, else_ter),
                )
                return cond_stmt + then_stmt + else_stmt + [ifel_stmt], ifel_stmt.result
            case ASTCall(type_, func_name, args) if type_:
                prepare_args = [self.compile_expr(e) for e in args]
                call_stmt = IRInstruction(
                    True,
                    IRTemporary(type_, compile_dsl_type(type_, False)),
                    "call",
                    tuple(
                        [IRBoundIdentifier(None, None, func_name)]  # type: ignore
                        + [operand for _, operand in prepare_args]
                    ),
                )
                return list(
                    chain.from_iterable(
                        [stmts for stmts, _ in prepare_args] + [[call_stmt]]
                    )
                ), call_stmt.result
            case ASTBufferViewRead(ttype, buffer, index) if ttype and buffer.ttype:
                index_stmts, index_ter = self.compile_expr(index)
                load = IRInstruction(
                    True,
                    IRTemporary(ttype, compile_dsl_type(ttype, lanes > 1)),
                    "load",
                    (
                        IRBoundIdentifier(
                            buffer.ttype,
                            "matrix" if lanes > 1 else "vector",
                            buffer.name,
                        ),
                        index_ter,
                    ),
                )
                return index_stmts + [load], load.result
            case ASTReduction(ttype, _):
                assert lanes == 1, "no nested reductions please"
                return self.compile_reduction(ast_expression)
            case _:
                raise NotImplementedError(f"{ast_expression!r}")

    def compile_bin_expr(
        self, bin_expr: ASTBinaryOperation, lanes: int = 1
    ) -> tuple[list[IRStatement], IROperand]:
        # Recurse into children
        lstmts, lterm = self.compile_expr(bin_expr.left, lanes)
        rstmts, rterm = self.compile_expr(bin_expr.right, lanes)
        # Build insn/term
        assert bin_expr.ttype
        binop = IRInstruction(
            True,
            IRTemporary(bin_expr.ttype, compile_dsl_type(bin_expr.ttype, lanes > 1)),
            compile_operator(bin_expr.operator),
            (lterm, rterm),
        )
        return lstmts + rstmts + [binop], binop.result

    def compile_reduction(
        self, reduction: ASTReduction
    ) -> tuple[list[IRStatement], IROperand]:
        sta_stmts, sta_term = self.compile_expr(reduction.start)
        sto_stmts, sto_term = self.compile_expr(reduction.stop)
        if not self.module_builder.settings.lanes:
            ste_stmts, ste_term = self.compile_expr(reduction.step)
        else:
            ste_stmts, ste_term = self.compile_expr(
                ASTBinaryOperation(
                    Index(),
                    "*",
                    (reduction.step),
                    ASTInt(Index(), self.module_builder.settings.lanes),
                )
            )
        # Build insn/term
        match reduction.op:
            case "+":
                neutral_element = 0
            case "*":
                neutral_element = 1
            case _:
                raise ValueError(reduction.op)
        assert reduction.ttype
        # Accumulator
        declare_acc = IRInstruction(
            True,
            IRTemporary(
                reduction.ttype,
                compile_dsl_type(
                    reduction.ttype, bool(self.module_builder.settings.lanes)
                ),
            ),
            "const",
            (
                IRConst(
                    reduction.ttype,
                    compile_dsl_type(
                        reduction.ttype, bool(self.module_builder.settings.lanes)
                    ),
                    neutral_element,
                ),
            ),
        )
        # Body
        bod_stmts, bod_term = self.compile_expr(
            reduction.body,
            self.module_builder.settings.lanes
            if self.module_builder.settings.lanes
            else 1,
        )
        # Accumulator update
        update_acc = IRInstruction(
            False,
            declare_acc.result,
            compile_operator(reduction.op),
            (declare_acc.result, bod_term),
        )
        # TODO FIXME
        # Unprocessed data (if unrolling factor * lanes !| # of iterations)
        # Horizontal reduction
        if not self.module_builder.settings.lanes:
            horizontal_reduction = []
            final_value = declare_acc.result
        else:
            horizontal_reduction = [
                IRInstruction(
                    True,
                    IRTemporary(
                        reduction.ttype, compile_dsl_type(reduction.ttype, False)
                    ),
                    f"horiz_{compile_operator(reduction.op)}",
                    (declare_acc.result,),
                )
            ]
            final_value = horizontal_reduction[0].result
        return sta_stmts + sto_stmts + ste_stmts + [declare_acc] + [
            IRLoop(
                IRBoundIdentifier(
                    Index(), compile_dsl_type(Index(), False), reduction.var
                ),
                sta_term,
                sto_term,
                ste_term,
                bod_stmts
                + [
                    update_acc,
                    IRInstruction(
                        False, declare_acc.result, "carry", (declare_acc.result,)
                    ),
                ],
            ),
        ] + horizontal_reduction, final_value


class IRModuleBuilder:
    def __init__(
        self,
        ast_module: ASTModule,
        name: str,
        signatures: dict[str, DSLFunctionSignature],
        settings: Settings,
    ) -> None:
        self.ast_module: ASTModule = ast_module
        self.name = name
        self.signatures = signatures
        self.settings = settings

    def compile(self) -> IRModule:
        compiled_functions: list[IRFunction] = []
        for f in self.ast_module.functions:
            function_builder = IRFunctionBuilder(self, f, self.signatures[f.name])
            compiled_functions.append(function_builder.compile())
        return IRModule(self.name, compiled_functions)
