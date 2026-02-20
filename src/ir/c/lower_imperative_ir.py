from typing import List, Tuple

from ir.c.c_nodes import (
    CConst,
    CDeclaration,
    CExpression,
    CFunction,
    CProgram,
    CReturn,
    CStatement,
    CUnaryMinus,
    CVariable,
)
from ir.imperative.imperative_nodes import (
    IArrayAccess,
    IAssign,
    IBinOp,
    IBlock,
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
from ir.typed.typed_nodes import (
    TBinOp,
    TConst,
    TFunction,
    TNode,
    TProgram,
    TReduction,
    TVar,
)
from ir.types import Type


def lower_imperative_expression(e: IExpr) -> Tuple[CExpression, List[CStatement]]:
    match e:
        case IConst(Type.INDEX, value):
            return (CConst(value), [])
        case IVar(
            Type.INDEX, name
        ):
            return (CVariable(name), [])
        case IArrayAccess(
            Type.INDEX,
        ):
            raise NotImplementedError(type(e))
        case IBinOp(
            Type.INDEX,
        ):
            raise NotImplementedError(type(e))
        case IUnaryMinus(Type.INDEX, body):
            bb, stmts = lower_imperative_expression(body)
            return (CUnaryMinus(bb), stmts)
        case IPower(
            Type.INDEX,
        ):
            raise NotImplementedError(type(e))
        case ICall(
            Type.INDEX,
        ):
            raise NotImplementedError(type(e))
        case _:
            raise RuntimeError(f"{type(e)} {e.ty}")


def lower_imperative_statement(stmt: IStmt) -> List[CStatement]:
    output: List[CStatement] = []
    match stmt:
        case IDecl(ty, name, init):
            # Type
            c_type = "struct bigint" if ty == Type.BIGINT else "int64_t"
            # Initializer
            if init:
                c_expr, intermediate_statments = lower_imperative_expression(init)
                output.extend(intermediate_statments)
                output.append(CDeclaration(c_type, name, c_expr))
            else:
                output.append(CDeclaration(c_type, name, None))
        case IAssign():
            raise NotImplementedError(type(stmt))
        case IReturn(expr):
            c_expr, intermediate_statments = lower_imperative_expression(expr)
            output.extend(intermediate_statments)
            output.append(CReturn(c_expr))
        case IWhile():
            raise NotImplementedError(type(stmt))
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
