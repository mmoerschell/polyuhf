from ir.c.c_nodes import (
    CArrayAccess,
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
from ir.types import ArrayType, BigIntType, IndexType, Type


# One level higher ATM
def generate_type(t: Type) -> str:
    match t:
        case IndexType():
            return "int64_t"
        case BigIntType():
            return "bigint_t"
        case ArrayType(None, elem):
            return f"{generate_type(elem)}*"
        case ArrayType(int(size), elem):
            return f"{generate_type(elem)}[{size}]"
        case _:
            raise ValueError("pattern matching")


def generate_expr(expr: CExpression) -> str:
    match expr:
        case CVariable(name):
            return name
        case CArrayAccess(var, index):
            return f"{generate_expr(var)}[{generate_expr(index)}]"
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
    output = ["#include <stdint.h>", ""]

    # TODO data-structure declarations

    # Functions
    for f in p.functions:
        # Params
        params = ",".join([
            f"{generate_type(ty)} {name}" for ty, name in f.parameters
        ])
        output.append(f"{generate_type(f.return_type)} {f.name}({params})" + "{")
        # Statements
        output.extend(map(generate_stmt, f.statements))
        # Closing curly brace
        output.append("}")
    return "\n".join(output)
