# pyright: basic
import sympy as sp

from ir.ir_nodes import (
    IRIfElse,
    IRInstruction,
    IRLoop,
    IRModule,
    IRReturn,
    IRStatement,
    IRTemporary,
)
from settings import Settings
from typesystem import Index, PrimeField


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
            return 1.5 * settings.limbs**2, 0
        case IRInstruction(_, IRTemporary(_, "vector"), "carry"):
            return (settings.limbs + 2) * 3 + 1, 0
        case IRInstruction(_, IRTemporary(_, "vector"), "horiz_add") if settings.lanes:
            return (settings.lanes - 1) * settings.limbs, 0
        # Matrix
        case IRInstruction(_, IRTemporary(_, "matrix"), "load") if settings.lanes:
            return 2.75 * settings.limbs, 16 * settings.lanes
        case IRInstruction(_, IRTemporary(_, "matrix"), "add") if settings.lanes:
            return settings.lanes * settings.limbs, 0
        case IRInstruction(_, IRTemporary(_, "matrix"), "mul") if settings.lanes:
            return settings.lanes * 1.5 * settings.limbs**2, 0
        case IRInstruction(_, IRTemporary(PrimeField(_, theta), "matrix"), "carry") if (
            settings.lanes
        ):
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
        case IRIfElse():
            # Heuristic
            # TODO change this if if-else did compute both sides, or only then branch
            then_ops, then_traffic = per_statement_list(stmt.then_branch, settings, B)
            else_ops, else_traffic = per_statement_list(stmt.else_branch, settings, B)
            return (then_ops + else_ops) / 2, (then_traffic + else_traffic) / 2
        case IRReturn():
            return 0, 0


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
    if (
        len(module.funcs) == 1
        and len(module.funcs[0].params) == 3
        and module.funcs[0].params[0].ir_type == "pod"  # key
        and module.funcs[0].params[1].ir_type == "pod"  # message
        and module.funcs[0].params[2].ir_type == "scalar"  # n. of blocks
    ):
        B = sp.symbols("B")
        try:
            ops, traffic = per_statement_list(module.funcs[0].body, settings, B)
        except ValueError as _:
            return None
        return sp.simplify(ops), sp.simplify(traffic), B
