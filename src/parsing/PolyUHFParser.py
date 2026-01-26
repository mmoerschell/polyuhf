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
        4,1,19,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,28,8,1,10,1,12,1,31,9,1,3,1,33,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,
        1,3,1,3,5,3,44,8,3,10,3,12,3,47,9,3,1,4,1,4,1,4,5,4,52,8,4,10,4,
        12,4,55,9,4,1,5,1,5,1,5,3,5,60,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,89,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,1,0,5,6,1,
        0,7,8,2,0,5,5,7,7,94,0,15,1,0,0,0,2,21,1,0,0,0,4,38,1,0,0,0,6,40,
        1,0,0,0,8,48,1,0,0,0,10,56,1,0,0,0,12,88,1,0,0,0,14,16,3,2,1,0,15,
        14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,
        0,19,20,5,0,0,1,20,1,1,0,0,0,21,22,5,14,0,0,22,23,5,15,0,0,23,32,
        5,1,0,0,24,29,5,15,0,0,25,26,5,2,0,0,26,28,5,15,0,0,27,25,1,0,0,
        0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,33,1,0,0,0,31,29,
        1,0,0,0,32,24,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,5,3,0,0,
        35,36,5,4,0,0,36,37,3,4,2,0,37,3,1,0,0,0,38,39,3,6,3,0,39,5,1,0,
        0,0,40,45,3,8,4,0,41,42,7,0,0,0,42,44,3,8,4,0,43,41,1,0,0,0,44,47,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,45,1,0,0,0,48,
        53,3,10,5,0,49,50,7,1,0,0,50,52,3,10,5,0,51,49,1,0,0,0,52,55,1,0,
        0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,9,1,0,0,0,55,53,1,0,0,0,56,59,
        3,12,6,0,57,58,5,9,0,0,58,60,3,4,2,0,59,57,1,0,0,0,59,60,1,0,0,0,
        60,11,1,0,0,0,61,62,5,6,0,0,62,89,3,12,6,0,63,64,5,1,0,0,64,65,3,
        4,2,0,65,66,5,3,0,0,66,89,1,0,0,0,67,89,5,16,0,0,68,89,5,15,0,0,
        69,70,5,15,0,0,70,71,5,10,0,0,71,72,3,4,2,0,72,73,5,11,0,0,73,89,
        1,0,0,0,74,75,7,2,0,0,75,76,5,10,0,0,76,77,5,15,0,0,77,78,5,2,0,
        0,78,79,3,4,2,0,79,80,5,4,0,0,80,81,3,4,2,0,81,82,5,4,0,0,82,83,
        3,4,2,0,83,84,5,11,0,0,84,85,5,12,0,0,85,86,3,4,2,0,86,87,5,13,0,
        0,87,89,1,0,0,0,88,61,1,0,0,0,88,63,1,0,0,0,88,67,1,0,0,0,88,68,
        1,0,0,0,88,69,1,0,0,0,88,74,1,0,0,0,89,13,1,0,0,0,7,17,29,32,45,
        53,59,88
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'+'", "'-'", 
                     "'*'", "'/'", "'^'", "'['", "']'", "'{'", "'}'", "'function'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNCTION", "IDENTIFIER", 
                      "INT", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_expr = 2
    RULE_addSubExpr = 3
    RULE_mulDivExpr = 4
    RULE_exponentExpr = 5
    RULE_primary = 6

    ruleNames =  [ "program", "function", "expr", "addSubExpr", "mulDivExpr", 
                   "exponentExpr", "primary" ]

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
    T__10=11
    T__11=12
    T__12=13
    FUNCTION=14
    IDENTIFIER=15
    INT=16
    WS=17
    LINE_COMMENT=18
    BLOCK_COMMENT=19

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

        def EOF(self):
            return self.getToken(PolyUHFParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.FunctionContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.FunctionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.function()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 19
            self.match(PolyUHFParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PolyUHFParser.FUNCTION, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PolyUHFParser.IDENTIFIER)
            else:
                return self.getToken(PolyUHFParser.IDENTIFIER, i)

        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = PolyUHFParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(PolyUHFParser.FUNCTION)
            self.state = 22
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 23
            self.match(PolyUHFParser.T__0)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 24
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 25
                    self.match(PolyUHFParser.T__1)
                    self.state = 26
                    self.match(PolyUHFParser.IDENTIFIER)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 34
            self.match(PolyUHFParser.T__2)
            self.state = 35
            self.match(PolyUHFParser.T__3)
            self.state = 36
            self.expr()
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

        def addSubExpr(self):
            return self.getTypedRuleContext(PolyUHFParser.AddSubExprContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = PolyUHFParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.addSubExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddSubExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_addSubExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddSubContext(AddSubExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.AddSubExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulDivExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.MulDivExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.MulDivExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)



    def addSubExpr(self):

        localctx = PolyUHFParser.AddSubExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_addSubExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.AddSubContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.mulDivExpr()
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 41
                    _la = self._input.LA(1)
                    if not(_la==5 or _la==6):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 42
                    self.mulDivExpr() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulDivExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_mulDivExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulDivContext(MulDivExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.MulDivExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exponentExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.ExponentExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.ExponentExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def mulDivExpr(self):

        localctx = PolyUHFParser.MulDivExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mulDivExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulDivContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.exponentExpr()
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 50
                    self.exponentExpr() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_exponentExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExponentContext(ExponentExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.ExponentExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(PolyUHFParser.PrimaryContext,0)

        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)



    def exponentExpr(self):

        localctx = PolyUHFParser.ExponentExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exponentExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.ExponentContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.primary()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 57
                self.match(PolyUHFParser.T__8)
                self.state = 58
                self.expr()


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

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class ReductionExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.ExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReductionExpr" ):
                return visitor.visitReductionExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(PolyUHFParser.PrimaryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
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


    class IdentifierExpressionContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = PolyUHFParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(PolyUHFParser.T__5)
                self.state = 62
                self.primary()
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(PolyUHFParser.T__0)
                self.state = 64
                self.expr()
                self.state = 65
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(PolyUHFParser.INT)
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 70
                self.match(PolyUHFParser.T__9)
                self.state = 71
                self.expr()
                self.state = 72
                self.match(PolyUHFParser.T__10)
                pass

            elif la_ == 6:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==5 or _la==7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75
                self.match(PolyUHFParser.T__9)
                self.state = 76
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 77
                self.match(PolyUHFParser.T__1)
                self.state = 78
                self.expr()
                self.state = 79
                self.match(PolyUHFParser.T__3)
                self.state = 80
                self.expr()
                self.state = 81
                self.match(PolyUHFParser.T__3)
                self.state = 82
                self.expr()
                self.state = 83
                self.match(PolyUHFParser.T__10)
                self.state = 84
                self.match(PolyUHFParser.T__11)
                self.state = 85
                self.expr()
                self.state = 86
                self.match(PolyUHFParser.T__12)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





