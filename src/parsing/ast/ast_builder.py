# pyright: standard

from itertools import chain
from typing import List, Tuple

from parsing.ast.nodes import (
    Add,
    ArrayAccess,
    Call,
    Div,
    Function,
    Int,
    Mul,
    Power,
    Program,
    Reduction,
    Sub,
    Var,
)
from parsing.ir.types import Type
from parsing.PolyUHFParser import PolyUHFParser
from parsing.PolyUHFVisitor import PolyUHFVisitor


class ASTBuilder(PolyUHFVisitor):
    # Visit a parse tree produced by PolyUHFParser#program.
    def visitProgram(self, ctx: PolyUHFParser.ProgramContext):  # noqa: N802
        return Program([self.visit(f) for f in ctx.function()])

    # Visit a parse tree produced by PolyUHFParser#function.
    def visitFunction(self, ctx: PolyUHFParser.FunctionContext):  # noqa: N802
        name = ctx.IDENTIFIER().getText()
        assert isinstance(name, str)
        param_groups = [self.visit(param_group) for param_group in ctx.param_group()]
        params: List[Tuple[str, Type]] = list(chain.from_iterable(param_groups))
        return_type = self.visit(ctx.type_annotation())
        body = self.visit(ctx.expr())
        return Function(name, params, return_type, body)

    # Visit a parse tree produced by PolyUHFParser#type_annotation.
    def visitType_annotation(self, ctx: PolyUHFParser.Type_annotationContext):  # noqa: N802
        token = ctx.getText()
        if token == "bigint":
            return Type.BIGINT
        elif token == "index":
            return Type.INDEX
        else:
            raise RuntimeError(f"Unknown or missing type annotation '{token}'")

    # Visit a parse tree produced by PolyUHFParser#param_group.
    def visitParam_group(self, ctx: PolyUHFParser.Param_groupContext):  # noqa: N802
        # Collect all identifiers
        names = [tok.getText() for tok in ctx.IDENTIFIER()]
        # The last child is the type annotation
        ty = self.visit(ctx.type_annotation())
        return [(name, ty) for name in names]

    # Visit a parse tree produced by PolyUHFParser#expr.
    def visitExpr(self, ctx: PolyUHFParser.ExprContext):  # noqa: N802
        # TODO remove?
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PolyUHFParser#AddSub.
    def visitAddSub(self, ctx: PolyUHFParser.AddSubContext):  # noqa: N802
        # left-associative fold
        nodes = [self.visit(child) for child in ctx.mulDivExpr()]
        if len(nodes) == 1:
            return nodes[0]
        node = nodes[0]
        for i, n in enumerate(nodes[1:]):
            op = ctx.getChild(2 * i + 1).getText()  # operator token: '+' or '-'
            if op == "+":
                node = Add(node, n)
            elif op == "-":
                node = Sub(node, n)
            else:
                raise RuntimeError(f"Invalid AddSub operator '{op}'")
        return node

    # Visit a parse tree produced by PolyUHFParser#MulDiv.
    def visitMulDiv(self, ctx: PolyUHFParser.MulDivContext):  # noqa: N802
        # left-associative fold
        nodes = [self.visit(child) for child in ctx.exponentExpr()]
        if len(nodes) == 1:
            return nodes[0]
        node = nodes[0]
        for i, n in enumerate(nodes[1:]):
            op = ctx.getChild(2 * i + 1).getText()  # '*' or '/'
            if op == "*":
                node = Mul(node, n)
            elif op == "/":
                node = Div(node, n)
            else:
                raise RuntimeError(f"Invalid MulDiv operator '{op}'")
        return node

    # Visit a parse tree produced by PolyUHFParser#Exponent.
    def visitExponent(self, ctx: PolyUHFParser.ExponentContext):  # noqa: N802
        # Recall rule: base (^ exponent)?
        base = self.visit(ctx.primary())
        if ctx.expr():
            exponent = self.visit(ctx.expr())
            return Power(base, exponent)
        return base

    # Visit a parse tree produced by PolyUHFParser#UnaryMinus.
    def visitUnaryMinus(self, ctx: PolyUHFParser.UnaryMinusContext):  # noqa: N802
        value = self.visit(ctx.primary())
        # Note: unary minus is represented as multiplication
        # by -1. This is only used for indices, not bigints.
        # Any C compiler will happily optimize it away.
        return Mul(Int(-1), value)

    # Visit a parse tree produced by PolyUHFParser#Parentheses.
    def visitParentheses(self, ctx: PolyUHFParser.ParenthesesContext):  # noqa: N802
        # Remove parentheses
        return self.visit(ctx.expr())

    # Visit a parse tree produced by PolyUHFParser#IntExpr.
    def visitIntExpr(self, ctx: PolyUHFParser.IntExprContext):  # noqa: N802
        return Int(int(ctx.INT().getText()))

    # Visit a parse tree produced by PolyUHFParser#CallExpr.
    def visitCallExpr(self, ctx: PolyUHFParser.CallExprContext):  # noqa: N802
        function_name = ctx.IDENTIFIER().getText()
        args = [self.visit(child) for child in ctx.expr()]
        return Call(function_name, args)

    # Visit a parse tree produced by PolyUHFParser#ArrayExpr.
    def visitArrayExpr(self, ctx: PolyUHFParser.ArrayExprContext):  # noqa: N802
        identifier = ctx.IDENTIFIER().getText()
        index = self.visit(ctx.expr())
        return ArrayAccess(identifier, index)

    # Visit a parse tree produced by PolyUHFParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx: PolyUHFParser.IdentifierExpressionContext):  # noqa: N802
        return Var(ctx.IDENTIFIER().getText())

    # Visit a parse tree produced by PolyUHFParser#ReductionExpr.
    def visitReductionExpr(self, ctx: PolyUHFParser.ReductionExprContext):  # noqa: N802
        # For bigints: '*' or '+'
        op = ctx.op.text  # type: ignore
        var = ctx.IDENTIFIER().getText()
        start, stop, step, body = [self.visit(e) for e in ctx.expr()]
        return Reduction(op, var, start, stop, step, body)
