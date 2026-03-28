# pyright: standard

from itertools import chain
from typing import List, Tuple

from ir.types import ArrayType, BigIntType, IndexType, Type
from parsing.antlr.PolyUHFParser import PolyUHFParser
from parsing.antlr.PolyUHFVisitor import PolyUHFVisitor
from parsing.ast.ast_nodes import (
    Add,
    ArrayAccess,
    Call,
    Div,
    Function,
    IfElse,
    Int,
    Mul,
    Neg,
    Power,
    Program,
    Reduction,
    Sub,
    Var,
)


class DSLParseError(SyntaxError):
    pass


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
        annotation: str = ctx.TYPE_ANNOTATION().getText()
        if annotation == "index":
            return IndexType()
        elif annotation == "bigint":
            return BigIntType()
        elif annotation.startswith("["):
            close = annotation.index("]")
            size_part = annotation[1:close]
            elem_part = annotation[close + 1 :]
            size = int(size_part) if size_part else None
            if elem_part == "index":
                return ArrayType(size, IndexType())
            elif elem_part == "bigint":
                return ArrayType(size, BigIntType())
            else:
                raise DSLParseError(f"Unknown array element type '{annotation}'")
        else:
            raise DSLParseError(f"Unknown or missing type annotation '{annotation}'")

    # Visit a parse tree produced by PolyUHFParser#param_group.
    def visitParam_group(self, ctx: PolyUHFParser.Param_groupContext):  # noqa: N802
        # Collect all identifiers
        names = [tok.getText() for tok in ctx.IDENTIFIER()]
        # The last child is the type annotation
        ty = self.visit(ctx.type_annotation())
        return [(name, ty) for name in names]

    # visitExpr omitted, base class handles default behavior

    # Visit a parse tree produced by PolyUHFParser#AddSub.
    def visitAddSub(self, ctx: PolyUHFParser.AddSubContext):  # noqa: N802
        # left-associative fold
        nodes = [self.visit(child) for child in ctx.mulDivExpr()]
        if len(nodes) == 1:
            return nodes[0]
        node = nodes[0]
        for op_token, rhs in zip(ctx.op, nodes[1:], strict=True):
            if op_token.text == "+":
                node = Add(node, rhs)
            elif op_token.text == "-":
                node = Sub(node, rhs)
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
            if op_token.text == "*":
                node = Mul(node, rhs)
            elif op_token.text == "/":
                node = Div(node, rhs)
            else:
                # CF reaches here -> grammar is broken
                raise RuntimeError(f"Invalid MulDiv operator '{op_token.text}'")
        return node

    # Visit a parse tree produced by PolyUHFParser#UnaryMinus.
    def visitUnaryMinus(self, ctx: PolyUHFParser.UnaryMinusContext):  # noqa: N802
        payload = self.visit(ctx.unaryMinusExpr())
        return Neg(payload)

    # visitUnaryAtom omitted, handled by base class

    # Visit a parse tree produced by PolyUHFParser#Exponent.
    def visitExponent(self, ctx: PolyUHFParser.ExponentContext):  # noqa: N802
        # Recall rule: base (^ exponent)?
        base = self.visit(ctx.primary())
        rhs = ctx.exponentExpr()
        if rhs is None:
            return base
        return Power(base, self.visit(rhs))

    # Visit a parse tree produced by PolyUHFParser#Parentheses.
    def visitParentheses(self, ctx: PolyUHFParser.ParenthesesContext):  # noqa: N802
        # Remove parentheses
        return self.visit(ctx.expr())

    # Visit a parse tree produced by PolyUHFParser#IfElseExpr.
    def visitIfElseExpr(self, ctx: PolyUHFParser.IfElseExprContext):  # noqa: N802
        condition, then_branch, else_branch = [
            self.visit(ctx.expr(i)) for i in range(3)
        ]
        return IfElse(condition, then_branch, else_branch)

    # Visit a parse tree produced by PolyUHFParser#HexBigIntExpr.
    def visitHexBigIntExpr(self, ctx: PolyUHFParser.HexBigIntExprContext):  # noqa: N802
        payload = ctx.HEX_BIGINT().getText()[:-1]  # drop 'L'/'l', keep '0x'
        try:
            value = int(payload, 16)
            return Int(value, BigIntType())
        except ValueError as e:
            raise DSLParseError(f"invalid hex literal: '{payload}'") from e

    # Visit a parse tree produced by PolyUHFParser#DecBigIntExpr.
    def visitDecBigIntExpr(self, ctx: PolyUHFParser.DecBigIntExprContext):  # noqa: N802
        payload = ctx.DEC_BIGINT().getText()[:-1]  # drop 'L'/'l'
        value = int(payload, 10)
        return Int(value, BigIntType())

    # Visit a parse tree produced by PolyUHFParser#HexIntExpr.
    def visitHexIntExpr(self, ctx: PolyUHFParser.HexIntExprContext):  # noqa: N802
        payload = ctx.HEX_INT().getText()  # keep '0x'
        try:
            value = int(payload, 16)
            return Int(value, IndexType())
        except ValueError as e:
            raise DSLParseError(f"invalid hex literal: '{payload}'") from e

    # Visit a parse tree produced by PolyUHFParser#DecIntExpr.
    def visitDecIntExpr(self, ctx: PolyUHFParser.DecIntExprContext):  # noqa: N802
        payload = ctx.DEC_INT().getText()
        value = int(payload, 10)
        return Int(value, IndexType())

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
        expressions = ctx.expr()
        if len(expressions) != 4:
            raise DSLParseError("malformed reduction expression")
        start, stop, step, body = [self.visit(e) for e in expressions]
        return Reduction(op, var, start, stop, step, body)
