from typing import List

from ir.c_like.c_nodes import (
    CFunction,
    CProgram,
    CReturn,
    CScalarAddition,
    CScalarConst,
    CScalarDivision,
    CScalarExpression,
    CScalarMultiplication,
    CScalarParameter,
    CScalarSubtraction,
    CStatement,
)
from ir.high_level.nodes import IRBinOp, IRConst, IRFunction, IRNode, IRProgram, IRVar
from ir.types import Type


def lower_hl_index_expression(hl_ie: IRNode) -> CScalarExpression:
    match hl_ie:
        case IRConst(Type.INDEX, value) as x:
            return CScalarConst(value)
        case IRVar(Type.INDEX, name):
            return CScalarParameter(name)
        case IRBinOp(Type.INDEX, '+', left, right):
            return CScalarAddition(
                lower_hl_index_expression(left),
                lower_hl_index_expression(right)
            )
        case IRBinOp(Type.INDEX, '-', left, right):
            return CScalarSubtraction(
                lower_hl_index_expression(left),
                lower_hl_index_expression(right)
            )
        case IRBinOp(Type.INDEX, '*', left, right):
            return CScalarMultiplication(
                lower_hl_index_expression(left),
                lower_hl_index_expression(right)
            )
        case IRBinOp(Type.INDEX, '/', left, right):
            return CScalarDivision(
                lower_hl_index_expression(left),
                lower_hl_index_expression(right)
            )
        case IRNode(Type.BIGINT):
            raise RuntimeError("internal error, index-only function")
        case x:
            raise NotImplementedError(f"{type(x)}")


def lower_hl_function(hl_f: IRFunction) -> CFunction:
    # Parameters
    parameters = [(p.ty, p.name) for p in hl_f.params]
    # TODO some sort of env
    # Body
    statements: List[CStatement] = []
    match hl_f.body.ty:
        case Type.INDEX:
            # Expand expression, return
            statements.append(CReturn(lower_hl_index_expression(hl_f.body)))
        case Type.BIGINT:
            # Tough luck
            raise NotImplementedError("Bigint expression")
    # Return
    return CFunction(hl_f.name, parameters, statements, hl_f.ty)


def lower_hl_program(hl_ir: IRProgram) -> CProgram:
    return CProgram([lower_hl_function(f) for f in hl_ir.functions])
