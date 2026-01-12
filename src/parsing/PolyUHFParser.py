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
        4,1,14,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,3,1,35,8,1,1,1,1,1,1,1,1,1,1,2,
        1,2,1,3,1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,4,1,4,1,4,5,4,54,8,
        4,10,4,12,4,57,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,67,8,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,1,0,6,7,88,0,17,1,0,0,
        0,2,23,1,0,0,0,4,40,1,0,0,0,6,42,1,0,0,0,8,50,1,0,0,0,10,66,1,0,
        0,0,12,68,1,0,0,0,14,82,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,
        1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,
        22,1,1,0,0,0,23,24,5,1,0,0,24,25,5,12,0,0,25,34,5,2,0,0,26,31,5,
        12,0,0,27,28,5,3,0,0,28,30,5,12,0,0,29,27,1,0,0,0,30,33,1,0,0,0,
        31,29,1,0,0,0,31,32,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,34,26,1,
        0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,5,4,0,0,37,38,5,5,0,0,38,
        39,3,4,2,0,39,3,1,0,0,0,40,41,3,6,3,0,41,5,1,0,0,0,42,47,3,8,4,0,
        43,44,5,6,0,0,44,46,3,8,4,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,
        0,0,0,47,48,1,0,0,0,48,7,1,0,0,0,49,47,1,0,0,0,50,55,3,10,5,0,51,
        52,5,7,0,0,52,54,3,10,5,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,
        0,0,55,56,1,0,0,0,56,9,1,0,0,0,57,55,1,0,0,0,58,59,5,2,0,0,59,60,
        3,4,2,0,60,61,5,4,0,0,61,67,1,0,0,0,62,67,3,12,6,0,63,67,3,14,7,
        0,64,67,5,12,0,0,65,67,5,13,0,0,66,58,1,0,0,0,66,62,1,0,0,0,66,63,
        1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,11,1,0,0,0,68,69,7,0,0,0,
        69,70,5,8,0,0,70,71,5,12,0,0,71,72,5,3,0,0,72,73,3,4,2,0,73,74,5,
        5,0,0,74,75,3,4,2,0,75,76,5,5,0,0,76,77,3,4,2,0,77,78,5,9,0,0,78,
        79,5,10,0,0,79,80,3,4,2,0,80,81,5,11,0,0,81,13,1,0,0,0,82,83,5,12,
        0,0,83,84,5,8,0,0,84,85,3,4,2,0,85,86,5,9,0,0,86,15,1,0,0,0,6,19,
        31,34,47,55,66
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
    RULE_reduction = 6
    RULE_array = 7

    ruleNames =  [ "program", "function", "expr", "addExpr", "mulExpr", 
                   "primary", "reduction", "array" ]

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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.function()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 21
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
            self.state = 23
            self.match(PolyUHFParser.T__0)
            self.state = 24
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 25
            self.match(PolyUHFParser.T__1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 26
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 27
                    self.match(PolyUHFParser.T__2)
                    self.state = 28
                    self.match(PolyUHFParser.IDENTIFIER)
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 36
            self.match(PolyUHFParser.T__3)
            self.state = 37
            self.match(PolyUHFParser.T__4)
            self.state = 38
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
            self.state = 40
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
            self.state = 42
            self.mulExpr()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 43
                self.match(PolyUHFParser.T__5)
                self.state = 44
                self.mulExpr()
                self.state = 49
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
            self.state = 50
            self.primary()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 51
                self.match(PolyUHFParser.T__6)
                self.state = 52
                self.primary()
                self.state = 57
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
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(PolyUHFParser.T__1)
                self.state = 59
                self.expr()
                self.state = 60
                self.match(PolyUHFParser.T__3)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.reduction()
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.array()
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 65
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

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 12, self.RULE_reduction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self.match(PolyUHFParser.T__7)
            self.state = 70
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 71
            self.match(PolyUHFParser.T__2)
            self.state = 72
            self.expr()
            self.state = 73
            self.match(PolyUHFParser.T__4)
            self.state = 74
            self.expr()
            self.state = 75
            self.match(PolyUHFParser.T__4)
            self.state = 76
            self.expr()
            self.state = 77
            self.match(PolyUHFParser.T__8)
            self.state = 78
            self.match(PolyUHFParser.T__9)
            self.state = 79
            self.expr()
            self.state = 80
            self.match(PolyUHFParser.T__10)
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

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 83
            self.match(PolyUHFParser.T__7)
            self.state = 84
            self.expr()
            self.state = 85
            self.match(PolyUHFParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





