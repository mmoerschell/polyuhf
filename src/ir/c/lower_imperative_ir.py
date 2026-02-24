from typing import List, Tuple

from ir.c.c_nodes import (
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
from ir.types import Type


def lower_imperative_index_expr(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:
    assert expr.ty == Type.INDEX
    match expr:
        case IConst(Type.INDEX, value):
            return (CConst(value), [])
        case IVar(Type.INDEX, name):
            return (CVariable(name), [])
        case IArrayAccess(Type.INDEX):
            raise NotImplementedError(type(expr))
        case IBinOp(Type.INDEX, op, left, right):
            ll, stmts_left = lower_imperative_index_expr(left)
            rr, stmts_right = lower_imperative_index_expr(right)
            return (CBinOp(op, ll, rr), stmts_left + stmts_right)
        case IUnaryMinus(Type.INDEX, body):
            bb, stmts = lower_imperative_index_expr(body)
            return (CUnaryMinus(bb), stmts)
        case IPower(Type.INDEX):
            raise NotImplementedError(type(expr))
        case ICall(Type.INDEX):
            raise NotImplementedError(type(expr))
        case _:
            raise NotImplementedError(type(expr))


def lower_imperative_bigint_expr(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:
    assert expr.ty == Type.BIGINT
    match expr:
        case IConst(Type.BIGINT, value):
            return (CConst(value), [])
        case IVar(Type.BIGINT, name):
            return (CVariable(name), [])
        case IArrayAccess(Type.BIGINT):
            raise NotImplementedError(type(expr))
        case IBinOp(Type.BIGINT, op, left, right):
            ll, stmts_left = lower_imperative_bigint_expr(left)
            rr, stmts_right = lower_imperative_bigint_expr(right)
            return (CBinOp(op, ll, rr), stmts_left + stmts_right)
        case IUnaryMinus(Type.BIGINT, body):
            bb, stmts = lower_imperative_bigint_expr(body)
            return (CUnaryMinus(bb), stmts)
        case IPower(Type.BIGINT):
            raise NotImplementedError(type(expr))
        case ICall(Type.BIGINT):
            raise NotImplementedError(type(expr))
        case _:
            raise NotImplementedError(type(expr))


def lower_imperative_expression(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:
    match expr.ty:
        case Type.INDEX:
            return lower_imperative_index_expr(expr)
        case Type.BIGINT:
            return lower_imperative_bigint_expr(expr)


def lower_imperative_statement(stmt: IStmt) -> List[CStatement]:
    output: List[CStatement] = []
    match stmt:
        case IDecl(IVar(ty, name), init):
            # # Type
            # c_type = "struct bigint" if ty == Type.BIGINT else "int64_t"
            # Initializer
            if init:
                c_expr, intermediate_statments = lower_imperative_expression(init)
                output.extend(intermediate_statments)
                output.append(CDeclaration(ty, name, c_expr))
            else:
                output.append(CDeclaration(ty, name, None))
        case IAssign(lhs, rhs):
            lo_rhs, stmts_rhs = lower_imperative_expression(rhs)
            match lhs:
                case IVar(_, name):
                    return stmts_rhs + [CAssign(CVariable(name), lo_rhs)]
                case IArrayAccess():
                    raise NotImplementedError()
                case _:
                    raise ValueError(f"invalid lhs of assignment {lhs}")
        case IReturn(expr):
            c_expr, intermediate_statments = lower_imperative_expression(expr)
            output.extend(intermediate_statments)
            output.append(CReturn(c_expr))
        case IWhile(cond, body):
            lo_cond, stmts_cond = lower_imperative_expression(cond)
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
