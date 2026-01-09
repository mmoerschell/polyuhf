# Generated from PolyUHF.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PolyUHFParser import PolyUHFParser
else:
    from PolyUHFParser import PolyUHFParser

# This class defines a complete generic visitor for a parse tree produced by PolyUHFParser.

class PolyUHFVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolyUHFParser#expr.
    def visitExpr(self, ctx:PolyUHFParser.ExprContext):
        return self.visitChildren(ctx)



del PolyUHFParser