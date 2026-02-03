# Generated from PolyUHF.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PolyUHFParser import PolyUHFParser
else:
    from PolyUHFParser import PolyUHFParser

# This class defines a complete generic visitor for a parse tree produced by PolyUHFParser.

class PolyUHFVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolyUHFParser#program.
    def visitProgram(self, ctx:PolyUHFParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#function.
    def visitFunction(self, ctx:PolyUHFParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#type_annotation.
    def visitType_annotation(self, ctx:PolyUHFParser.Type_annotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#param_group.
    def visitParam_group(self, ctx:PolyUHFParser.Param_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#expr.
    def visitExpr(self, ctx:PolyUHFParser.ExprContext):
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


    # Visit a parse tree produced by PolyUHFParser#HexBigIntExpr.
    def visitHexBigIntExpr(self, ctx:PolyUHFParser.HexBigIntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#DecBigIntExpr.
    def visitDecBigIntExpr(self, ctx:PolyUHFParser.DecBigIntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#HexIntExpr.
    def visitHexIntExpr(self, ctx:PolyUHFParser.HexIntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#DecIntExpr.
    def visitDecIntExpr(self, ctx:PolyUHFParser.DecIntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#CallExpr.
    def visitCallExpr(self, ctx:PolyUHFParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#ArrayExpr.
    def visitArrayExpr(self, ctx:PolyUHFParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:PolyUHFParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#ReductionExpr.
    def visitReductionExpr(self, ctx:PolyUHFParser.ReductionExprContext):
        return self.visitChildren(ctx)



del PolyUHFParser