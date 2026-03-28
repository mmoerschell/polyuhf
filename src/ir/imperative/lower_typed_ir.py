from typing import List, Tuple

from ir.imperative.imperative_nodes import (
    IArrayAccess,
    IAssign,
    IBinOp,
    IBlock,
    IConst,
    IDecl,
    IExpr,
    IFunction,
    IIfElse,
    IParam,
    IPower,
    IProgram,
    IReturn,
    IStmt,
    IUnaryMinus,
    IVar,
    IWhile,
)
from ir.typed.typed_nodes import (
    TArrayAccess,
    TBinOp,
    TCall,
    TConst,
    TFunction,
    TIfElse,
    TNode,
    TPower,
    TProgram,
    TReduction,
    TUnaryMinus,
    TVar,
)
from ir.types import IndexType

variable_name_counter = 0


def fresh_var_name() -> str:
    global variable_name_counter
    variable_name_counter += 1
    return f"_{variable_name_counter}"


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
        case TPower(ty, base, exponent):
            match exponent:
                # Small consts: turn into multiplication
                case TConst(IndexType(), 2):
                    return lower_typed_expression(TBinOp(base.ty, "*", base, base))
                # Other expressions: keep it as a power
                case TNode(IndexType()):
                    bb, stmts_base = lower_typed_expression(base)
                    ee, stmts_exp = lower_typed_expression(exponent)
                    return IPower(base.ty, bb, ee), stmts_base + stmts_exp
                case _:
                    raise NotImplementedError()
        case TIfElse(ty, cond, if_branch, else_branch):
            cc, stmts_cc = lower_typed_expression(cond)
            ii, stmts_if = lower_typed_expression(if_branch)
            ee, stmts_el = lower_typed_expression(else_branch)
            result = IVar(ty, fresh_var_name() + "_ie")
            stmts: List[IStmt] = []
            stmts += stmts_cc
            stmts.append(IDecl(result, None))
            stmts.append(
                IIfElse(
                    cc,
                    IBlock(stmts_if + [IAssign(result, ii)]),
                    IBlock(stmts_el + [IAssign(result, ee)]),
                )
            )
            return result, stmts
        case TCall():
            raise NotImplementedError()
        case TReduction(ty, op, var, start, stop, step, body):
            output: List[IStmt] = []
            # Lower start, stop, step expressions
            lo_start, stmts_start = lower_typed_expression(start)
            lo_stop, stmts_stop = lower_typed_expression(stop)
            lo_step, stmts_step = lower_typed_expression(step)
            output.extend(stmts_start + stmts_stop + stmts_step)
            # Declare accumulator
            accumulator = IVar(ty, fresh_var_name() + "_acc")
            output.append(IDecl(accumulator, IConst(ty, 0 if op == "+" else 1)))
            # Declare loop index variable
            loop_index = IVar(IndexType(), var)
            output.append(IDecl(loop_index, lo_start))
            # Loop condition
            cond = IBinOp(IndexType(), "<", loop_index, lo_stop)
            # Loop body
            lo_body, stmts_body = lower_typed_expression(body)
            body_block = IBlock(
                # Loop body computation
                # TODO: Loop-invariant code motion?
                stmts_body
                + [
                    # Loop body reduction
                    IAssign(accumulator, IBinOp(ty, op, accumulator, lo_body)),
                    # Loop increment
                    IAssign(loop_index, IBinOp(IndexType(), "+", loop_index, lo_step)),
                ]
            )
            output.append(IWhile(cond, body_block))
            return (accumulator, output)
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
