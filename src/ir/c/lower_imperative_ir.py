from typing import List, Tuple

from helpers import BUILTIN_BIGINT_FUNCTIONS
from ir.c.c_nodes import (
    CArrayAccess,
    CAssign,
    CBinOp,
    CConst,
    CDeclaration,
    CExpression,
    CFunction,
    CFunctionCall,
    CIdentifier,
    CProgram,
    CReturn,
    CStatement,
    CUnaryMinus,
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
from ir.types import ArrayType, BigIntType, IndexType, LoweringError


def lower_imperative_expr(expr: IExpr) -> Tuple[CExpression, List[CStatement]]:  # noqa: C901
    match expr:
        case IConst(ty, value):
            return CConst(ty, value), []
        case IVar(ty, name):
            return CIdentifier(name), []
        case IArrayAccess(ty, array, index):
            aa = CIdentifier(array.name)
            ii, stmts_ii = lower_imperative_expr(index)
            assert isinstance(aa, CIdentifier)
            return CArrayAccess(aa, ii), stmts_ii
        case IBinOp(ty, op, left, right):
            ll, stmts_left = lower_imperative_expr(left)
            rr, stmts_right = lower_imperative_expr(right)
            match ty:
                case IndexType():
                    return CBinOp(op, ll, rr), stmts_left + stmts_right
                case BigIntType():
                    # NOTE handle this here and not in Imperative IR
                    if op not in BUILTIN_BIGINT_FUNCTIONS.keys():
                        raise LoweringError(f"Invalid bigint operator '{op}'")
                    return (
                        CFunctionCall(BUILTIN_BIGINT_FUNCTIONS[op], [ll, rr]),
                        stmts_left + stmts_right,
                    )
                case ArrayType():
                    raise RuntimeError("no sane binop produces an array")
        case IUnaryMinus(ty, body):
            bb, stmts = lower_imperative_expr(body)
            return CUnaryMinus(bb), stmts
        case IPower(ty):
            raise NotImplementedError(type(expr))
        case ICall(ty):
            raise NotImplementedError(type(expr))
        case _:
            raise NotImplementedError(type(expr))


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
                    return stmts_rhs + [CAssign(CIdentifier(name), lo_rhs)]
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
