from itertools import chain
from typing import assert_never

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


def pprint_module(module: IRModule) -> str:
    return "\n\n".join(pprint_function(func) for func in module.funcs)


def pprint_function(func: IRFunction) -> str:
    ctx: dict[int, str] = {}
    header = (
        f"func {func.name} ("
        + ", ".join(
            f"{p.name}: {p.ir_type}" for p in func.params
        )
        + ") {\n"
    )
    body = "\n".join(
        chain.from_iterable(pprint_statement(x, ctx, 1) for x in func.body)
    )
    return header + body + "\n}\n"


def pprint_statement(
    stmt: IRStatement,
    print_ctx: dict[int, str],
    indentation_level: int = 0,
) -> list[str]:
    indentation = f"{' ' * indentation_level * 4}"
    match stmt:
        case IRAssigningInstruction(result, name, ops):
            return [
                f"{indentation}"
                f"{pprint_operand(result, print_ctx)}"
                f": {result.ir_type} = {name} "
                f"{', '.join(pprint_operand(o, print_ctx) for o in ops)}"
            ]
        case IRLoop(var, begin, end, increment, body):
            header = (
                f"{indentation}"
                f"loop var {pprint_operand(var, print_ctx)} from "
                f"{pprint_operand(begin, print_ctx)} to "
                f"{pprint_operand(end, print_ctx)} step "
                f"{pprint_operand(increment, print_ctx)} {'{'}"
            )
            body_text = list(
                chain.from_iterable(
                    pprint_statement(x, print_ctx, indentation_level + 1) for x in body
                )
            )
            return [header] + body_text + [indentation + "}"]
        case IRReturn(value):
            return [f"{indentation}ret {pprint_operand(value, print_ctx)}"]


def pprint_operand(operand: IROperand, print_ctx: dict[int, str]) -> str:
    match operand:
        case IRTemporary():
            return print_ctx.setdefault(id(operand), f"%{len(print_ctx)}")
        case IRBoundIdentifier(_, _, name):
            return f"%{name}"
        case IRConst(_, _, value):
            return str(value)
        case _:
            assert_never(operand)  # type: ignore
