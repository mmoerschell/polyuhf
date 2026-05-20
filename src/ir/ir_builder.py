from __future__ import annotations

from itertools import chain

import utils
from ir.ir_nodes import (
    IRAssigningInstruction,
    IRBoundIdentifier,
    IRConst,
    IRFunction,
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
from typechecker import DSLFunctionSignature
from typesystem import (
    BufferView,
    DSLType,
    Index,
    IRType,
    IRTypeMatrix,
    IRTypeScalar,
    IRTypeVector,
    PrimeField,
)


# FIXME set these constants somewhere else!
def compile_dsl_type(dsl_type: DSLType, lanes: int = 1) -> IRType:
    match dsl_type:
        case Index() if lanes == 1:
            return IRTypeScalar(64)
        case PrimeField(pi, _) if lanes == 1:
            # TODO pick smart limb sizes
            lam = 10
            limbs = (pi + lam - 1) // lam
            lam_prime = pi % lam
            return IRTypeVector(
                32, limbs, lam, lam_prime, (1 << lam) - 1, (1 << lam_prime) - 1
            )
        case PrimeField(pi, _):
            lam = 10
            limbs = (pi + lam - 1) // lam
            lam_prime = pi % lam
            # TODO ensure 32 * lanes = max available machine width
            return IRTypeMatrix(
                32, lanes, limbs, lam, lam_prime, (1 << lam) - 1, (1 << lam_prime) - 1
            )
        case BufferView():
            return "pod"
        case _:
            raise NotImplementedError(f"{dsl_type!r}")


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
        if isinstance(ret_val, IRTemporary) and isinstance(
            ret_val.ir_type, IRTypeVector
        ):
            statements.append(IRAssigningInstruction(ret_val, "carry", (ret_val,)))
        statements.append(IRReturn(ret_val))
        return IRFunction(
            self.function.name,
            [
                IRBoundIdentifier(t, compile_dsl_type(t), n)
                for n, t in self.function.params
            ],
            statements,
            ret_val,
            self.function.return_type,
        )

    def compile_expr(
        self, ast_expression: ASTExpr, lanes: int = 1
    ) -> tuple[list[IRStatement], IROperand]:
        match ast_expression:
            case ASTInt(ttype, value) if ttype:
                return [], IRConst(ttype, compile_dsl_type(ttype), value)
            case ASTLocalIdentifier(ttype, name) if ttype:
                return [], IRBoundIdentifier(ttype, compile_dsl_type(ttype), name)
            case ASTBinaryOperation(ttype, _):
                return self.compile_bin_expr(ast_expression, lanes)
            case ASTComparison(type_, operator, left, right) if type_:
                left_stmt, left_ter = self.compile_expr(left)
                right_stmt, right_ter = self.compile_expr(right)
                comp = IRAssigningInstruction(
                    IRTemporary(type_, compile_dsl_type(type_)),
                    utils.OP_TO_IR_TABLE[operator],
                    (left_ter, right_ter),
                )
                return left_stmt + right_stmt + [comp], comp.result
            case ASTIfElse(type_, cond, then, else_) if type_:
                cond_stmt, cond_ter = self.compile_expr(cond)
                then_stmt, then_ter = self.compile_expr(then)
                else_stmt, else_ter = self.compile_expr(else_)
                ifel_stmt = IRAssigningInstruction(
                    IRTemporary(type_, compile_dsl_type(type_)),
                    "ifelse",
                    (cond_ter, then_ter, else_ter),
                )
                return cond_stmt + then_stmt + else_stmt + [ifel_stmt], ifel_stmt.result
            case ASTCall(type_, func_name, args) if type_:
                prepare_args = [self.compile_expr(e) for e in args]
                call_stmt = IRAssigningInstruction(
                    IRTemporary(type_, compile_dsl_type(type_)),
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
                # TODO figure out an instruction set
                load = IRAssigningInstruction(
                    IRTemporary(ttype, compile_dsl_type(ttype, lanes)),
                    "load",
                    (
                        IRBoundIdentifier(
                            buffer.ttype,
                            compile_dsl_type(buffer.ttype),
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
        binop = IRAssigningInstruction(
            IRTemporary(bin_expr.ttype, compile_dsl_type(bin_expr.ttype, lanes)),
            compile_operator(bin_expr.operator),
            (lterm, rterm),
        )
        return lstmts + rstmts + [binop], binop.result

    def compile_reduction(
        self, reduction: ASTReduction
    ) -> tuple[list[IRStatement], IROperand]:
        # TODO WARNING verify that expression is indeed
        # vectorizable: affine indices and no if-else
        # Recurse into children
        sta_stmts, sta_term = self.compile_expr(reduction.start)
        sto_stmts, sto_term = self.compile_expr(reduction.stop)
        if self.module_builder.available_lanes == 1:
            ste_stmts, ste_term = self.compile_expr(reduction.step)
        else:
            # FIXME incorporate additional unrolling as well
            ste_stmts, ste_term = self.compile_expr(
                ASTBinaryOperation(
                    Index(),
                    "*",
                    (reduction.step),
                    ASTInt(Index(), self.module_builder.available_lanes),
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
        declare_acc = IRAssigningInstruction(
            IRTemporary(
                reduction.ttype,
                compile_dsl_type(reduction.ttype, self.module_builder.available_lanes),
            ),
            "const",
            (
                IRConst(
                    reduction.ttype,
                    compile_dsl_type(
                        reduction.ttype, self.module_builder.available_lanes
                    ),
                    neutral_element,
                ),
            ),
        )
        # Body
        bod_stmts, bod_term = self.compile_expr(
            reduction.body, self.module_builder.available_lanes
        )
        # Accumulator update
        update_acc = IRAssigningInstruction(
            declare_acc.result,
            compile_operator(reduction.op),
            (declare_acc.result, bod_term),
        )
        # TODO FIXME
        # Unprocessed data (if unrolling factor * lanes !| # of iterations)
        # Horizontal reduction
        if self.module_builder.available_lanes == 1:
            horizontal_reduction = []
            final_value = declare_acc.result
        else:
            horizontal_reduction = [
                IRAssigningInstruction(
                    IRTemporary(reduction.ttype, compile_dsl_type(reduction.ttype)),
                    f"horiz_{compile_operator(reduction.op)}",
                    (declare_acc.result,),
                )
            ]
            final_value = horizontal_reduction[0].result
        return sta_stmts + sto_stmts + ste_stmts + [declare_acc] + [
            IRLoop(
                IRBoundIdentifier(Index(), compile_dsl_type(Index()), reduction.var),
                sta_term,
                sto_term,
                ste_term,
                bod_stmts
                + [
                    update_acc,
                    IRAssigningInstruction(
                        declare_acc.result, "carry", (declare_acc.result,)
                    ),
                ],
            ),
        ] + horizontal_reduction, final_value


class IRModuleBuilder:
    def __init__(
        self,
        ast_module: ASTModule,
        name: str,
        signatures: list[DSLFunctionSignature],
        available_lanes: int,
    ) -> None:
        # Probably want to build some global symbols table here
        self.ast_module: ASTModule = ast_module
        self.name = name
        self.signatures = signatures
        self.available_lanes = available_lanes

    def compile(self) -> IRModule:
        compiled_functions: list[IRFunction] = []
        for f, signature in zip(
            self.ast_module.functions, self.signatures, strict=True
        ):
            function_builder = IRFunctionBuilder(self, f, signature)
            compiled_functions.append(function_builder.compile())
        return IRModule(self.name, compiled_functions)
