from ir.c.c_nodes import (
    CAssign,
    CBinOp,
    CConst,
    CDeclaration,
    CExpression,
    CProgram,
    CReturn,
    CStatement,
    CVariable,
    CWhile,
)
from ir.types import Type


# One level higher ATM
def generate_type(t: Type) -> str:
    match t:
        case Type.INDEX:
            return "int64_t"
        case Type.BIGINT:
            return "bigint_t"


def generate_expr(expr: CExpression) -> str:
    match expr:
        case CVariable(name):
            return name
        case CConst(value):
            return str(value)
        case CBinOp(op, lhs, rhs):
            # Parentheses: better safe than sorry
            return f"(({generate_expr(lhs)}){op}({generate_expr(rhs)}))"
        case _:
            raise NotImplementedError(f"missing printing pass for expr {type(expr)}")


def generate_stmt(stmt: CStatement) -> str:
    match stmt:
        case CDeclaration(ty, name, None):
            return f"{generate_type(ty)} {name};"
        case CDeclaration(ty, name, CExpression() as init):
            return f"{generate_type(ty)} {name}={generate_expr(init)};"
        case CAssign(CVariable(name), rhs):
            return f"{name}={generate_expr(rhs)};"
        case CReturn(None):
            return "return;"
        case CReturn(CExpression() as expr):
            return f"return {generate_expr(expr)};"
        case CWhile(cond, stmts):
            body = "".join(map(generate_stmt, stmts))
            return f"while({generate_expr(cond)}){{{body}}}"
        case _:
            raise NotImplementedError(f"missing printing pass for {type(stmt)}")


def generate_program(p: CProgram) -> str:
    # Imports
    output = ["#import <stdint.h>", ""]

    # TODO data-structure declarations

    # Functions
    for f in p.functions:
        # Params
        for _ in f.parameters:
            raise NotImplementedError()
        output.append(f"{generate_type(f.return_type)} {f.name}()" + "{")
        # Statements
        output.extend(map(generate_stmt, f.statements))
        # Closing curly brace
        output.append("}")
    return "\n".join(output)
