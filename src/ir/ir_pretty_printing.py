from itertools import chain
from typing import assert_never

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
    IRTemporary,
)


def pprint_module(module: IRModule) -> str:
    funcs = "\n\n".join(pprint_function(func) for func in module.funcs)
    return f"module {module.name}\n\n{funcs}"


def pprint_function(func: IRFunction) -> str:
    ctx: dict[int, str] = {}
    header = (
        f"func {func.name}("
        + ", ".join(pprint_param(p) for p in func.params)
        + f") -> {func.dsl_return_type}/{func.ir_return_type} {'{'}\n"
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
        case IRInstruction():
            return [indentation + pprint_instruction(stmt, print_ctx)]
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
        case IRIfElse(cond, then_branch, else_branch, constant_time):
            keyword = "if" if constant_time else "nctif"
            header = f"{indentation}{keyword} {pprint_operand(cond, print_ctx)} {'{'}"
            then_text = list(
                chain.from_iterable(
                    pprint_statement(x, print_ctx, indentation_level + 1)
                    for x in then_branch
                )
            )
            if else_branch is None:
                return [header] + then_text + [indentation + "}"]
            else_text = list(
                chain.from_iterable(
                    pprint_statement(x, print_ctx, indentation_level + 1)
                    for x in else_branch
                )
            )
            return (
                [header]
                + then_text
                + [indentation + "} else {"]
                + else_text
                + [indentation + "}"]
            )
        case IRReturn(value):
            return [f"{indentation}ret {pprint_operand(value, print_ctx)}"]
        case _:
            raise NotImplementedError(stmt)


def pprint_instruction(insn: IRInstruction, print_ctx: dict[int, str]) -> str:
    lhs = pprint_assignment_lhs(insn, print_ctx)
    match insn:
        case IRInstruction(_, _, "select", (condition, then_, else_)):
            return (
                f"{lhs} = select {pprint_operand(condition, print_ctx)} ? "
                f"{pprint_operand(then_, print_ctx)} : "
                f"{pprint_operand(else_, print_ctx)}"
            )
        case IRInstruction(_, _, "call", (func, *args)):
            return (
                f"{lhs} = call {pprint_operand(func, print_ctx)}("
                + ", ".join(pprint_operand(arg, print_ctx) for arg in args)
                + ")"
            )
        case IRInstruction(_, _, name, ops):
            operand_text = ", ".join(pprint_operand(o, print_ctx) for o in ops)
            return f"{lhs} = {name} {operand_text}".rstrip()


def pprint_assignment_lhs(insn: IRInstruction, print_ctx: dict[int, str]) -> str:
    result = pprint_operand(insn.result, print_ctx)
    if not insn.declare:
        return result
    return f"{result}: {insn.result.dsl_type}/{insn.result.ir_type}"


def pprint_param(param: IRBoundIdentifier) -> str:
    return f"%{param.name}: {param.dsl_type}/{param.ir_type}"


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
