import copy
from typing import Dict, List

from ir.env import Env
from ir.typed.typed_nodes import (
    TArrayAccess,
    TBinOp,
    TCall,
    TConst,
    TFunction,
    TFunctionSignature,
    TIfElse,
    TNode,
    TPower,
    TProgram,
    TReduction,
    TUnaryMinus,
    TVar,
)
from ir.types import ArrayType, BigIntType, IndexType, LoweringError
from parsing.ast.ast_nodes import (
    Add,
    ArrayAccess,
    Call,
    Div,
    Eq,
    Expr,
    Function,
    Ge,
    Gt,
    IfElse,
    Int,
    Le,
    Lt,
    Mul,
    Neg,
    Neq,
    Power,
    Program,
    Reduction,
    Sub,
    Var,
)


def lower_ast_expr(ast: Expr, env: Env) -> TNode:  # noqa: C901
    match ast:
        case Int():
            return TConst(ast.type, ast.value)
        case Var():
            # Variable should be defined
            if ast.name not in env.vars:
                raise LoweringError(f"Undefined variable {ast.name}")
            return env.vars[ast.name]

        case ArrayAccess():
            # Name should be defined
            if ast.array not in env.vars:
                raise LoweringError(f"Undefined array {ast.array}")
            # Array
            base = env.vars[ast.array]
            # Base must be an array
            if not isinstance(base.ty, ArrayType):
                raise LoweringError(
                    # TODO too strict? Do index arrays make sense?
                    f"Bracket notation implies a mandatory array type. "
                    f"Illegal attempt on {ast.array}"
                )
            # Index
            index = lower_ast_expr(ast.index, env)
            if index.ty != IndexType():
                f"Array index type must be index, got {index.ty}"
            return TArrayAccess(base.ty.elem, base, index)

        case Add():
            return lower_ast_binop("+", ast.left, ast.right, env)

        case Sub():
            return lower_ast_binop("-", ast.left, ast.right, env)

        case Mul():
            return lower_ast_binop("*", ast.left, ast.right, env)

        case Div():
            return lower_ast_binop("/", ast.left, ast.right, env)

        case Power():
            base = lower_ast_expr(ast.base, env)
            exponent = lower_ast_expr(ast.exponent, env)
            # Paper-specific constraints
            if base.ty != BigIntType():
                raise LoweringError(
                    f"exponentiation is only permitted on {BigIntType()} type, "
                    f"found {base.ty}"
                )
            if exponent.ty != IndexType():
                raise LoweringError(
                    f"exponents must have type {IndexType()}, found {exponent.ty}"
                )
            return TPower(base.ty, base, exponent)

        case Neg():
            body = lower_ast_expr(ast.body, env)
            if body.ty != IndexType():
                raise LoweringError(
                    f"unary minus can only be used on expressions of type {IndexType()}"
                    f", found {body.ty}"
                )
            return TUnaryMinus(IndexType(), body)

        case Eq(lhs, rhs):
            return lower_ast_binop("==", lhs, rhs, env)
        case Neq(lhs, rhs):
            return lower_ast_binop("!=", lhs, rhs, env)
        case Lt(lhs, rhs):
            return lower_ast_binop("<", lhs, rhs, env)
        case Le(lhs, rhs):
            return lower_ast_binop("<=", lhs, rhs, env)
        case Gt(lhs, rhs):
            return lower_ast_binop(">", lhs, rhs, env)
        case Ge(lhs, rhs):
            return lower_ast_binop(">=", lhs, rhs, env)

        case Reduction():
            return lower_ast_reduction(ast, env)

        case IfElse(condition, then_branch, else_branch):
            lo_cond, lo_then, lo_else = [
                lower_ast_expr(x, env) for x in [condition, then_branch, else_branch]
            ]
            if lo_cond.ty != IndexType():
                raise LoweringError(f"If condition must be of type {IndexType()}")
            if lo_then.ty != lo_else.ty:
                raise LoweringError(
                    f"Arms of if-clause must be of identical type, "
                    f"found {lo_then.ty} and {lo_else.ty}"
                )
            return TIfElse(lo_then.ty, lo_cond, lo_then, lo_else)

        case Call():
            return lower_ast_call(ast, env)
        case _:
            raise NotImplementedError(f"lowering of {type(ast)}")


