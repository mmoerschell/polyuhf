from __future__ import annotations

from dataclasses import dataclass, field, replace
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
    ASTHornerReduction,
    ASTIfElse,
    ASTInt,
    ASTLeftFold,
    ASTLocalIdentifier,
    ASTModule,
    ASTSum,
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


@dataclass(frozen=True)
class CompileContext:
    bindings: dict[str, IROperand] = field(default_factory=dict)
    offsets: dict[str, int] = field(default_factory=dict)

    def bind(self, name: str, operand: IROperand) -> CompileContext:
        bindings = dict(self.bindings)
        bindings[name] = operand
        return replace(self, bindings=bindings)

    def with_offset(self, name: str, value: int) -> CompileContext:
        offsets = dict(self.offsets)
        offsets[name] = value
        return replace(self, offsets=offsets)

    def without_offset(self, name: str) -> CompileContext:
        offsets = dict(self.offsets)
        offsets.pop(name, None)
        return replace(self, offsets=offsets)


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

    def _carry_if_partial(self, value: IRTemporary) -> list[IRStatement]:
        if self.module_builder.settings.limb_realignment == "full":
            return []
        return [
            IRInstruction(
                False,
                value,
                vectorized_insn_name("carry", value.ir_type == "matrix"),
                (value,),
            )
        ]

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
        ctx: CompileContext | None = None,
    ) -> tuple[list[IRStatement], IROperand]:
        ctx = ctx or CompileContext()
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
                base_id = ctx.bindings.get(
                    name,
                    IRBoundIdentifier(type_, compile_dsl_type(type_, False), name),
                )
                # If an unroll offset exists for this variable, inject an addition
                if name in ctx.offsets and ctx.offsets[name] != 0:
                    ir_type = compile_dsl_type(type_, False)
                    temp = IRTemporary(type_, ir_type)
                    add_stmt = IRInstruction(
                        True,
                        temp,
                        compile_operator("+"),
                        (base_id, IRConst(type_, ir_type, ctx.offsets[name])),
                    )
                    return [add_stmt], temp
                return [], base_id
            case ASTBinaryOperation(type_, operator, left, right):
                if operator == "**":
                    match right:
                        case ASTInt(Index(), 0):
                            return self.compile_expr(
                                ASTInt(left.ttype, 1), lanes, step, ctx
                            )
                        case ASTInt(Index(), 1):
                            return self.compile_expr(left, lanes, step, ctx)
                        case ASTInt(Index(), 2):
                            if not isinstance(left.ttype, PrimeField):
                                return self.compile_expr(
                                    ASTBinaryOperation(left.ttype, "*", left, left),
                                    lanes,
                                    step,
                                    ctx,
                                )
                            base_stmts, base_term = self.compile_expr(
                                left, lanes, step, ctx
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
                return self.compile_bin_expr(ast_expression, lanes, step, ctx)
            case ASTComparison(type_, operator, left, right) if type_:
                left_stmt, left_ter = self.compile_expr(left, ctx=ctx)
                right_stmt, right_ter = self.compile_expr(right, ctx=ctx)
                comp = IRInstruction(
                    True,
                    IRTemporary(type_, compile_dsl_type(type_, False)),
                    utils.OP_TO_IR_TABLE[operator],
                    (left_ter, right_ter),
                )
                return left_stmt + right_stmt + [comp], comp.result
            case ASTIfElse():
                return self.compile_if_else(ast_expression, ctx)
            case ASTCall(type_, func_name, args) if type_:
                prepare_args = [self.compile_expr(e, ctx=ctx) for e in args]
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
                index_stmts, index_ter = self.compile_expr(index, ctx=ctx)
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
            case ASTSum(ttype, _):
                assert lanes == 1, "no nested reductions please"
                return self.compile_sum(ast_expression, ctx)
            case ASTHornerReduction(ttype, _):
                assert lanes == 1, "no nested reductions please"
                return self.compile_horner_reduction(ast_expression, ctx)
            case ASTLeftFold(ttype, _):
                assert lanes == 1, "no nested reductions please"
                return self.compile_left_fold(ast_expression, ctx)
            case _:
                raise NotImplementedError(f"{ast_expression!r}")

    def compile_bin_expr(
        self,
        bin_expr: ASTBinaryOperation,
        lanes: int = 1,
        step: int = 1,
        ctx: CompileContext | None = None,
    ) -> tuple[list[IRStatement], IROperand]:
        ctx = ctx or CompileContext()
        # Recurse into children
        lstmts, lterm = self.compile_expr(bin_expr.left, lanes, step, ctx)
        rstmts, rterm = self.compile_expr(bin_expr.right, lanes, step, ctx)
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
        self, if_else: ASTIfElse, ctx: CompileContext | None = None
    ) -> tuple[list[IRStatement], IROperand]:
        ctx = ctx or CompileContext()
        assert if_else.ttype
        dsl_type, ir_type = if_else.ttype, compile_dsl_type(if_else.ttype, False)
        cond_stmts, cond_ter = self.compile_expr(if_else.condition, ctx=ctx)
        then_stmts, then_ter = self.compile_expr(if_else.then_branch, ctx=ctx)

        if if_else.constant_time:
            assert if_else.else_branch is not None, "constant-time if requires else"
            else_stmts, else_ter = self.compile_expr(if_else.else_branch, ctx=ctx)
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
            else_stmts, else_ter = self.compile_expr(if_else.else_branch, ctx=ctx)
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

    def field_power(
        self,
        base: IROperand,
        exponent: int,
    ) -> tuple[list[IRStatement], IROperand]:
        if exponent < 0:
            raise ValueError(f"negative field exponent {exponent}")
        assert isinstance(base.dsl_type, PrimeField)
        if exponent == 0:
            return [], IRConst(base.dsl_type, base.ir_type, 1)
        if exponent == 1:
            return [], base

        statements: list[IRStatement] = []
        current = base
        for _ in range(2, exponent + 1):
            product = IRInstruction(
                True,
                IRTemporary(base.dsl_type, base.ir_type),
                vectorized_insn_name("mul", base.ir_type == "matrix"),
                (current, base),
            )
            statements.append(product)
            statements.extend(self._carry_if_partial(product.result))
            current = product.result
        return statements, current

    def compile_horner_step(
        self,
        acc: IRTemporary,
        r: IROperand,
        body_term: IROperand,
        carry_result: bool = False,
    ) -> list[IRStatement]:
        assert acc.dsl_type
        sum_ = IRInstruction(
            True,
            IRTemporary(acc.dsl_type, acc.ir_type),
            vectorized_insn_name("add", acc.ir_type == "matrix"),
            (acc, body_term),
        )
        product = IRInstruction(
            True,
            IRTemporary(acc.dsl_type, acc.ir_type),
            vectorized_insn_name("mul", acc.ir_type == "matrix"),
            (sum_.result, r),
        )
        statements = [
            sum_,
            product,
        ]
        if carry_result:
            statements.extend(self._carry_if_partial(product.result))
        statements.append(IRInstruction(False, acc, "copy", (product.result,)))
        return statements

    def compile_horner_reduction(
        self, reduction: ASTHornerReduction, ctx: CompileContext | None = None
    ) -> tuple[list[IRStatement], IROperand]:
        ctx = ctx or CompileContext()
        sta_stmts, sta_term = self.compile_expr(reduction.start, ctx=ctx)
        sto_stmts, sto_term = self.compile_expr(reduction.stop, ctx=ctx)
        r_stmts, r_term = self.compile_expr(reduction.r, ctx=ctx)

        if not isinstance(reduction.step, ASTInt):
            raise ValueError(f"Non-constant loop step {reduction.step}")

        base_step = reduction.step.value
        lanes = self.module_builder.settings.lanes or 1
        unroll_factor = self.module_builder.settings.unrolling_factor or 1

        vector_step = base_step * lanes
        unrolled_step = vector_step * unroll_factor

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
        main_end_stmts, main_end_term = self.compile_expr(main_loop_end_expr, ctx=ctx)

        assert reduction.ttype
        vectorize = bool(self.module_builder.settings.lanes)
        acc_ir_type = compile_dsl_type(reduction.ttype, vectorize)
        declare_acc = IRInstruction(
            True,
            IRTemporary(reduction.ttype, acc_ir_type),
            "const",
            (IRConst(reduction.ttype, acc_ir_type, 0),),
        )

        precompute_stmts: list[IRStatement] = []
        r_for_main = r_term
        lane_powers: IROperand | None = None
        if vectorize:
            scalar_power_stmts: list[IRStatement] = []
            scalar_powers: dict[int, IROperand] = {1: r_term}
            for exponent in range(2, lanes + 1):
                product = IRInstruction(
                    True,
                    IRTemporary(
                        reduction.ttype, compile_dsl_type(reduction.ttype, False)
                    ),
                    "mul",
                    (scalar_powers[exponent - 1], r_term),
                )
                scalar_power_stmts.append(product)
                scalar_power_stmts.extend(self._carry_if_partial(product.result))
                scalar_powers[exponent] = product.result

            splat_r = IRInstruction(
                True,
                IRTemporary(reduction.ttype, compile_dsl_type(reduction.ttype, True)),
                "splat",
                (scalar_powers[lanes],),
            )
            lane_powers_insn = IRInstruction(
                True,
                IRTemporary(reduction.ttype, compile_dsl_type(reduction.ttype, True)),
                "lane_powers",
                tuple(scalar_powers[lanes - lane] for lane in range(lanes)),
            )
            precompute_stmts.extend(scalar_power_stmts)
            precompute_stmts.extend([splat_r, lane_powers_insn])
            r_for_main = splat_r.result
            lane_powers = lane_powers_insn.result

        new_bound: sp.Expr = sp.simplify(  # type: ignore
            reduction.bound / (lanes * unroll_factor)
        )

        unrolled_body_stmts: list[IRStatement] = []
        for u in range(unroll_factor):
            offset_val = u * vector_step
            loop_ctx = ctx.bind(
                reduction.var,
                IRBoundIdentifier(
                    Index(), compile_dsl_type(Index(), False), reduction.var
                ),
            ).with_offset(reduction.var, offset_val)

            bod_stmts, bod_term = self.compile_expr(
                reduction.body,
                lanes=lanes,
                step=base_step,
                ctx=loop_ctx,
            )
            unrolled_body_stmts.extend(bod_stmts)

            if vectorize:
                assert lane_powers is not None
                weighted_body = IRInstruction(
                    True,
                    IRTemporary(
                        reduction.ttype, compile_dsl_type(reduction.ttype, True)
                    ),
                    "vmul",
                    (bod_term, lane_powers),
                )
                scaled_acc = IRInstruction(
                    True,
                    IRTemporary(
                        reduction.ttype, compile_dsl_type(reduction.ttype, True)
                    ),
                    "vmul",
                    (declare_acc.result, r_for_main),
                )
                update_acc = IRInstruction(
                    True,
                    IRTemporary(
                        reduction.ttype, compile_dsl_type(reduction.ttype, True)
                    ),
                    "vadd",
                    (scaled_acc.result, weighted_body.result),
                )
                unrolled_body_stmts.extend(
                    [
                        weighted_body,
                        scaled_acc,
                        update_acc,
                        IRInstruction(
                            False, declare_acc.result, "copy", (update_acc.result,)
                        ),
                    ]
                )
            else:
                unrolled_body_stmts.extend(
                    self.compile_horner_step(declare_acc.result, r_for_main, bod_term)
                )

        unrolled_body_stmts.extend(self._carry_if_partial(declare_acc.result))

        main_loop = IRLoop(
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), reduction.var),
            sta_term,
            main_end_term,
            IRConst(Index(), compile_dsl_type(Index(), False), unrolled_step),
            unrolled_body_stmts,
            new_bound,  # type: ignore
        )

        if not vectorize:
            horizontal_reduction = []
            final_value = declare_acc.result
        else:
            horizontal_reduction = [
                IRInstruction(
                    True,
                    IRTemporary(
                        reduction.ttype, compile_dsl_type(reduction.ttype, False)
                    ),
                    "horiz_add",
                    (declare_acc.result,),
                )
            ]
            final_value = horizontal_reduction[0].result

        tail_ctx = ctx.bind(
            reduction.var,
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), reduction.var),
        ).without_offset(reduction.var)

        tail_bod_stmts, tail_bod_term = self.compile_expr(
            reduction.body, lanes=1, step=base_step, ctx=tail_ctx
        )
        tail_update = self.compile_horner_step(
            final_value, r_term, tail_bod_term, carry_result=True
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
            tail_bod_stmts + tail_update,
            tail_bound,  # type: ignore
        )

        all_statements = (
            sta_stmts
            + sto_stmts
            + r_stmts
            + precompute_stmts
            + main_end_stmts
            + [declare_acc, main_loop]
            + horizontal_reduction
            + [tail_loop]
        )

        return all_statements, final_value

    def compile_left_fold(
        self, fold: ASTLeftFold, ctx: CompileContext | None = None
    ) -> tuple[list[IRStatement], IROperand]:
        ctx = ctx or CompileContext()
        sta_stmts, sta_term = self.compile_expr(fold.start, ctx=ctx)
        sto_stmts, sto_term = self.compile_expr(fold.stop, ctx=ctx)
        init_stmts, init_term = self.compile_expr(fold.init, ctx=ctx)

        if not isinstance(fold.step, ASTInt):
            raise ValueError(f"Non-constant loop step {fold.step}")

        assert fold.ttype
        acc_ir_type = compile_dsl_type(fold.ttype, False)
        declare_acc = IRInstruction(
            True,
            IRTemporary(fold.ttype, acc_ir_type),
            "const",
            (IRConst(fold.ttype, acc_ir_type, 0),),
        )
        initialize_acc: list[IRStatement] = [
            IRInstruction(False, declare_acc.result, "copy", (init_term,))
        ]
        if isinstance(fold.ttype, PrimeField):
            initialize_acc.extend(self._carry_if_partial(declare_acc.result))

        body_ctx = ctx.without_offset(fold.var).without_offset(fold.acc_var).bind(
            fold.var,
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), fold.var),
        ).bind(fold.acc_var, declare_acc.result)
        body_stmts, body_term = self.compile_expr(fold.body, lanes=1, ctx=body_ctx)
        update_acc: list[IRStatement] = [
            IRInstruction(False, declare_acc.result, "copy", (body_term,))
        ]
        if isinstance(fold.ttype, PrimeField):
            update_acc.extend(self._carry_if_partial(declare_acc.result))

        base_step = fold.step.value
        loop = IRLoop(
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), fold.var),
            sta_term,
            sto_term,
            IRConst(Index(), compile_dsl_type(Index(), False), base_step),
            body_stmts + update_acc,
            fold.bound,
        )

        return (
            sta_stmts
            + sto_stmts
            + init_stmts
            + [declare_acc]
            + initialize_acc
            + [loop],
            declare_acc.result,
        )

    def compile_sum(
        self, sum_: ASTSum, ctx: CompileContext | None = None
    ) -> tuple[list[IRStatement], IROperand]:
        ctx = ctx or CompileContext()
        sta_stmts, sta_term = self.compile_expr(sum_.start, ctx=ctx)
        sto_stmts, sto_term = self.compile_expr(sum_.stop, ctx=ctx)

        if not isinstance(sum_.step, ASTInt):
            raise ValueError(f"Non-constant loop step {sum_.step}")

        base_step = sum_.step.value
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
            ASTBinaryOperation(Index(), "-", sum_.stop, sum_.start),
            ASTInt(Index(), unrolled_step),
        )
        main_loop_end_expr = ASTBinaryOperation(
            Index(),
            "-",
            sum_.stop,
            tail_len_expr,
        )
        main_end_stmts, main_end_term = self.compile_expr(main_loop_end_expr, ctx=ctx)

        # Update bound for codegen
        new_bound: sp.Expr = sp.simplify(  # type: ignore
            sum_.bound / (lanes * unroll_factor)
        )
        assert sum_.ttype

        # Initialize the vector accumulator for the main unrolled loop
        declare_acc = IRInstruction(
            True,
            IRTemporary(
                sum_.ttype,
                compile_dsl_type(
                    sum_.ttype, bool(self.module_builder.settings.lanes)
                ),
            ),
            "const",
            (
                IRConst(
                    sum_.ttype,
                    compile_dsl_type(
                        sum_.ttype, bool(self.module_builder.settings.lanes)
                    ),
                    0,
                ),
            ),
        )

        # Build unrolled main loop body
        unrolled_body_stmts: list[IRStatement] = []
        for u in range(unroll_factor):
            offset_val = u * vector_step

            # Create a fresh environment for this unroll iteration
            loop_ctx = ctx.bind(
                sum_.var,
                IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), sum_.var),
            ).with_offset(sum_.var, offset_val)

            bod_stmts, bod_term = self.compile_expr(
                sum_.body,
                lanes=self.module_builder.settings.lanes
                if self.module_builder.settings.lanes
                else 1,
                step=base_step,
                ctx=loop_ctx,
            )
            unrolled_body_stmts.extend(bod_stmts)

            update_acc = IRInstruction(
                False,
                declare_acc.result,
                vectorized_insn_name("add", declare_acc.result.ir_type == "matrix"),
                (declare_acc.result, bod_term),
            )
            unrolled_body_stmts.append(update_acc)

        # Handle carries every 'unroll_facror' times
        unrolled_body_stmts.extend(self._carry_if_partial(declare_acc.result))

        # Create the main unrolled vector loop
        main_loop = IRLoop(
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), sum_.var),
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
                        sum_.ttype, compile_dsl_type(sum_.ttype, False)
                    ),
                    "horiz_add",
                    (declare_acc.result,),
                )
            ]
            final_value = horizontal_reduction[0].result

        # Scalar tail cleanup Loop
        # Remove the unrolling offset for the tail
        tail_ctx = ctx.bind(
            sum_.var,
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), sum_.var),
        ).without_offset(sum_.var)

        tail_bod_stmts, tail_bod_term = self.compile_expr(
            sum_.body, lanes=1, step=base_step, ctx=tail_ctx
        )
        update_tail_acc = IRInstruction(
            False,
            final_value,
            "add",
            (final_value, tail_bod_term),
        )

        try:
            tail_bound = sum_.bound % unrolled_step  # type: ignore
        except Exception:
            tail_bound = sp.var("tail_bound")  # type: ignore # TODO

        tail_loop = IRLoop(
            IRBoundIdentifier(Index(), compile_dsl_type(Index(), False), sum_.var),
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
