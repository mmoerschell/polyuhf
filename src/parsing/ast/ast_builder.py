import re
from itertools import chain

import sympy as sp

from parsing.antlr.PolyUHFParser import PolyUHFParser
from parsing.antlr.PolyUHFVisitor import PolyUHFVisitor
from parsing.ast.ast_nodes import (
    ASTBinaryOperation,
    ASTBufferViewRead,
    ASTCall,
    ASTComparison,
    ASTFunction,
    ASTHornerReduction,
    ASTIfElse,
    ASTInt,
    ASTLeftFold,
    ASTLocalIdentifier,
    ASTModule,
    ASTSum,
    ASTUnaryMinus,
)
from settings import Settings
from typesystem import (
    Buffer,
    DSLType,
    Index,
)


class DSLParseError(SyntaxError):
    pass


class ASTBuilder(PolyUHFVisitor):
    settings: Settings

    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self.settings = settings

    # Visit a parse tree produced by PolyUHFParser#module.
    def visitModule(self, ctx: PolyUHFParser.ModuleContext):  # noqa: N802
        return ASTModule([self.visit(f) for f in ctx.function()])

    # Visit a parse tree produced by PolyUHFParser#function.
    def visitFunction(self, ctx: PolyUHFParser.FunctionContext):  # noqa: N802
        return self.visitChildren(ctx)

    def visitHash_function(self, ctx: PolyUHFParser.Hash_functionContext):  # noqa: N802
        name = ctx.IDENTIFIER().getText()
        assert isinstance(name, str)
        params = self.visit(ctx.hash_params())
        body = self.visit(ctx.expr())
        return ASTFunction(name, params, self.settings.field, body, True)

    def visitHash_params(self, ctx: PolyUHFParser.Hash_paramsContext):  # noqa: N802
        names = [tok.getText() for tok in ctx.IDENTIFIER()]
        return [
            (names[0], Buffer()),
            (names[1], Buffer()),
            (names[2], Index()),
        ]

    def visitHelper_function(  # noqa: N802
        self, ctx: PolyUHFParser.Helper_functionContext
    ):
        name = ctx.IDENTIFIER().getText()
        assert isinstance(name, str)
        param_groups = [self.visit(param_group) for param_group in ctx.param_group()]
        params: list[tuple[str, DSLType]] = list(chain.from_iterable(param_groups))
        return_type = self.visit(ctx.helper_return_type())
        body = self.visit(ctx.expr())
        return ASTFunction(name, params, return_type, body, False)

    # Visit a parse tree produced by PolyUHFParser#param_group.
    def visitParam_group(self, ctx: PolyUHFParser.Param_groupContext):  # noqa: N802
        # Collect all identifiers
        names = [tok.getText() for tok in ctx.IDENTIFIER()]
        # The last child is the type annotation
        ttype = self.visit(ctx.ttype())
        return [(name, ttype) for name in names]

    # Visit a parse tree produced by PolyUHFParser#ttype.
    def visitTtype(self, ctx: PolyUHFParser.TtypeContext):
        if ctx.BUFFER():
            return Buffer()
        elif ctx.FIELDELEMENT():
            return self.settings.field
        elif ctx.INDEX():
            return Index()
        else:
            raise NotImplementedError(ctx)

    def visitHelper_return_type(self, ctx: PolyUHFParser.Helper_return_typeContext):  # noqa: N802
        if ctx.FIELDELEMENT():
            return self.settings.field
        elif ctx.INDEX():
            return Index()
        else:
            raise NotImplementedError(ctx)

    # visitExpr omitted, base class handles default behavior

    # Visit a parse tree produced by PolyUHFParser#SingleCompare.
    def visitSingleCompare(self, ctx: PolyUHFParser.SingleCompareContext):  # noqa: N802
        left = self.visit(ctx.addSubExpr(0))
        # No compOp -> single expression
        if ctx.compOp() is None:
            return left
        op_token = ctx.compOp().start
        right = self.visit(ctx.addSubExpr(1))
        match op_token.type:
            case PolyUHFParser.EQ:
                return ASTComparison(None, "==", left, right)
            case PolyUHFParser.NEQ:
                return ASTComparison(None, "!=", left, right)
            case PolyUHFParser.LT:
                return ASTComparison(None, "<", left, right)
            case PolyUHFParser.LE:
                return ASTComparison(None, "<=", left, right)
            case PolyUHFParser.GT:
                return ASTComparison(None, ">", left, right)
            case PolyUHFParser.GE:
                return ASTComparison(None, ">=", left, right)
            case _:
                raise NotImplementedError()

    # visitCompOp omitted, handled in visitSingleCompare

    # Visit a parse tree produced by PolyUHFParser#AddSub.
    def visitAddSub(self, ctx: PolyUHFParser.AddSubContext):  # noqa: N802
        # left-associative fold
        nodes = [self.visit(child) for child in ctx.mulDivExpr()]
        if len(nodes) == 1:
            return nodes[0]
        node = nodes[0]
        for op_token, rhs in zip(ctx.op, nodes[1:], strict=True):
            if op_token.text in ["+", "-"]:
                node = ASTBinaryOperation(None, op_token.text, node, rhs)
            else:
                # CF reaches here -> grammar is broken
                raise RuntimeError(f"Invalid AddSub operator '{op_token.text}'")
        return node

    # Visit a parse tree produced by PolyUHFParser#MulDiv.
    def visitMulDiv(self, ctx: PolyUHFParser.MulDivContext):  # noqa: N802
        # left-associative fold
        nodes = [self.visit(child) for child in ctx.unaryMinusExpr()]
        if len(nodes) == 1:
            return nodes[0]
        node = nodes[0]
        for op_token, rhs in zip(ctx.op, nodes[1:], strict=True):
            if op_token.text in ["*", "/", "%"]:
                node = ASTBinaryOperation(None, op_token.text, node, rhs)
            else:
                # CF reaches here -> grammar is broken
                raise RuntimeError(f"Invalid MulDiv operator '{op_token.text}'")
        return node

    # Visit a parse tree produced by PolyUHFParser#UnaryMinus.
    def visitUnaryMinus(self, ctx: PolyUHFParser.UnaryMinusContext):  # noqa: N802
        payload = self.visit(ctx.unaryMinusExpr())
        return ASTUnaryMinus(None, payload)

    # visitUnaryAtom omitted, handled by base class

    # Visit a parse tree produced by PolyUHFParser#Exponent.
    def visitExponent(self, ctx: PolyUHFParser.ExponentContext):  # noqa: N802
        # Recall rule: base (** exponent)?
        base = self.visit(ctx.primary())
        rhs = ctx.exponentExpr()
        if rhs is None:
            return base
        return ASTBinaryOperation(None, "**", base, self.visit(rhs))

    # Visit a parse tree produced by PolyUHFParser#Parentheses.
    def visitParentheses(self, ctx: PolyUHFParser.ParenthesesContext):  # noqa: N802
        # Remove parentheses
        return self.visit(ctx.expr())

    # Visit a parse tree produced by PolyUHFParser#CtIfElseExpr.
    def visitCtIfElseExpr(self, ctx):  # noqa: N802
        condition, then_branch, else_branch = [
            self.visit(ctx.expr(i)) for i in range(3)
        ]
        return ASTIfElse(None, condition, then_branch, else_branch, True)

    # Visit a parse tree produced by PolyUHFParser#NctIfExpr.
    def visitNctIfExpr(self, ctx):  # noqa: N802
        expressions = ctx.expr()
        condition = self.visit(expressions[0])
        then_branch = self.visit(expressions[1])
        else_branch = self.visit(expressions[2]) if len(expressions) > 2 else None
        return ASTIfElse(None, condition, then_branch, else_branch, False)

    # Visit a parse tree produced by PolyUHFParser#HexadecimalExpression.
    def visitHexadecimalExpression(  # noqa: N802
        self, ctx: PolyUHFParser.HexadecimalExpressionContext
    ):
        ttype = self.visit(ctx.ttype()) if ctx.ttype() else None
        return ASTInt(ttype, int(ctx.HEXADECIMAL().getText(), 16))

    # Visit a parse tree produced by PolyUHFParser#DecimalExpr.
    def visitDecimalExpr(self, ctx: PolyUHFParser.DecimalExprContext):  # noqa: N802
        ttype = self.visit(ctx.ttype()) if ctx.ttype() else None
        return ASTInt(ttype, int(ctx.DECIMAL().getText()))

    # Visit a parse tree produced by PolyUHFParser#CallExpr.
    def visitCallExpr(self, ctx: PolyUHFParser.CallExprContext):  # noqa: N802
        function_name = ctx.IDENTIFIER().getText()
        args = [self.visit(child) for child in ctx.expr()]
        return ASTCall(None, function_name, args)

    # Visit a parse tree produced by PolyUHFParser#BufferViewReadExpr.
    def visitBufferViewReadExpr(self, ctx: PolyUHFParser.BufferViewReadExprContext):  # noqa: N802
        identifier = ctx.IDENTIFIER().getText()
        index = self.visit(ctx.expr())
        return ASTBufferViewRead(None, ASTLocalIdentifier(None, identifier), index)

    # Visit a parse tree produced by PolyUHFParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx: PolyUHFParser.IdentifierExpressionContext):  # noqa: N802
        return ASTLocalIdentifier(None, ctx.IDENTIFIER().getText())

    # Visit a parse tree produced by PolyUHFParser#SumReductionExpr.
    def visitSumReductionExpr(  # noqa: N802
        self, ctx: PolyUHFParser.SumReductionExprContext
    ):
        var = ctx.IDENTIFIER().getText()
        expressions = ctx.expr()
        if len(expressions) != 4:
            raise DSLParseError("malformed sum expression")
        start, stop, step, body = [self.visit(e) for e in expressions]
        bound_text = (
            f"(({expressions[1].getText()})-({expressions[0].getText()}))"
            f"/({expressions[2].getText()})"
        )
        symbols = {
            name: sp.Symbol(name)
            for name in set(re.findall(r"[A-Za-z][A-Za-z0-9_]*", bound_text))
        }
        bound = sp.simplify(
            sp.parse_expr(
                bound_text,
                local_dict=symbols,
            )
        )
        # print(f"Loop bound is {bound}")
        return ASTSum(None, var, start, stop, step, body, bound)

    # Visit a parse tree produced by PolyUHFParser#HornerReductionExpr.
    def visitHornerReductionExpr(  # noqa: N802
        self, ctx: PolyUHFParser.HornerReductionExprContext
    ):
        var = ctx.IDENTIFIER().getText()
        expressions = ctx.expr()
        if len(expressions) != 5:
            raise DSLParseError("malformed horner reduction expression")
        start, stop, step, r, body = [self.visit(e) for e in expressions]
        bound_text = (
            f"(({expressions[1].getText()})-({expressions[0].getText()}))"
            f"/({expressions[2].getText()})"
        )
        symbols = {
            name: sp.Symbol(name)
            for name in set(re.findall(r"[A-Za-z][A-Za-z0-9_]*", bound_text))
        }
        bound = sp.simplify(
            sp.parse_expr(
                bound_text,
                local_dict=symbols,
            )
        )
        return ASTHornerReduction(None, var, start, stop, step, r, body, bound)

    # Visit a parse tree produced by PolyUHFParser#LeftFoldExpr.
    def visitLeftFoldExpr(  # noqa: N802
        self, ctx: PolyUHFParser.LeftFoldExprContext
    ):
        identifiers = [tok.getText() for tok in ctx.IDENTIFIER()]
        if len(identifiers) != 2:
            raise DSLParseError("malformed foldl expression")
        var, acc_var = identifiers
        expressions = ctx.expr()
        if len(expressions) != 5:
            raise DSLParseError("malformed foldl expression")
        start, stop, step, init, body = [self.visit(e) for e in expressions]
        bound_text = (
            f"(({expressions[1].getText()})-({expressions[0].getText()}))"
            f"/({expressions[2].getText()})"
        )
        symbols = {
            name: sp.Symbol(name)
            for name in set(re.findall(r"[A-Za-z][A-Za-z0-9_]*", bound_text))
        }
        bound = sp.simplify(
            sp.parse_expr(
                bound_text,
                local_dict=symbols,
            )
        )
        return ASTLeftFold(None, var, start, stop, step, acc_var, init, body, bound)
