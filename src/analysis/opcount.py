# pyright: basic
import sympy as sp

from ir.ir_nodes import (
    IRIfElse,
    IRInstruction,
    IRLoop,
    IRModule,
    IRReturn,
    IRStatement,
    IRStore,
    IRTemporary,
)
from settings import Settings
from typesystem import Index, PrimeField


def field_mul_ops(settings: Settings) -> float:
    if settings.mul_algo == "karatsuba":
        low = (settings.limbs + 1) // 2
        high = settings.limbs // 2
        return 1.5 * (2 * low**2 + high**2)
    return 1.5 * settings.limbs**2


def field_square_ops(settings: Settings) -> float:
    return 1.5 * settings.limbs * (settings.limbs + 1) / 2


def per_instruction(  # noqa: C901
    insn: IRInstruction, settings: Settings
) -> tuple[float, float]:
    # TODO review these
    # TODO distinguish architectures
    match insn:
        # Generic
        case IRInstruction(_, _, "const"):
            return 0, 0
        case IRInstruction(_, _, "copy"):
            return 0, 0
        case IRInstruction(_, _, "call"):
            raise ValueError("Can't determin op-count for recursive functions")
        case IRInstruction(_, IRTemporary(Index(), "scalar"), "select"):
            return 4, 0
        case IRInstruction(_, IRTemporary(_, "vector"), "select"):
            return 4 * settings.limbs, 0
        # Scalar
        case IRInstruction(_, IRTemporary(Index(), "scalar"), _):
            # TODO do these count?
            return 1, 0
        # Vector
        case IRInstruction(_, IRTemporary(_, "vector"), "load"):
            return 6 * settings.limbs, settings.field.chunk_size()
        case IRInstruction(_, IRTemporary(_, "vector"), "add"):
            return settings.limbs, 0
        case IRInstruction(_, IRTemporary(_, "vector"), "mul"):
            return field_mul_ops(settings), 0
        case IRInstruction(_, IRTemporary(_, "vector"), "square"):
            return field_square_ops(settings), 0
        case IRInstruction(_, IRTemporary(_, "vector"), "carry"):
            return (settings.limbs + 2) * 3 + 1, 0
        case IRInstruction(_, IRTemporary(_, "vector"), "full_reduction"):
            # TODO ooo
            return (settings.limbs + 2) * 3 + 1, 0
        case IRInstruction(_, IRTemporary(_, "vector"), "horiz_add") if settings.lanes:
            return (settings.lanes - 1) * settings.limbs, 0
        # Matrix
        case IRInstruction(_, IRTemporary(_, "matrix"), "vload") if settings.lanes:
            return 2.75 * settings.limbs, 16 * settings.lanes
        case IRInstruction(_, IRTemporary(_, "matrix"), "splat") if settings.lanes:
            return settings.limbs, 0
        case IRInstruction(
            _, IRTemporary(_, "matrix"), "lane_powers"
        ) if settings.lanes:
            return settings.lanes * settings.limbs, 0
        case IRInstruction(_, IRTemporary(_, "matrix"), "vadd") if settings.lanes:
            return settings.lanes * settings.limbs, 0
        case IRInstruction(_, IRTemporary(_, "matrix"), "vmul") if settings.lanes:
            return settings.lanes * field_mul_ops(settings), 0
        case IRInstruction(_, IRTemporary(_, "matrix"), "vsquare") if settings.lanes:
            return settings.lanes * field_square_ops(settings), 0
        case IRInstruction(
            _, IRTemporary(PrimeField(_, theta), "matrix"), "vcarry"
        ) if settings.lanes:
            return (settings.limbs + 2) * 3 + 2 * theta.bit_count(), 0
        case _:
            pass
    raise NotImplementedError(insn)


def per_statement(
    stmt: IRStatement, settings: Settings, B: sp.Symbol
) -> tuple[sp.Expr, sp.Expr]:
    match stmt:
        case IRInstruction():
            ops, traffic = per_instruction(stmt, settings)
            return sp.Integer(ops), sp.Integer(traffic)
        case IRLoop():
            ops, traffic = per_statement_list(stmt.body, settings, B)
            return stmt.bound * ops, stmt.bound * traffic
        case IRIfElse(_, then_branch, else_branch, constant_time):
            then_ops, then_traffic = per_statement_list(then_branch, settings, B)
            if else_branch is None:
                return then_ops / 2, then_traffic / 2
            else_ops, else_traffic = per_statement_list(else_branch, settings, B)
            if constant_time:
                return then_ops + else_ops, then_traffic + else_traffic
            # Heuristic for non-constant-time branches.
            return (then_ops + else_ops) / 2, (then_traffic + else_traffic) / 2
        case IRReturn():
            return 0, 0
        case IRStore():
            return 0, (settings.field.pi + 7) // 8


def per_statement_list(
    stmt_list: list[IRStatement], settings: Settings, B: sp.Symbol
) -> tuple[sp.Expr, sp.Expr]:
    ops, traffic = sp.Integer(0), sp.Integer(0)
    for stmt in stmt_list:
        o, t = per_statement(stmt, settings, B)
        ops += o
        traffic += t
    return ops, traffic


def opcount_and_traffic(
    module: IRModule, settings: Settings
) -> tuple[sp.Expr, sp.Expr, sp.Symbol] | None:
    """
    number of integer operations, and amount of memory traffic in bytes
    if and only iff the module has one function,
    """
    candidate_functions = list(
        filter(
            lambda f: (
                f.is_hash
                and len(f.params) == 3
                and f.params[0].ir_type == "pod"  # key
                and f.params[1].ir_type == "pod"  # message
                and f.params[2].ir_type == "scalar"  # n. of blocks
            ),
            module.funcs,
        )
    )
    if len(candidate_functions) == 1:
        B = sp.symbols("B")
        try:
            ops, traffic = per_statement_list(candidate_functions[0].body, settings, B)
        except ValueError as _:
            return None
        return sp.simplify(ops), sp.simplify(traffic), B