def lower_ast_comparison(op: str, lhs: Expr, rhs: Expr, env: Env) -> TBinOp:
    left = lower_ast_expr(lhs, env)
    right = lower_ast_expr(rhs, env)
    if left.ty != IndexType() or right.ty != IndexType():
        raise LoweringError(f"Comparisons are only allowed on {IndexType()}")
    return TBinOp(IndexType(), op, left, right)


def lower_ast_binop(op: str, lhs: Expr, rhs: Expr, env: Env) -> TBinOp:
    left = lower_ast_expr(lhs, env)
    right = lower_ast_expr(rhs, env)

    if left.ty == right.ty:
        if op == "-" and left.ty == BigIntType():
            raise LoweringError("field subtraction not allowed")
        if op == "/" and left.ty == BigIntType():
            raise NotImplementedError("Field division? What do we do?")
        return TBinOp(left.ty, op, left, right)

    raise LoweringError(f"type mismatch on {op} operation")


def lower_ast_reduction(ast: Reduction, env: Env) -> TReduction:
    # Start, stop, step
    start = lower_ast_expr(ast.start, env)
    stop = lower_ast_expr(ast.stop, env)
    step = lower_ast_expr(ast.step, env)
    for n in (start, stop, step):
        if n.ty != IndexType():
            raise LoweringError("Reduction bounds must be indices")

    # TODO: Shadowing
    if ast.var in env.vars:
        raise NotImplementedError(
            f"Reduction variable '{ast.var}' shadows an existing variable"
        )

    # TODO: is a copy necessary here?
    inner_env = Env(vars=dict(env.vars), signatures=env.signatures)
    inner_env.vars[ast.var] = TVar(IndexType(), ast.var)

    body = lower_ast_expr(ast.body, inner_env)

    return TReduction(
        body.ty,
        ast.op,
        ast.var,
        start,
        stop,
        step,
        body,
    )


def lower_ast_call(ast: Call, env: Env) -> TCall:
    # Function must exist
    if ast.func not in env.signatures:
        raise LoweringError(f"call to undefined function '{ast.func}'")
    signature = env.signatures[ast.func]

    # Lower arguments
    args: List[TNode] = []
    for arg in ast.args:
        lo = lower_ast_expr(arg, env)
        args.append(lo)

    # Check number of arguments
    if len(args) != len(signature.params):
        raise LoweringError(
            f"function '{ast.func}' expects {len(signature.params)} args, "
            f"got {len(args)}"
        )

    # Check argument types
    for arg_node, param in zip(args, signature.params):
        if arg_node.ty != param:
            raise LoweringError(
                f"Function '{ast.func}' argument type mismatch for parameter "
                f"'{arg_node.name}': expected {param}, got {arg_node.ty}"  # type: ignore
            )

    return TCall(signature.return_type, signature.name, args)


def lower_ast_function(ast: Function, env: Env) -> TFunction:
    # Assuming no globals
    params: list[TVar] = []
    for name, ty in ast.params:
        if name in env.vars:
            raise LoweringError(f"duplicate parameter '{name}' in function {ast.name}")
        var = TVar(ty, name)
        env.vars[name] = var
        params.append(var)
    # Lower body
    body = lower_ast_expr(ast.body, env)
    # Only allow subset of return types
    if ast.return_type not in [IndexType(), BigIntType()]:
        raise LoweringError(
            f"function '{ast.name}' declared "
            f"return type {ast.return_type}, but only index or bigint are allowed"
        )
    # Typechecking
    if body.ty != ast.return_type:
        raise LoweringError(
            f"function '{ast.name}' declared return type '{ast.return_type}' but "
            f"its body has type '{body.ty}'"
        )
    return TFunction(ast.name, params, ast.return_type, body)


def lower_ast_program(ast: Program) -> TProgram:
    # Collect function signatures
    signatures: Dict[str, TFunctionSignature] = {}
    for fn in ast.functions:
        if fn.name in signatures:
            raise LoweringError(f"duplicate function {fn.name}")
        param_types = [p[1] for p in fn.params]
        signatures[fn.name] = TFunctionSignature(
            name=fn.name, params=param_types, return_type=fn.return_type
        )

    # Lower functions, each with a fresh environment!
    functions: List[TFunction] = []
    for f in ast.functions:
        try:
            functions.append(
                lower_ast_function(
                    f, Env(vars={}, signatures=copy.deepcopy(signatures))
                )
            )
        except LoweringError as e:
            raise LoweringError(f"in '{f.name}': {e}") from e

    return TProgram(functions)
