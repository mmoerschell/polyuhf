import string

from parsing.ast.nodes import (
    Add,
    ArrayAccess,
    Div,
    Expr,
    Function,
    Int,
    Mul,
    Power,
    Program,
    Reduction,
    Sub,
    Var,
)

from .env import Env
from .nodes import (
    IRArrayAccess,
    IRBinOp,
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
        if not isinstance(base, IRVar):
            raise LoweringError(
                f"Cannot dereference anything else than variables. Found {type(base)}"
            )
        if base.type != Type.FIELD:
            raise LoweringError(
                # TODO too strict? Do index arrays make sense?
                f"Can only use FIELD as arrays. Illegal attempt on {ast.array}"
            )
        # Index
        index = lower_expr(ast.index, env)
        if index.type != Type.INDEX:
            f"Array index type must be INDEX, got {index.type}"
        return IRArrayAccess(base, index, Type.FIELD)

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
        assert base.type == Type.FIELD
        return IRPower(base, exponent, base.type)

    if isinstance(ast, ArrayAccess):
        raise NotImplementedError("Array access")

    if isinstance(ast, Reduction):
        return lower_reduction(ast, env)

    raise NotImplementedError(type(ast))


def lower_binop(op: str, lhs: Expr, rhs: Expr, env: Env) -> IRBinOp:
    left = lower_expr(lhs, env)
    right = lower_expr(rhs, env)

    if left.type == right.type:
        if op == "-" and left.type == Type.FIELD:
            raise LoweringError("field subtraction not allowed")
        if op == "/" and left.type == Type.FIELD:
            raise NotImplementedError("Field division? What do we do?")
        return IRBinOp(op, left, right, left.type)

    raise LoweringError("Type mismatch")


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
        raise NotImplementedError("Shadowing! What do we do?")

    # TODO: is a copy necessary here?
    inner_env = Env(vars=dict(env.vars))
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


def infer_param_type(name: str) -> Type:
    if name[0] in string.ascii_uppercase:
        return Type.FIELD
    else:
        return Type.INDEX


def lower_function(ast: Function) -> IRFunction:
    # Assuming no globals
    env = Env({})
    params = []
    for param_name in ast.params:
        if param_name in env.vars:
            raise LoweringError(
                f"Duplicate parameter '{param_name}' in function {ast.name}"
            )
        param_type = infer_param_type(param_name)
        node = IRVar(param_name, param_type)
        env.vars[param_name] = node
        params.append(node)
    body = lower_expr(ast.body, env)
    return IRFunction(ast.name, params, body, body.type)


def lower_program(ast: Program) -> IRProgram:
    # Assuming no globals
    functions = [lower_function(f) for f in ast.functions]
    return IRProgram(functions)
