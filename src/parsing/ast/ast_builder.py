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
    ASTIfElse,
    ASTInt,
    ASTLocalIdentifier,
    ASTModule,
    ASTReduction,
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
        name = ctx.IDENTIFIER().getText()
        assert isinstance(name, str)
        param_groups = [self.visit(param_group) for param_group in ctx.param_group()]
        params: list[tuple[str, DSLType]] = list(chain.from_iterable(param_groups))
        return_type = self.visit(ctx.ttype())
        body = self.visit(ctx.expr())
        return ASTFunction(name, params, return_type, body)

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
        # Recall rule: base (^ exponent)?
        base = self.visit(ctx.primary())
        rhs = ctx.exponentExpr()
        if rhs is None:
            return base
        return ASTBinaryOperation(None, "^", base, self.visit(rhs))

    # Visit a parse tree produced by PolyUHFParser#Parentheses.
    def visitParentheses(self, ctx: PolyUHFParser.ParenthesesContext):  # noqa: N802
        # Remove parentheses
        return self.visit(ctx.expr())

    # Visit a parse tree produced by PolyUHFParser#IfElseExpr.
    def visitIfElseExpr(self, ctx: PolyUHFParser.IfElseExprContext):  # noqa: N802
        condition, then_branch, else_branch = [
            self.visit(ctx.expr(i)) for i in range(3)
        ]
        return ASTIfElse(None, condition, then_branch, else_branch)

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

    # Visit a parse tree produced by PolyUHFParser#ReductionExpr.
    def visitReductionExpr(self, ctx: PolyUHFParser.ReductionExprContext):  # noqa: N802
        op = ctx.op.text  # type: ignore
        var = ctx.IDENTIFIER().getText()
        expressions = ctx.expr()
        if len(expressions) != 4:
            raise DSLParseError("malformed reduction expression")
        start, stop, step, body = [self.visit(e) for e in expressions]
        bound = sp.simplify(
            sp.parse_expr(
                f"(({expressions[1].getText()})-({expressions[0].getText()}))/({expressions[2].getText()})"
            )
        )
        # print(f"Loop bound is {bound}")
        return ASTReduction(None, op, var, start, stop, step, body, bound)
