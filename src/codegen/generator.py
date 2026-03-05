from ir.c.c_nodes import (
    CArrayAccess,
    CAssign,
    CBinOp,
    CConst,
    CDeclaration,
    CExpression,
    CFunctionCall,
    CIdentifier,
    CProgram,
    CReturn,
    CStatement,
    CWhile,
)
from ir.types import ArrayType, BigIntType, IndexType, LoweringError, Type


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
        case CIdentifier(name):
            return name
        case CArrayAccess(array, index):
            return f"{generate_expr(array)}[{generate_expr(index)}]"
        case CConst(ty, value):
            match ty:
                case IndexType():
                    return str(value)
                case BigIntType():
                    raise NotImplementedError("generalize limbs & lambda")
                    # LIMBS = 6
                    # LAMBD = 48
                    # bits = [int(x) for x in bin(value)[2:]][::-1]  # LSB first
                    # limbs = [
                    #     bits[i * LAMBD : (i + 1) * LAMBD][::-1] for i in range(LIMBS)
                    # ]  # MSB first
                    # limbs = ["0b0" + "".join([str(y) for y in x]) for x in limbs]
                    # return f"{{{','.join(limbs)}}}"
                case ArrayType(_):
                    raise LoweringError("array-typed constants?")
        case CBinOp(op, lhs, rhs):
            # Parentheses: better safe than sorry
            return f"(({generate_expr(lhs)}){op}({generate_expr(rhs)}))"
        case CFunctionCall(func, args):
            chained_args = ",".join(map(generate_expr, args))
            return f"{func}({chained_args})"
        case _:
            raise NotImplementedError(f"missing printing pass for expr {type(expr)}")


def generate_stmt(stmt: CStatement) -> str:
    match stmt:
        case CDeclaration(ty, name, None):
            return f"{generate_type(ty)} {name};"
        case CDeclaration(ty, name, CExpression() as init):
            return f"{generate_type(ty)} {name}={generate_expr(init)};"
        case CAssign(CIdentifier(name), rhs):
            return f"{name}={generate_expr(rhs)};"
        case CAssign(CArrayAccess(CIdentifier(name)), rhs):
            return f"{name}={generate_expr(rhs)};"
        case CReturn(None):
            return "return;"
        case CReturn(CExpression() as expr):
            return f"return {generate_expr(expr)};"
        case CWhile(cond, stmts):
            body = "".join(map(generate_stmt, stmts))
            return f"while({generate_expr(cond)}){{{body}}}"
        case _:
            raise NotImplementedError(f"missing printing pass for {type(stmt)} {stmt}")


def generate_program(p: CProgram) -> str:
    # Includes
    output = [
        f'#include {x}'
        for x in ['<stddef.h>', '<stdint.h>', '"configuration.h"', '"helpers.h"']
    ]
    output.insert(2, "")
    output.insert(5, "")

    # Functions
    for f in p.functions:
        # Params
        params = ",".join([f"{generate_type(ty)} {name}" for ty, name in f.parameters])
        output.append(f"{generate_type(f.return_type)} {f.name}({params})" + "{")
        # Statements
        for s in f.statements:
            assert s
        output.extend(map(generate_stmt, f.statements))
        # Closing curly brace and empty line
        output.append("}\n")
    return "\n".join(output)
