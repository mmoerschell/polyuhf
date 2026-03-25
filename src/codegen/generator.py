from field_configuration import FieldConfiguration
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
            return "uint64_t"
        case BigIntType():
            return "bigint_t"
        case ArrayType(None, elem):
            return f"{generate_type(elem)}*"
        case ArrayType(int(size), elem):
            return f"{generate_type(elem)}[{size}]"
        case _:
            raise ValueError("pattern matching")


def generate_expr(expr: CExpression, field_configuration: FieldConfiguration) -> str:
    match expr:
        case CIdentifier(name):
            return name
        case CArrayAccess(array, index):
            return f"{generate_expr(array, field_configuration)}[{generate_expr(index, field_configuration)}]"
        case CConst(ty, value):
            match ty:
                case IndexType():
                    return str(value)
                case BigIntType():
                    limbs_consts = [
                        (value >> (i * field_configuration.lambda_))
                        & field_configuration.lambda_mask
                        for i in range(field_configuration.limbs)
                    ]
                    return f"bigint_t{{.limbs={{{','.join([f'{hex(x)}UL' for x in limbs_consts])}}}}}"
                case ArrayType(_):
                    raise LoweringError("array-typed constants?")
        case CBinOp(op, lhs, rhs):
            # Parentheses: better safe than sorry
            return f"(({generate_expr(lhs, field_configuration)}){op}({generate_expr(rhs, field_configuration)}))"
        case CFunctionCall(func, args):
            chained_args = ",".join(
                [generate_expr(e, field_configuration) for e in args]
            )
            return f"{func}({chained_args})"
        case _:
            raise NotImplementedError(f"missing printing pass for expr {type(expr)}")


def generate_stmt(stmt: CStatement, field_configuration: FieldConfiguration) -> str:
    match stmt:
        case CDeclaration(ty, name, None):
            return f"{generate_type(ty)} {name};"
        case CDeclaration(ty, name, CExpression() as init):
            return f"{generate_type(ty)} {name}={generate_expr(init, field_configuration)};"
        case CAssign(CIdentifier(name), rhs):
            return f"{name}={generate_expr(rhs, field_configuration)};"
        case CAssign(CArrayAccess(CIdentifier(name)), rhs):
            return f"{name}={generate_expr(rhs, field_configuration)};"
        case CReturn(None):
            return "return;"
        case CReturn(CExpression() as expr):
            return f"return {generate_expr(expr, field_configuration)};"
        case CWhile(cond, stmts):
            body = "".join([generate_stmt(s, field_configuration) for s in stmts])
            return f"while({generate_expr(cond, field_configuration)}){{{body}}}"
        case _:
            raise NotImplementedError(f"missing printing pass for {type(stmt)} {stmt}")


def generate_program(p: CProgram, field_configuration: FieldConfiguration) -> str:
    # Field configuration (datastructures) and arithmetic
    output = [field_configuration.as_code(), ""]

    # Functions
    for f in p.functions:
        # Params
        params = ",".join([f"{generate_type(ty)} {name}" for ty, name in f.parameters])
        output.append(f"inline {generate_type(f.return_type)} {f.name}({params})" + "{")
        # Statements
        for s in f.statements:
            assert s
        output.extend([generate_stmt(s, field_configuration) for s in f.statements])
        # Closing curly brace and empty line
        output.append("}\n")
    return "\n".join(output)
