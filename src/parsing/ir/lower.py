import copy
from typing import Dict, List

from parsing.ast.nodes import (
    Add,
    ArrayAccess,
    Call,
    Div,
    Expr,
    Function,
    Int,
    Mul,
    Neg,
    Power,
    Program,
    Reduction,
    Sub,
    Var,
)

from .env import Env
from .nodes import (
    FunctionSignature,
    IRArrayAccess,
    IRBinOp,
    IRCall,
    IRConst,
    IRFunction,
    IRNode,
    IRPower,
    IRProgram,
    IRReduction,
    IRVar,
)
from .types import Type


class LoweringError(Exception):
    pass


def lower_expr(ast: Expr, env: Env) -> IRNode:  # noqa: C901
    if isinstance(ast, Int):
        # TODO: allow bigint literals?
        # In that case, constants would not always have type INDEX
        return IRConst(ast.value, Type.INDEX)

    if isinstance(ast, Var):
        # Variable should be defined
        if ast.name not in env.vars:
            raise LoweringError(f"Undefined variable {ast.name}")
        return env.vars[ast.name]

    if isinstance(ast, ArrayAccess):
        # Name should be defined
        if ast.array not in env.vars:
            raise LoweringError(f"Undefined array {ast.array}")
        # Array
        base = env.vars[ast.array]
        # ArrayAccess is only valid on BIGINT variables.
        if base.type != Type.BIGINT:
            raise LoweringError(
                # TODO too strict? Do index arrays make sense?
                f"Can only use {Type.BIGINT} as arrays. Illegal attempt on {ast.array}"
            )
        # Index
        index = lower_expr(ast.index, env)
        if index.type != Type.INDEX:
            f"Array index type must be INDEX, got {index.type}"
        return IRArrayAccess(base, index, Type.BIGINT)

    if isinstance(ast, Add):
        return lower_binop("+", ast.left, ast.right, env)

    if isinstance(ast, Sub):
        return lower_binop("-", ast.left, ast.right, env)

    if isinstance(ast, Mul):
        return lower_binop("*", ast.left, ast.right, env)

    if isinstance(ast, Div):
        return lower_binop("/", ast.left, ast.right, env)

    if isinstance(ast, Power):
        base = lower_expr(ast.base, env)
        exponent = lower_expr(ast.exponent, env)
        assert isinstance(exponent, IRConst), "Only allow constant exponents?"
        assert base.type == Type.BIGINT, "Only allow bigints as base of powers?"
        return IRPower(base, exponent, base.type)

    if isinstance(ast, Neg):
        body = lower_expr(ast.body, env)
        if body.type != Type.INDEX:
            raise LoweringError(
                f"unary minus can only be used on expressions of type {Type.INDEX}"
                f", found {body.type}"
            )
        return IRBinOp("*", IRConst(-1, Type.INDEX), body, Type.INDEX)

    if isinstance(ast, ArrayAccess):
        raise NotImplementedError("Array access")

    if isinstance(ast, Reduction):
        return lower_reduction(ast, env)

    if isinstance(ast, Call):
        return lower_call(ast, env)

    raise NotImplementedError(f"lowering of {type(ast)}")


def lower_binop(op: str, lhs: Expr, rhs: Expr, env: Env) -> IRBinOp:
    left = lower_expr(lhs, env)
    right = lower_expr(rhs, env)

    if left.type == right.type:
        if op == "-" and left.type == Type.BIGINT:
            raise LoweringError("field subtraction not allowed")
        if op == "/" and left.type == Type.BIGINT:
            raise NotImplementedError("Field division? What do we do?")
        return IRBinOp(op, left, right, left.type)

    raise LoweringError(f"type mismatch on {op} operation")


def lower_reduction(ast: Reduction, env: Env) -> IRReduction:
    # Start, stop, step
    start = lower_expr(ast.start, env)
    stop = lower_expr(ast.stop, env)
    step = lower_expr(ast.step, env)
    for n in (start, stop, step):
        if n.type != Type.INDEX:
            raise LoweringError("Reduction bounds must be indices")

    # TODO: Shadowing
    if ast.var in env.vars:
        raise NotImplementedError(
            f"Reduction variable '{ast.var}' shadows an existing variable"
        )

    # TODO: is a copy necessary here?
    inner_env = Env(vars=dict(env.vars), signatures=dict(env.signatures))
    inner_env.vars[ast.var] = IRVar(ast.var, Type.INDEX)

    body = lower_expr(ast.body, inner_env)

    return IRReduction(
        ast.op,
        ast.var,
        start,
        stop,
        step,
        body,
        body.type,
    )


def lower_call(ast: Call, env: Env) -> IRCall:
    # Function must exist
    if ast.func not in env.signatures:
        raise LoweringError(f"call to undefined function '{ast.func}'")
    signature = env.signatures[ast.func]

    # Lower arguments
    args = [lower_expr(arg, env) for arg in ast.args]

    # Check number of arguments
    if len(args) != len(signature.params):
        raise LoweringError(
            f"function '{ast.func}' expects {len(signature.params)} args, "
            f"got {len(args)}"
        )

    # Check argument types
    for arg_node, param in zip(args, signature.params):
        if arg_node.type != param:
            raise LoweringError(
                f"Function '{ast.func}' argument type mismatch for parameter "
                f"'{param.name}': expected {param}, got {arg_node.type}"
            )

    return IRCall(function=signature.name, args=args, type=signature.return_type)


def lower_function(ast: Function, env: Env) -> IRFunction:
    # Assuming no globals
    params: list[IRVar] = []
    for name, ty in ast.params:
        if name in env.vars:
            raise LoweringError(f"duplicate parameter '{name}' in function {ast.name}")
        var = IRVar(name, ty)
        env.vars[name] = var
        params.append(var)
    # Lower body
    body = lower_expr(ast.body, env)
    # Typechecking
    if body.type != ast.return_type:
        raise LoweringError(
            f"function '{ast.name}' declared return type '{ast.return_type}' but body "
            f"has type '{body.type}'"
        )
    return IRFunction(ast.name, params, body, ast.return_type)


def lower_program(ast: Program) -> IRProgram:
    # Collect function signatures
    signatures: Dict[str, FunctionSignature] = {}
    for fn in ast.functions:
        if fn.name in signatures:
            raise LoweringError(f"duplicate function {fn.name}")
        param_types = [p[1] for p in fn.params]
        signatures[fn.name] = FunctionSignature(
            name=fn.name, params=param_types, return_type=fn.return_type
        )

    # Lower functions, each with a fresh environment!
    functions: List[IRFunction] = []
    for f in ast.functions:
        try:
            functions.append(
                lower_function(f, Env(vars={}, signatures=copy.deepcopy(signatures)))
            )
        except LoweringError as e:
            raise LoweringError(f"in '{f.name}': {e}") from e

    return IRProgram(functions)
