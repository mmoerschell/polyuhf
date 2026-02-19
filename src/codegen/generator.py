from ir.c_like.c_nodes import (
    CProgram,
    CReturn,
    CScalarAddition,
    CScalarConst,
    CScalarDivision,
    CScalarExpression,
    CScalarMultiplication,
    CScalarParameter,
    CScalarSubtraction,
)
from ir.types import Type

INTEGER_TYPE = "int64_t"
BIGINT_TYPE = "void*"


def generate_scalar_expression(e: CScalarExpression) -> str:
    match e:
        case CScalarConst(value):
            return f"{value}L"  # TODO U for unsigned?
        case CScalarParameter(name):
            return name
        case CScalarAddition(op1, op2):
            return f"{
                generate_scalar_expression(op1)
            }+{
                generate_scalar_expression(op2)
            }"
        case CScalarSubtraction(op1, op2):
            return f"{
                generate_scalar_expression(op1)
            }-{
                generate_scalar_expression(op2)
            }"
        case CScalarMultiplication(op1, op2):
            return f"{
                generate_scalar_expression(op1)
            }*{
                generate_scalar_expression(op2)
            }"
        case CScalarDivision(op1, op2):
            return f"{
                generate_scalar_expression(op1)
            }/{
                generate_scalar_expression(op2)
            }"
        case x:
            raise NotImplementedError(f"{type(x)}")



def generate_program(p: CProgram) -> str:
    # Imports
    output = ["#import <stdint.h>", ""]

    # TODO data-strucutre declarations

    # Functions
    for f in p.functions:
        # Params
        ctype = INTEGER_TYPE if f.return_type == Type.INDEX else "void"
        params = ",".join([
            f"{INTEGER_TYPE if ty == Type.INDEX else BIGINT_TYPE} {nm}"
            for ty, nm in f.parameters
        ])
        output.append(f"{ctype} {f.name}({params})"+"{")

        # Statements
        for s in f.statements:
            match s:
                case CReturn(None):
                    output.append("return;")
                case CReturn(CScalarExpression() as expr):
                    output.append(f"return {generate_scalar_expression(expr)};")
                case x:
                    raise NotImplementedError(f"{type(x)}")

        output.append("}")
    return "\n".join(output)
