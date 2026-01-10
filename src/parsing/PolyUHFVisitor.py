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


    # Visit a parse tree produced by PolyUHFParser#expr.
    def visitExpr(self, ctx:PolyUHFParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#Add.
    def visitAdd(self, ctx:PolyUHFParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#Mul.
    def visitMul(self, ctx:PolyUHFParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#Parentheses.
    def visitParentheses(self, ctx:PolyUHFParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#ReductionExpr.
    def visitReductionExpr(self, ctx:PolyUHFParser.ReductionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#ArrayExpr.
    def visitArrayExpr(self, ctx:PolyUHFParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#VariableExpr.
    def visitVariableExpr(self, ctx:PolyUHFParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#IntExpr.
    def visitIntExpr(self, ctx:PolyUHFParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#reduction.
    def visitReduction(self, ctx:PolyUHFParser.ReductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyUHFParser#array.
    def visitArray(self, ctx:PolyUHFParser.ArrayContext):
        return self.visitChildren(ctx)



del PolyUHFParser