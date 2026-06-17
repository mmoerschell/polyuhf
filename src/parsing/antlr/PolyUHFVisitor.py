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


    # Visit a parse tree produced by PolyUHFParser#hash_function.
    def visitHash_function(self, ctx:PolyUHFParser.Hash_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#hash_params.
    def visitHash_params(self, ctx:PolyUHFParser.Hash_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#helper_function.
    def visitHelper_function(self, ctx:PolyUHFParser.Helper_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#param_group.
    def visitParam_group(self, ctx:PolyUHFParser.Param_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#helper_return_type.
    def visitHelper_return_type(self, ctx:PolyUHFParser.Helper_return_typeContext):
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


    # Visit a parse tree produced by PolyUHFParser#CtIfElseExpr.
    def visitCtIfElseExpr(self, ctx:PolyUHFParser.CtIfElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#NctIfExpr.
    def visitNctIfExpr(self, ctx:PolyUHFParser.NctIfExprContext):
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


    # Visit a parse tree produced by PolyUHFParser#SumReductionExpr.
    def visitSumReductionExpr(self, ctx:PolyUHFParser.SumReductionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#HornerReductionExpr.
    def visitHornerReductionExpr(self, ctx:PolyUHFParser.HornerReductionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#LeftFoldExpr.
    def visitLeftFoldExpr(self, ctx:PolyUHFParser.LeftFoldExprContext):
        return self.visitChildren(ctx)



del PolyUHFParser