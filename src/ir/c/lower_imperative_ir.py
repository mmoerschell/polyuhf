from typing import List, Tuple

from ir.c.c_nodes import (
    CArrayAccess,
    CAssign,
    CBinOp,
    CConst,
    CDeclaration,
    CExpression,
    CFunction,
    CProgram,
    CReturn,
    CStatement,
    CUnaryMinus,
    CVariable,
    CWhile,
)
from ir.imperative.imperative_nodes import (
    IArrayAccess,
    IAssign,
    IBinOp,
    ICall,
    IConst,
    IDecl,
    IExpr,
    IFunction,
    IPower,
    IProgram,
    IReturn,
    IStmt,
    IUnaryMinus,
    IVar,
    IWhile,
)
from ir.types import BigIntType, IndexType


def lower_imperative_index_expr(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:
    assert isinstance(expr.ty, IndexType)
    match expr:
        case IConst(IndexType(), value):
            return CConst(value), []
        case IVar(IndexType(), name):
            return CVariable(name), []
        case IArrayAccess(IndexType(), array, index):
            aa = CVariable(array.name)
            ii, stmts_ii = lower_imperative_expr(index)
            assert isinstance(aa, CVariable)
            return CArrayAccess(aa, ii), stmts_ii
        case IBinOp(IndexType(), op, left, right):
            ll, stmts_left = lower_imperative_expr(left)
            rr, stmts_right = lower_imperative_expr(right)
            return CBinOp(op, ll, rr), stmts_left + stmts_right
        case IUnaryMinus(IndexType(), body):
            bb, stmts = lower_imperative_expr(body)
            return CUnaryMinus(bb), stmts
        case IPower(IndexType()):
            raise NotImplementedError(type(expr))
        case ICall(IndexType()):
            raise NotImplementedError(type(expr))
        case _:
            raise NotImplementedError(type(expr))


def lower_imperative_bigint_expr(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:
    assert isinstance(expr.ty, BigIntType)
    match expr:
        case IConst(BigIntType(), value):
            return CConst(value), []
        case IVar(BigIntType(), name):
            return CVariable(name), []
        case IArrayAccess(BigIntType()):
            raise NotImplementedError(type(expr))
        case IBinOp(BigIntType(), op, left, right):
            ll, stmts_left = lower_imperative_expr(left)
            rr, stmts_right = lower_imperative_expr(right)
            return CBinOp(op, ll, rr), stmts_left + stmts_right
        case IUnaryMinus(BigIntType(), body):
            bb, stmts = lower_imperative_expr(body)
            return CUnaryMinus(bb), stmts
        case IPower(BigIntType()):
            raise NotImplementedError(type(expr))
        case ICall(BigIntType()):
            raise NotImplementedError(type(expr))
        case _:
            raise NotImplementedError(type(expr))


# def lower_imperative_array_expr(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:
#     assert isinstance(expr.ty, ArrayType)

#     pass


def lower_imperative_expr(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:
    match expr.ty:
        case IndexType():
            return lower_imperative_index_expr(expr)
        case BigIntType():
            return lower_imperative_bigint_expr(expr)
        case _:
            raise NotImplementedError()
        # case ArrayType():
        #     return lower_imperative_array_expr(expr)


def lower_imperative_statement(stmt: IStmt) -> List[CStatement]:
    output: List[CStatement] = []
    match stmt:
        case IDecl(IVar(ty, name), init):
            # # Type
            # c_type = "struct bigint" if ty == BigIntType() else "int64_t"
            # Initializer
            if init:
                c_expr, intermediate_statments = lower_imperative_expr(init)
                output.extend(intermediate_statments)
                output.append(CDeclaration(ty, name, c_expr))
            else:
                output.append(CDeclaration(ty, name, None))
        case IAssign(lhs, rhs):
            lo_rhs, stmts_rhs = lower_imperative_expr(rhs)
            match lhs:
                case IVar(_, name):
                    return stmts_rhs + [CAssign(CVariable(name), lo_rhs)]
                case IArrayAccess():
                    raise NotImplementedError()
                case _:
                    raise ValueError(f"invalid lhs of assignment {lhs}")
        case IReturn(expr):
            c_expr, intermediate_statments = lower_imperative_expr(expr)
            output.extend(intermediate_statments)
            output.append(CReturn(c_expr))
        case IWhile(cond, body):
            lo_cond, stmts_cond = lower_imperative_expr(cond)
            stmts_body = sum(map(lower_imperative_statement, body.stmts), [])  # type: ignore
            # recompute condition after every iteration
            return stmts_cond + [CWhile(lo_cond, stmts_body + stmts_cond)]
        case _:
            raise ValueError(f"undefined statement {type(stmt)}")
    return output


def lower_imperative_function(f: IFunction) -> CFunction:
    return CFunction(
        f.name,
        [(p.ty, p.name) for p in f.params],
        # Concatenate C statments emanating from each imperative statement
        sum(map(lower_imperative_statement, f.body.stmts), []),  # type: ignore
        f.return_type,
    )


def lower_imperative_program(p: IProgram) -> CProgram:
    return CProgram([lower_imperative_function(f) for f in p.functions])
