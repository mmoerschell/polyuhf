import copy
import itertools
from dataclasses import dataclass

from parsing.ast.ast_nodes import (
    ASTBinaryOperation,
    ASTBufferViewRead,
    ASTCall,
    ASTComparison,
    ASTExpr,
    ASTFunction,
    ASTIfElse,
    ASTInt,
    ASTLocalIdentifier,
    ASTModule,
    ASTReduction,
)
from settings import Settings
from typesystem import Buffer, DSLType, Index


@dataclass
class TypeCheckingError(Exception):
    func: ASTFunction | None
    expr: ASTExpr
    expected: DSLType
    actual: DSLType

    def __str__(self) -> str:
        return (
            f"in {self.func.name + ', ' if self.func else ''}expression {self.expr}, "
            f"expected type {self.expected} but found {self.actual}"
        )


@dataclass(frozen=True)
class DSLFunctionSignature:
    name: str
    params: tuple[tuple[str, DSLType], ...]
    return_type: DSLType


@dataclass(frozen=True)
class Context:
    globals: dict[str, DSLFunctionSignature]
    locals: dict[str, DSLType]


class Typechecker:
    settings: Settings

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def typecheck_module(self, module: ASTModule) -> dict[str, DSLFunctionSignature]:
        if any(
            f1.name == f2.name
            for (f1, f2) in itertools.combinations(module.functions, 2)
        ):
            raise ValueError("Duplicate function names.")
        function_signatures = {
            f.name: DSLFunctionSignature(f.name, tuple(f.params), f.return_type)
            for f in module.functions
        }
        for func in module.functions:
            ctx = Context(function_signatures, {})
            for name, ttype in func.params:
                ctx.locals[name] = ttype
            actual = self._typecheck_expr(func.body, ctx)
            if actual != func.return_type:
                raise TypeCheckingError(func, func.body, func.return_type, actual)
        return function_signatures

    def _typecheck_expr(self, expr: ASTExpr, ctx: Context) -> DSLType:  # noqa: C901
        match expr:
            case ASTInt():
                expr.ttype = (
                    expr.ttype or Index()
                )  # default if not explicitly annotated
            case ASTLocalIdentifier(_, name):
                if name not in ctx.locals:
                    raise ValueError(f"unknown local identifier '{name}'")
                expr.ttype = ctx.locals[name]
            case ASTBinaryOperation(_, operator, left, right):
                ltype = self._typecheck_expr(left, ctx)
                rtype = self._typecheck_expr(right, ctx)
                match operator:
                    case "+" | "-" | "*" | "/" | "%":
                        if rtype != ltype or not ltype:
                            raise TypeCheckingError(None, right, ltype, rtype)
                    case "^":
                        if rtype != Index() or not ltype:
                            raise TypeCheckingError(None, right, Index(), rtype)
                expr.ttype = ltype
            case ASTComparison(_, operator, left, right):
                ltype = self._typecheck_expr(left, ctx)
                rtype = self._typecheck_expr(right, ctx)
                if rtype != ltype or not ltype:
                    raise TypeCheckingError(None, right, ltype, rtype)
                expr.ttype = Index()
            case ASTIfElse(_, condition, then_branch, else_branch):
                cond_type = self._typecheck_expr(condition, ctx)
                if cond_type != Index():
                    raise TypeCheckingError(None, condition, Index(), cond_type)
                then_type = self._typecheck_expr(then_branch, ctx)
                else_type = self._typecheck_expr(else_branch, ctx)
                if else_type != then_type:
                    raise TypeCheckingError(None, else_branch, then_type, else_type)
                expr.ttype = then_type
            case ASTCall(_, func_name, args):
                # Function must exist
                if func_name not in ctx.globals:
                    raise ValueError(f"Call to undefined function {func_name}")
                signature = ctx.globals[func_name]
                # Check number of arguments
                if len(args) != len(signature.params):
                    raise ValueError(
                        f"function '{func_name}' expects {len(signature.params)} parameters"
                        f", but {len(args)} were given."
                    )
                # Check argument types
                for arg, param in zip(args, signature.params, strict=True):
                    arg_type = self._typecheck_expr(arg, ctx)
                    if arg_type != param[1]:
                        raise ValueError(
                            f"In call to '{func_name}', argument type mismatch for "
                            f"parameter '{param[0]}': expected {param[1]}, "
                            f"got {arg_type}"
                        )
                expr.ttype = signature.return_type
            case ASTBufferViewRead(_, buffer, index):
                btype = self._typecheck_expr(buffer, ctx)
                if not isinstance(btype, Buffer):
                    raise ValueError(f"can only index into buffers, found {btype}")
                index_type = self._typecheck_expr(index, ctx)
                if index_type != Index():
                    raise TypeCheckingError(None, index, Index(), index_type)
                expr.ttype = self.settings.field
            case ASTReduction(_, _, var, start, stop, step, body):
                for expr_ in [start, stop, step]:
                    ttype = self._typecheck_expr(expr_, ctx)
                    if ttype != Index():
                        raise TypeCheckingError(None, expr_, Index(), ttype)
                ctx_ = copy.copy(ctx)
                ctx_.locals[var] = Index()  # Shadowing
                expr.ttype = self._typecheck_expr(body, ctx_)
            case _:
                raise NotImplementedError(f"{expr!r}")
        assert expr.ttype
        return expr.ttype
