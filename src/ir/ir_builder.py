from __future__ import annotations

from itertools import chain
from typing import assert_never

import sympy as sp

import utils
from ir.ir_nodes import (
    IRBoundIdentifier,
    IRConst,
    IRFunction,
    IRIfElse,
    IRInstruction,
    IRLoop,
    IRModule,
    IROperand,
    IRReturn,
    IRStatement,
    IRStore,
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
    Buffer,
    DSLType,
    Index,
    IRType,
    PrimeField,
)


def compile_dsl_type(type_: DSLType, vectorize: bool) -> IRType:
    match type_, vectorize:
        case Index(), False:
            return "scalar"
        case PrimeField(), False:
            return "vector"
        case PrimeField(), True:
            return "matrix"
        case Buffer(), False:
            return "pod"
        case _:
            assert_never((type_, vectorize))  # type: ignore


def compile_operator(operator: str) -> str:
    try:
        return utils.OP_TO_IR_TABLE[operator]
    except KeyError as ke:
        raise NotImplementedError(operator) from ke


def vectorized_insn_name(base_name: str, vectorize: bool) -> str:
    return f"v{base_name}" if vectorize else base_name


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
            statements.append(
                # Propagates further, handles cases
                # where 2^pi - theta <= x < 2^pi once at the end
                IRInstruction(False, ret_val, "full_reduction", (ret_val,))
            )
        if self.function.is_hash:
            statements.append(IRStore(ret_val))
        else:
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
            self.function.is_hash,
        )

    def compile_expr(  # noqa: C901
        self,
        ast_expression: ASTExpr,
        lanes: int = 1,
        step: int = 1,
        offsets: dict[str, int] | None = None,
    ) -> tuple[list[IRStatement], IROperand]:
        match ast_expression:
            case ASTInt(Index(), value):
                return [], IRConst(Index(), compile_dsl_type(Index(), lanes > 1), value)  # type: ignore
            case ASTInt(type_, value) if type_:
                ir_type = compile_dsl_type(type_, lanes > 1)
                temporary = IRTemporary(type_, ir_type)
                return [
                    IRInstruction(
                        True,
                        temporary,
                        "const",
                        (IRConst(type_, ir_type, value),),  # type: ignore
                    )
                ], temporary
            case ASTLocalIdentifier(type_, name) if type_:
                base_id = IRBoundIdentifier(type_, compile_dsl_type(type_, False), name)
                # If an unroll offset exists for this variable, inject an addition
                if offsets and name in offsets and offsets[name] != 0:
                    ir_type = compile_dsl_type(type_, False)
                    temp = IRTemporary(type_, ir_type)
                    add_stmt = IRInstruction(
                        True,
                        temp,
                        compile_operator("+"),
                        (base_id, IRConst(type_, ir_type, offsets[name])),
                    )
                    return [add_stmt], temp
                return [], base_id
            case ASTBinaryOperation(type_, operator, left, right):
                if operator == "**":
                    match right:
                        case ASTInt(Index(), 0):
                            return self.compile_expr(
                                ASTInt(left.ttype, 1), lanes, step, offsets
                            )
                        case ASTInt(Index(), 1):
                            return self.compile_expr(left, lanes, step, offsets)
                        case ASTInt(Index(), 2):
                            if not isinstance(left.ttype, PrimeField):
                                return self.compile_expr(
                                    ASTBinaryOperation(left.ttype, "*", left, left),
                                    lanes,
                                    step,
                                    offsets,
                                )
                            base_stmts, base_term = self.compile_expr(
                                left, lanes, step, offsets
                            )
                            assert left.ttype
                            square = IRInstruction(
                                True,
                                IRTemporary(
                                    left.ttype,
                                    compile_dsl_type(left.ttype, lanes > 1),
                                ),
                                vectorized_insn_name("square", lanes > 1),
                                (base_term,),
                            )
                            return base_stmts + [square], square.result
                        case ASTInt(Index(), _):
                            raise NotImplementedError("Exponents greater than 2")
                        case _:
                            raise NotImplementedError(ast_expression)
                return self.compile_bin_expr(ast_expression, lanes, step, offsets)
            case ASTComparison(type_, operator, left, right) if type_:
                left_stmt, left_ter = self.compile_expr(left, offsets=offsets)
                right_stmt, right_ter = self.compile_expr(right, offsets=offsets)
                comp = IRInstruction(
                    True,
                    IRTemporary(type_, compile_dsl_type(type_, False)),
                    utils.OP_TO_IR_TABLE[operator],
                    (left_ter, right_ter),
                )
                return left_stmt + right_stmt + [comp], comp.result
            case ASTIfElse():
                return self.compile_if_else(ast_expression, offsets)
            case ASTCall(type_, func_name, args) if type_:
                prepare_args = [self.compile_expr(e, offsets=offsets) for e in args]
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
                index_stmts, index_ter = self.compile_expr(index, offsets=offsets)
                ir_offsets = [
                    IRConst(Index(), compile_dsl_type(Index(), False), i * (step or 1))
                    for i in range(lanes)
                ]
                load = IRInstruction(
                    True,
                    IRTemporary(ttype, compile_dsl_type(ttype, lanes > 1)),
                    vectorized_insn_name(
                        "load", lanes > 1 and isinstance(ttype, PrimeField)
                    ),
                    (
                        IRBoundIdentifier(
                            buffer.ttype,
                            "matrix" if lanes > 1 else "vector",
                            buffer.name,
                        ),
                        index_ter,
                        *ir_offsets,
                    ),
                )
                return index_stmts + [load], load.result
            case ASTReduction(ttype, _):
                assert lanes == 1, "no nested reductions please"
                return self.compile_reduction(ast_expression, offsets)
            case _:
                raise NotImplementedError(f"{ast_expression!r}")

    def compile_bin_expr(
        self,
        bin_expr: ASTBinaryOperation,
        lanes: int = 1,
        step: int = 1,
        offsets: dict[str, int] | None = None,
    ) -> tuple[list[IRStatement], IROperand]:
        # Recurse into children
        lstmts, lterm = self.compile_expr(bin_expr.left, lanes, step, offsets)
        rstmts, rterm = self.compile_expr(bin_expr.right, lanes, step, offsets)
        # Build insn/term
        assert bin_expr.ttype
        binop = IRInstruction(
            True,
            IRTemporary(bin_expr.ttype, compile_dsl_type(bin_expr.ttype, lanes > 1)),
            vectorized_insn_name(
                compile_operator(bin_expr.operator),
                lanes > 1 and isinstance(bin_expr.ttype, PrimeField),
            ),
            (lterm, rterm),
        )
        return lstmts + rstmts + [binop], binop.result

    def compile_if_else(
        self, if_else: ASTIfElse, offsets: dict[str, int] | None = None
    ) -> tuple[list[IRStatement], IROperand]:
        assert if_else.ttype
        dsl_type, ir_type = if_else.ttype, compile_dsl_type(if_else.ttype, False)
        cond_stmts, cond_ter = self.compile_expr(if_else.condition, offsets=offsets)
        then_stmts, then_ter = self.compile_expr(if_else.then_branch, offsets=offsets)

        if if_else.constant_time:
            assert if_else.else_branch is not None, "constant-time if requires else"
            else_stmts, else_ter = self.compile_expr(
                if_else.else_branch, offsets=offsets
            )
            ifelse = IRIfElse(
                cond_ter,
                then_stmts,
                else_stmts,
                True,
            )
            select = IRInstruction(
                True,
                IRTemporary(dsl_type, ir_type),
                "select",
                (cond_ter, then_ter, else_ter),
            )
            return cond_stmts + [ifelse, select], select.result

        declare = IRInstruction(
            True,
            IRTemporary(dsl_type, ir_type),
            "const",
            (IRConst(dsl_type, ir_type, 0),),
        )
        else_branch = None
        if if_else.else_branch is not None:
            else_stmts, else_ter = self.compile_expr(
                if_else.else_branch, offsets=offsets
            )
            else_branch = else_stmts + [
                IRInstruction(False, declare.result, "copy", (else_ter,))
            ]
        ifelse = IRIfElse(
            cond_ter,
            then_stmts + [IRInstruction(False, declare.result, "copy", (then_ter,))],
            else_branch,
            False,
        )
        return [declare] + cond_stmts + [ifelse], declare.result

    def compile_reduction(
        self, reduction: ASTReduction, offsets: dict[str, int] | None = None
    ) -> tuple[list[IRStatement], IROperand]:
        sta_stmts, sta_term = self.compile_expr(reduction.start, offsets=offsets)
        sto_stmts, sto_term = self.compile_expr(reduction.stop, offsets=offsets)

        if not isinstance(reduction.step, ASTInt):
            raise ValueError(f"Non-constant loop step {reduction.step}")

        base_step = reduction.step.value
        lanes = self.module_builder.settings.lanes or 1
        unroll_factor = self.module_builder.settings.unrolling_factor or 1

        # Calculate full step size across lanes and unroll slots
        vector_step = base_step * lanes
        unrolled_step = vector_step * unroll_factor

        # Dynamic tail boundary
        # Calculate the exact point where the main loop must stop
        # main_loop_end = stop - ((stop - start) % unrolled_step)
        tail_len_expr = ASTBinaryOperation(
            Index(),
            "%",
            ASTBinaryOperation(Index(), "-", reduction.stop, reduction.start),
            ASTInt(Index(), unrolled_step),
        )
        main_loop_end_expr = ASTBinaryOperation(
            Index(),
            "-",
            reduction.stop,
            tail_len_expr,
        )
        main_end_stmts, main_end_term = self.compile_expr(
            main_loop_end_expr, offsets=offsets
        )

        # Update bound for codegen
        new_bound: sp.Expr = sp.simplify(reduction.bound / (lanes * unroll_factor))  # type: ignore

        match reduction.op:
            case "+":
                neutral_element = 0
            case "*":
                neutral_element = 1
            case _:
                raise ValueError(reduction.op)
        assert reduction.ttype

        # Initialize the vector accumulator for the main unrolled loop
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

        # Build unrolled main loop body
        unrolled_body_stmts: list[IRStatement] = []
        for u in range(unroll_factor):
            offset_val = u * vector_step

            # Create a fresh environment for this unroll iteration
            loop_offsets = offsets.copy() if offsets else {}
            loop_offsets[reduction.var] = offset_val

            bod_stmts, bod_term = self.compile_expr(
                reduction.body,
                lanes=self.module_builder.settings.lanes
                if self.module_builder.settings.lanes
                else 1,
                step=base_step,
                offsets=loop_offsets,
            )
            unrolled_body_stmts.extend(bod_stmts)

            update_acc = IRInstruction(
                False,
                declare_acc.result,
                vectorized_insn_name(
                    compile_operator(reduction.op),
                    declare_acc.result.ir_type == "matrix",
                ),
                (declare_acc.result, bod_term),
            )
            unrolled_body_stmts.append(update_acc)

        # Handle carries every 'unroll_facror' times
        unrolled_body_stmts.append(
            IRInstruction(
                False,
                declare_acc.result,
                vectorized_insn_name("carry", declare_acc.result.ir_type == "matrix"),
                (declare_acc.result,),
            )
        )

        # Create the main unrolled vector loop
        main_loop = IRLoop(
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), reduction.var),
            sta_term,
            main_end_term,
            IRConst(Index(), compile_dsl_type(Index(), False), unrolled_step),
            unrolled_body_stmts,
            new_bound,  # type: ignore
        )

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

        # Scalar tail cleanup Loop
        # Remove the unrolling offset for the tail
        tail_offsets = offsets.copy() if offsets else {}
        tail_offsets.pop(reduction.var, None)

        tail_bod_stmts, tail_bod_term = self.compile_expr(
            reduction.body, lanes=1, step=base_step, offsets=tail_offsets
        )
        update_tail_acc = IRInstruction(
            False,
            final_value,
            compile_operator(reduction.op),
            (final_value, tail_bod_term),
        )

        try:
            tail_bound = reduction.bound % unrolled_step  # type: ignore
        except Exception:
            tail_bound = sp.var("tail_bound")  # type: ignore # TODO

        tail_loop = IRLoop(
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), reduction.var),
            main_end_term,
            sto_term,
            IRConst(Index(), compile_dsl_type(Index(), False), base_step),
            tail_bod_stmts + [update_tail_acc],
            tail_bound,  # type: ignore
        )

        # Group everything into a list of IR blocks
        all_statements = (
            sta_stmts
            + sto_stmts
            + main_end_stmts
            + [declare_acc, main_loop]
            + horizontal_reduction
            + [tail_loop]
        )

        return all_statements, final_value


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
