from pprint import pprint
from parsing.ast.nodes import Add, Int, Mul, Var, Function
from parsing.PolyUHFParser import PolyUHFParser
from parsing.PolyUHFVisitor import PolyUHFVisitor


class ASTBuilder(PolyUHFVisitor):
    # Visit a parse tree produced by PolyUHFParser#program.
    def visitProgram(self, ctx: PolyUHFParser.ProgramContext):  # noqa: N802
        return [self.visit(f) for f in ctx.function()]

    # Visit a parse tree produced by PolyUHFParser#function.
    def visitFunction(self, ctx: PolyUHFParser.FunctionContext):  # noqa: N802
        identifiers = [ter.getText() for ter in ctx.IDENTIFIER()]
        expr = self.visit(ctx.expr())
        return Function(identifiers[0], identifiers[1:], expr)

    # Visit a parse tree produced by PolyUHFParser#expr.
    def visitExpr(self, ctx: PolyUHFParser.ExprContext):  # noqa: N802
        # TODO!
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PolyUHFParser#Add.
    def visitAdd(self, ctx: PolyUHFParser.AddContext):  # noqa: N802
        # left-associative fold
        nodes = [self.visit(child) for child in ctx.mulExpr()]
        if len(nodes) == 1:
            return nodes[0]
        node = nodes[0]
        for n in nodes[1:]:
            node = Add(node, n)
        return node

    # Visit a parse tree produced by PolyUHFParser#Mul.
    def visitMul(self, ctx: PolyUHFParser.MulContext):  # noqa: N802
        nodes = [self.visit(child) for child in ctx.primary()]
        if len(nodes) == 1:
            return nodes[0]
        node = nodes[0]
        for n in nodes[1:]:
            node = Mul(node, n)
        return node

    # Visit a parse tree produced by PolyUHFParser#Parentheses.
    def visitParentheses(self, ctx: PolyUHFParser.ParenthesesContext):  # noqa: N802
        return self.visit(ctx.expr())

    # Visit a parse tree produced by PolyUHFParser#ReductionExpr.
    def visitReductionExpr(self, ctx: PolyUHFParser.ReductionExprContext):  # noqa: N802
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PolyUHFParser#ArrayExpr.
    def visitArrayExpr(self, ctx: PolyUHFParser.ArrayExprContext):  # noqa: N802
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PolyUHFParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx: PolyUHFParser.IdentifierExpressionContext):  # noqa: N802
        return Var(ctx.IDENTIFIER().getText())

    # Visit a parse tree produced by PolyUHFParser#IntExpr.
    def visitIntExpr(self, ctx: PolyUHFParser.IntExprContext):  # noqa: N802
        return Int(int(ctx.INT().getText()))

    # Visit a parse tree produced by PolyUHFParser#reduction.
    def visitReduction(self, ctx: PolyUHFParser.ReductionContext):  # noqa: N802
        # TODO!
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PolyUHFParser#array.
    def visitArray(self, ctx: PolyUHFParser.ArrayContext):  # noqa: N802
        # TODO!
        return self.visitChildren(ctx)
