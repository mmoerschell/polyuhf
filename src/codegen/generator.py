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
from settings import BigIntConfiguration


# One level higher ATM
def generate_type(t: Type) -> str:
    match t:
        case IndexType():
            return "uint64_t"
        case BigIntType():
            return "bigint_t"
        case ArrayType(None, elem):
            return f"{generate_type(elem)}*"
        case ArrayType(int(size), elem):
            return f"{generate_type(elem)}[{size}]"
        case _:
            raise ValueError("pattern matching")


def generate_expr(expr: CExpression, bigint_config: BigIntConfiguration) -> str:
    match expr:
        case CIdentifier(name):
            return name
        case CArrayAccess(array, index):
            return f"{generate_expr(array, bigint_config)}[{generate_expr(index, bigint_config)}]"
        case CConst(ty, value):
            match ty:
                case IndexType():
                    return str(value)
                case BigIntType():
                    lambd_mask = (1 << bigint_config.lambd) - 1
                    limbs_consts = [
                        (value >> (i * bigint_config.lambd)) & lambd_mask
                        for i in range(bigint_config.limbs)
                    ]
                    return f"bigint_t{{.limbs={{{','.join([f'{hex(x)}UL' for x in limbs_consts])}}}}}"
                case ArrayType(_):
                    raise LoweringError("array-typed constants?")
        case CBinOp(op, lhs, rhs):
            # Parentheses: better safe than sorry
            return f"(({generate_expr(lhs, bigint_config)}){op}({generate_expr(rhs, bigint_config)}))"
        case CFunctionCall(func, args):
            chained_args = ",".join([generate_expr(e, bigint_config) for e in args])
            return f"{func}({chained_args})"
        case _:
            raise NotImplementedError(f"missing printing pass for expr {type(expr)}")


def generate_stmt(stmt: CStatement, bigint_config: BigIntConfiguration) -> str:
    match stmt:
        case CDeclaration(ty, name, None):
            return f"{generate_type(ty)} {name};"
        case CDeclaration(ty, name, CExpression() as init):
            return f"{generate_type(ty)} {name}={generate_expr(init, bigint_config)};"
        case CAssign(CIdentifier(name), rhs):
            return f"{name}={generate_expr(rhs, bigint_config)};"
        case CAssign(CArrayAccess(CIdentifier(name)), rhs):
            return f"{name}={generate_expr(rhs, bigint_config)};"
        case CReturn(None):
            return "return;"
        case CReturn(CExpression() as expr):
            return f"return {generate_expr(expr, bigint_config)};"
        case CWhile(cond, stmts):
            body = "".join([generate_stmt(s, bigint_config) for s in stmts])
            return f"while({generate_expr(cond, bigint_config)}){{{body}}}"
        case _:
            raise NotImplementedError(f"missing printing pass for {type(stmt)} {stmt}")


def generate_program(p: CProgram, bigint_config: BigIntConfiguration) -> str:
    # This and that
    output = [
        "#pragma once",
        f"// Generated for "
        f"{str(bigint_config.field)} "
        f"({bigint_config.limbs}x{bigint_config.lambd} bits)",
    ]

    # Includes
    output.extend(
        [
            f"#include {x}"
            for x in ["<stddef.h>", "<stdint.h>", '"configuration.h"', '"helpers.h"']
        ]
    )

    # Add a few empty lines
    for line in [1, 3, 6, 9]:
        output.insert(line, "")

    # Functions
    for f in p.functions:
        # Params
        params = ",".join([f"{generate_type(ty)} {name}" for ty, name in f.parameters])
        output.append(f"{generate_type(f.return_type)} {f.name}({params})" + "{")
        # Statements
        for s in f.statements:
            assert s
        output.extend([generate_stmt(s, bigint_config) for s in f.statements])
        # Closing curly brace and empty line
        output.append("}\n")
    return "\n".join(output)
