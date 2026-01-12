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
        4,1,14,82,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,26,8,1,
        10,1,12,1,29,9,1,3,1,31,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,
        5,3,42,8,3,10,3,12,3,45,9,3,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,
        9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,80,8,5,1,5,0,0,6,0,2,
        4,6,8,10,0,1,1,0,6,7,84,0,13,1,0,0,0,2,19,1,0,0,0,4,36,1,0,0,0,6,
        38,1,0,0,0,8,46,1,0,0,0,10,79,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,
        0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,
        5,0,0,1,18,1,1,0,0,0,19,20,5,1,0,0,20,21,5,12,0,0,21,30,5,2,0,0,
        22,27,5,12,0,0,23,24,5,3,0,0,24,26,5,12,0,0,25,23,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,
        30,22,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,5,4,0,0,33,34,5,
        5,0,0,34,35,3,4,2,0,35,3,1,0,0,0,36,37,3,6,3,0,37,5,1,0,0,0,38,43,
        3,8,4,0,39,40,5,6,0,0,40,42,3,8,4,0,41,39,1,0,0,0,42,45,1,0,0,0,
        43,41,1,0,0,0,43,44,1,0,0,0,44,7,1,0,0,0,45,43,1,0,0,0,46,51,3,10,
        5,0,47,48,5,7,0,0,48,50,3,10,5,0,49,47,1,0,0,0,50,53,1,0,0,0,51,
        49,1,0,0,0,51,52,1,0,0,0,52,9,1,0,0,0,53,51,1,0,0,0,54,55,5,2,0,
        0,55,56,3,4,2,0,56,57,5,4,0,0,57,80,1,0,0,0,58,80,5,13,0,0,59,80,
        5,12,0,0,60,61,5,12,0,0,61,62,5,8,0,0,62,63,3,4,2,0,63,64,5,9,0,
        0,64,80,1,0,0,0,65,66,7,0,0,0,66,67,5,8,0,0,67,68,5,12,0,0,68,69,
        5,3,0,0,69,70,3,4,2,0,70,71,5,5,0,0,71,72,3,4,2,0,72,73,5,5,0,0,
        73,74,3,4,2,0,74,75,5,9,0,0,75,76,5,10,0,0,76,77,3,4,2,0,77,78,5,
        11,0,0,78,80,1,0,0,0,79,54,1,0,0,0,79,58,1,0,0,0,79,59,1,0,0,0,79,
        60,1,0,0,0,79,65,1,0,0,0,80,11,1,0,0,0,6,15,27,30,43,51,79
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'('", "','", "')'", "':'", 
                     "'+'", "'*'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "INT", "WS" ]

    RULE_program = 0
    RULE_function = 1
    RULE_expr = 2
    RULE_addExpr = 3
    RULE_mulExpr = 4
    RULE_primary = 5

    ruleNames =  [ "program", "function", "expr", "addExpr", "mulExpr", 
                   "primary" ]

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
    IDENTIFIER=12
    INT=13
    WS=14

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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.function()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 17
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
            self.state = 19
            self.match(PolyUHFParser.T__0)
            self.state = 20
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 21
            self.match(PolyUHFParser.T__1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 22
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 23
                    self.match(PolyUHFParser.T__2)
                    self.state = 24
                    self.match(PolyUHFParser.IDENTIFIER)
                    self.state = 29
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 32
            self.match(PolyUHFParser.T__3)
            self.state = 33
            self.match(PolyUHFParser.T__4)
            self.state = 34
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
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
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
        self.enterRule(localctx, 6, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.AddContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.mulExpr()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 39
                self.match(PolyUHFParser.T__5)
                self.state = 40
                self.mulExpr()
                self.state = 45
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
        self.enterRule(localctx, 8, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.primary()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 47
                self.match(PolyUHFParser.T__6)
                self.state = 48
                self.primary()
                self.state = 53
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
        self.enterRule(localctx, 10, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(PolyUHFParser.T__1)
                self.state = 55
                self.expr()
                self.state = 56
                self.match(PolyUHFParser.T__3)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(PolyUHFParser.INT)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 61
                self.match(PolyUHFParser.T__7)
                self.state = 62
                self.expr()
                self.state = 63
                self.match(PolyUHFParser.T__8)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self.match(PolyUHFParser.T__7)
                self.state = 67
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 68
                self.match(PolyUHFParser.T__2)
                self.state = 69
                self.expr()
                self.state = 70
                self.match(PolyUHFParser.T__4)
                self.state = 71
                self.expr()
                self.state = 72
                self.match(PolyUHFParser.T__4)
                self.state = 73
                self.expr()
                self.state = 74
                self.match(PolyUHFParser.T__8)
                self.state = 75
                self.match(PolyUHFParser.T__9)
                self.state = 76
                self.expr()
                self.state = 77
                self.match(PolyUHFParser.T__10)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





