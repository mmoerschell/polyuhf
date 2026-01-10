# Generated from PolyUHF.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,9,2,1,
        3,1,3,1,3,5,3,31,8,3,10,3,12,3,34,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,44,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,1,
        2,63,0,14,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,6,27,1,0,0,0,8,43,1,
        0,0,0,10,45,1,0,0,0,12,59,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,
        1,1,0,0,0,17,18,3,4,2,0,18,3,1,0,0,0,19,24,3,6,3,0,20,21,5,1,0,0,
        21,23,3,6,3,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,
        0,0,0,25,5,1,0,0,0,26,24,1,0,0,0,27,32,3,8,4,0,28,29,5,2,0,0,29,
        31,3,8,4,0,30,28,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,
        0,33,7,1,0,0,0,34,32,1,0,0,0,35,36,5,3,0,0,36,37,3,2,1,0,37,38,5,
        4,0,0,38,44,1,0,0,0,39,44,3,10,5,0,40,44,3,12,6,0,41,44,5,11,0,0,
        42,44,5,12,0,0,43,35,1,0,0,0,43,39,1,0,0,0,43,40,1,0,0,0,43,41,1,
        0,0,0,43,42,1,0,0,0,44,9,1,0,0,0,45,46,7,0,0,0,46,47,5,5,0,0,47,
        48,5,11,0,0,48,49,5,6,0,0,49,50,3,2,1,0,50,51,5,7,0,0,51,52,3,2,
        1,0,52,53,5,7,0,0,53,54,3,2,1,0,54,55,5,8,0,0,55,56,5,9,0,0,56,57,
        3,2,1,0,57,58,5,10,0,0,58,11,1,0,0,0,59,60,5,11,0,0,60,61,5,5,0,
        0,61,62,3,2,1,0,62,63,5,8,0,0,63,13,1,0,0,0,3,24,32,43
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'*'", "'('", "')'", "'['", "','", 
                     "':'", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VARIABLE", 
                      "INT", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_addExpr = 2
    RULE_mulExpr = 3
    RULE_primary = 4
    RULE_reduction = 5
    RULE_array = 6

    ruleNames =  [ "program", "expr", "addExpr", "mulExpr", "primary", "reduction", 
                   "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    VARIABLE=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def EOF(self):
            return self.getToken(PolyUHFParser.EOF, 0)

        def getRuleIndex(self):
            return PolyUHFParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PolyUHFParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expr()
            self.state = 15
            self.match(PolyUHFParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self):
            return self.getTypedRuleContext(PolyUHFParser.AddExprContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = PolyUHFParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.addExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_addExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.MulExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.MulExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)



    def addExpr(self):

        localctx = PolyUHFParser.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.AddContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.mulExpr()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 20
                self.match(PolyUHFParser.T__0)
                self.state = 21
                self.mulExpr()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_mulExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.PrimaryContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)



    def mulExpr(self):

        localctx = PolyUHFParser.MulExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.primary()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 28
                self.match(PolyUHFParser.T__1)
                self.state = 29
                self.primary()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(PolyUHFParser.ArrayContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class ReductionExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reduction(self):
            return self.getTypedRuleContext(PolyUHFParser.ReductionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReductionExpr" ):
                return visitor.visitReductionExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(PolyUHFParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PolyUHFParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesesContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = PolyUHFParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primary)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(PolyUHFParser.T__2)
                self.state = 36
                self.expr()
                self.state = 37
                self.match(PolyUHFParser.T__3)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.reduction()
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.array()
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.VariableExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.match(PolyUHFParser.VARIABLE)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(PolyUHFParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReductionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def VARIABLE(self):
            return self.getToken(PolyUHFParser.VARIABLE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.ExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.ExprContext,i)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_reduction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReduction" ):
                return visitor.visitReduction(self)
            else:
                return visitor.visitChildren(self)




    def reduction(self):

        localctx = PolyUHFParser.ReductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_reduction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 46
            self.match(PolyUHFParser.T__4)
            self.state = 47
            self.match(PolyUHFParser.VARIABLE)
            self.state = 48
            self.match(PolyUHFParser.T__5)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(PolyUHFParser.T__6)
            self.state = 51
            self.expr()
            self.state = 52
            self.match(PolyUHFParser.T__6)
            self.state = 53
            self.expr()
            self.state = 54
            self.match(PolyUHFParser.T__7)
            self.state = 55
            self.match(PolyUHFParser.T__8)
            self.state = 56
            self.expr()
            self.state = 57
            self.match(PolyUHFParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(PolyUHFParser.VARIABLE, 0)

        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = PolyUHFParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(PolyUHFParser.VARIABLE)
            self.state = 60
            self.match(PolyUHFParser.T__4)
            self.state = 61
            self.expr()
            self.state = 62
            self.match(PolyUHFParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





