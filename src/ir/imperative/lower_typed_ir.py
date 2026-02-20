from typing import List, Tuple

from ir.imperative.imperative_nodes import (
    IArrayAccess,
    IBinOp,
    IBlock,
    IConst,
    IExpr,
    IFunction,
    IParam,
    IProgram,
    IReturn,
    IStmt,
    IUnaryMinus,
    IVar,
)
from ir.typed.typed_nodes import (
    TArrayAccess,
    TBinOp,
    TCall,
    TConst,
    TFunction,
    TNode,
    TPower,
    TProgram,
    TReduction,
    TUnaryMinus,
    TVar,
)


def lower_typed_expression(e: TNode) -> Tuple[IExpr, List[IStmt]]:
    match e:
        case TConst(ty, value):
            return (IConst(ty, value), [])
        case TVar(ty, name):
            return (IVar(ty, name), [])
        case TArrayAccess(ty, array, index):
            arr, stmts_arr = lower_typed_expression(array)
            ind, stmts_ind = lower_typed_expression(index)
            assert isinstance(arr, IVar)
            return (IArrayAccess(ty, arr, ind), stmts_arr + stmts_ind)
        case TBinOp(ty, op, left, right):
            ll, stmts_left = lower_typed_expression(left)
            rr, stmts_right = lower_typed_expression(right)
            return (IBinOp(ty, op, ll, rr), stmts_left + stmts_right)
        case TUnaryMinus(ty, body):
            b, stmts = lower_typed_expression(body)
            return (IUnaryMinus(ty, b), stmts)
        case TPower():
            raise NotImplementedError()
        case TCall():
            raise NotImplementedError()
        case TReduction():
            raise NotImplementedError()
        case _:
            raise RuntimeError(type(e))


def lower_typed_function(f: TFunction) -> IFunction:
    result, statements = lower_typed_expression(f.body)
    statements.append(IReturn(result))
    return IFunction(
        f.name,
        [IParam(p.name, p.ty) for p in f.params],
        f.return_type,
        IBlock(statements),
    )


def lower_typed_program(prog: TProgram) -> IProgram:
    return IProgram([lower_typed_function(f) for f in prog.functions])
