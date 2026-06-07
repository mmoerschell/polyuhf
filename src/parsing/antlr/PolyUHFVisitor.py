# Generated from PolyUHF.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PolyUHFParser import PolyUHFParser
else:
    from PolyUHFParser import PolyUHFParser

# This class defines a complete generic visitor for a parse tree produced by PolyUHFParser.

class PolyUHFVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolyUHFParser#module.
    def visitModule(self, ctx:PolyUHFParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#function.
    def visitFunction(self, ctx:PolyUHFParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#param_group.
    def visitParam_group(self, ctx:PolyUHFParser.Param_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#ttype.
    def visitTtype(self, ctx:PolyUHFParser.TtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#expr.
    def visitExpr(self, ctx:PolyUHFParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#SingleCompare.
    def visitSingleCompare(self, ctx:PolyUHFParser.SingleCompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#compOp.
    def visitCompOp(self, ctx:PolyUHFParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#AddSub.
    def visitAddSub(self, ctx:PolyUHFParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#MulDiv.
    def visitMulDiv(self, ctx:PolyUHFParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:PolyUHFParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#UnaryAtom.
    def visitUnaryAtom(self, ctx:PolyUHFParser.UnaryAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#Exponent.
    def visitExponent(self, ctx:PolyUHFParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#Parentheses.
    def visitParentheses(self, ctx:PolyUHFParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#IfElseExpr.
    def visitIfElseExpr(self, ctx:PolyUHFParser.IfElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#HexadecimalExpression.
    def visitHexadecimalExpression(self, ctx:PolyUHFParser.HexadecimalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#DecimalExpr.
    def visitDecimalExpr(self, ctx:PolyUHFParser.DecimalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#CallExpr.
    def visitCallExpr(self, ctx:PolyUHFParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#BufferViewReadExpr.
    def visitBufferViewReadExpr(self, ctx:PolyUHFParser.BufferViewReadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:PolyUHFParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#ReductionExpr.
    def visitReductionExpr(self, ctx:PolyUHFParser.ReductionExprContext):
        return self.visitChildren(ctx)



del PolyUHFParser