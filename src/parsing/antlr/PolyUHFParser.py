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
        4,1,33,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,
        9,1,3,1,43,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,56,
        8,3,10,3,12,3,59,9,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,3,5,69,8,5,
        1,6,1,6,1,7,1,7,1,7,5,7,76,8,7,10,7,12,7,79,9,7,1,8,1,8,1,8,5,8,
        84,8,8,10,8,12,8,87,9,8,1,9,1,9,1,9,3,9,92,8,9,1,10,1,10,1,10,3,
        10,97,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        122,8,11,10,11,12,11,125,9,11,3,11,127,8,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,150,8,11,1,11,0,0,12,0,2,4,6,8,10,12,14,
        16,18,20,22,0,4,1,0,20,25,1,0,6,7,1,0,8,9,2,0,6,6,8,8,159,0,25,1,
        0,0,0,2,31,1,0,0,0,4,50,1,0,0,0,6,52,1,0,0,0,8,62,1,0,0,0,10,64,
        1,0,0,0,12,70,1,0,0,0,14,72,1,0,0,0,16,80,1,0,0,0,18,91,1,0,0,0,
        20,93,1,0,0,0,22,149,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,
        0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,
        1,1,0,0,0,31,32,5,14,0,0,32,33,5,30,0,0,33,42,5,1,0,0,34,39,3,6,
        3,0,35,36,5,2,0,0,36,38,3,6,3,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,
        1,0,0,0,39,40,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,42,34,1,0,0,0,
        42,43,1,0,0,0,43,44,1,0,0,0,44,45,5,3,0,0,45,46,3,4,2,0,46,47,5,
        4,0,0,47,48,3,8,4,0,48,49,5,5,0,0,49,3,1,0,0,0,50,51,5,17,0,0,51,
        5,1,0,0,0,52,57,5,30,0,0,53,54,5,2,0,0,54,56,5,30,0,0,55,53,1,0,
        0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,
        1,0,0,0,60,61,3,4,2,0,61,7,1,0,0,0,62,63,3,10,5,0,63,9,1,0,0,0,64,
        68,3,14,7,0,65,66,3,12,6,0,66,67,3,14,7,0,67,69,1,0,0,0,68,65,1,
        0,0,0,68,69,1,0,0,0,69,11,1,0,0,0,70,71,7,0,0,0,71,13,1,0,0,0,72,
        77,3,16,8,0,73,74,7,1,0,0,74,76,3,16,8,0,75,73,1,0,0,0,76,79,1,0,
        0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,15,1,0,0,0,79,77,1,0,0,0,80,85,
        3,18,9,0,81,82,7,2,0,0,82,84,3,18,9,0,83,81,1,0,0,0,84,87,1,0,0,
        0,85,83,1,0,0,0,85,86,1,0,0,0,86,17,1,0,0,0,87,85,1,0,0,0,88,89,
        5,7,0,0,89,92,3,18,9,0,90,92,3,20,10,0,91,88,1,0,0,0,91,90,1,0,0,
        0,92,19,1,0,0,0,93,96,3,22,11,0,94,95,5,10,0,0,95,97,3,20,10,0,96,
        94,1,0,0,0,96,97,1,0,0,0,97,21,1,0,0,0,98,99,5,1,0,0,99,100,3,8,
        4,0,100,101,5,3,0,0,101,150,1,0,0,0,102,103,5,15,0,0,103,104,3,8,
        4,0,104,105,5,4,0,0,105,106,3,8,4,0,106,107,5,5,0,0,107,108,5,16,
        0,0,108,109,5,4,0,0,109,110,3,8,4,0,110,111,5,5,0,0,111,150,1,0,
        0,0,112,150,5,26,0,0,113,150,5,27,0,0,114,150,5,28,0,0,115,150,5,
        29,0,0,116,117,5,30,0,0,117,126,5,1,0,0,118,123,3,8,4,0,119,120,
        5,2,0,0,120,122,3,8,4,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,126,118,
        1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,150,5,3,0,0,129,130,
        5,30,0,0,130,131,5,11,0,0,131,132,3,8,4,0,132,133,5,12,0,0,133,150,
        1,0,0,0,134,150,5,30,0,0,135,136,7,3,0,0,136,137,5,11,0,0,137,138,
        5,30,0,0,138,139,5,2,0,0,139,140,3,8,4,0,140,141,5,13,0,0,141,142,
        3,8,4,0,142,143,5,13,0,0,143,144,3,8,4,0,144,145,5,12,0,0,145,146,
        5,4,0,0,146,147,3,8,4,0,147,148,5,5,0,0,148,150,1,0,0,0,149,98,1,
        0,0,0,149,102,1,0,0,0,149,112,1,0,0,0,149,113,1,0,0,0,149,114,1,
        0,0,0,149,115,1,0,0,0,149,116,1,0,0,0,149,129,1,0,0,0,149,134,1,
        0,0,0,149,135,1,0,0,0,150,23,1,0,0,0,12,27,39,42,57,68,77,85,91,
        96,123,126,149
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "'+'", 
                     "'-'", "'*'", "'/'", "'^'", "'['", "']'", "':'", "'func'", 
                     "'if'", "'else'", "<INVALID>", "'bigint'", "'index'", 
                     "'=='", "'!='", "'<='", "'>='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNCTION", "IF", "ELSE", 
                      "TYPE_ANNOTATION", "TYPE_BIGINT", "TYPE_INDEX", "EQ", 
                      "NEQ", "LE", "GE", "LT", "GT", "HEX_BIGINT", "DEC_BIGINT", 
                      "HEX_INT", "DEC_INT", "IDENTIFIER", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_type_annotation = 2
    RULE_param_group = 3
    RULE_expr = 4
    RULE_comparisonExpr = 5
    RULE_compOp = 6
    RULE_addSubExpr = 7
    RULE_mulDivExpr = 8
    RULE_unaryMinusExpr = 9
    RULE_exponentExpr = 10
    RULE_primary = 11

    ruleNames =  [ "program", "function", "type_annotation", "param_group", 
                   "expr", "comparisonExpr", "compOp", "addSubExpr", "mulDivExpr", 
                   "unaryMinusExpr", "exponentExpr", "primary" ]

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
    IF=15
    ELSE=16
    TYPE_ANNOTATION=17
    TYPE_BIGINT=18
    TYPE_INDEX=19
    EQ=20
    NEQ=21
    LE=22
    GE=23
    LT=24
    GT=25
    HEX_BIGINT=26
    DEC_BIGINT=27
    HEX_INT=28
    DEC_INT=29
    IDENTIFIER=30
    WS=31
    LINE_COMMENT=32
    BLOCK_COMMENT=33

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.function()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 29
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

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)

        def type_annotation(self):
            return self.getTypedRuleContext(PolyUHFParser.Type_annotationContext,0)


        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def param_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.Param_groupContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.Param_groupContext,i)


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
            self.state = 31
            self.match(PolyUHFParser.FUNCTION)
            self.state = 32
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 33
            self.match(PolyUHFParser.T__0)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 34
                self.param_group()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 35
                    self.match(PolyUHFParser.T__1)
                    self.state = 36
                    self.param_group()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 44
            self.match(PolyUHFParser.T__2)
            self.state = 45
            self.type_annotation()
            self.state = 46
            self.match(PolyUHFParser.T__3)
            self.state = 47
            self.expr()
            self.state = 48
            self.match(PolyUHFParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_annotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_ANNOTATION(self):
            return self.getToken(PolyUHFParser.TYPE_ANNOTATION, 0)

        def getRuleIndex(self):
            return PolyUHFParser.RULE_type_annotation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_annotation" ):
                return visitor.visitType_annotation(self)
            else:
                return visitor.visitChildren(self)




    def type_annotation(self):

        localctx = PolyUHFParser.Type_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(PolyUHFParser.TYPE_ANNOTATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PolyUHFParser.IDENTIFIER)
            else:
                return self.getToken(PolyUHFParser.IDENTIFIER, i)

        def type_annotation(self):
            return self.getTypedRuleContext(PolyUHFParser.Type_annotationContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_param_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_group" ):
                return visitor.visitParam_group(self)
            else:
                return visitor.visitChildren(self)




    def param_group(self):

        localctx = PolyUHFParser.Param_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 53
                self.match(PolyUHFParser.T__1)
                self.state = 54
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.type_annotation()
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

        def comparisonExpr(self):
            return self.getTypedRuleContext(PolyUHFParser.ComparisonExprContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = PolyUHFParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.comparisonExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_comparisonExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleCompareContext(ComparisonExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.ComparisonExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addSubExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.AddSubExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.AddSubExprContext,i)

        def compOp(self):
            return self.getTypedRuleContext(PolyUHFParser.CompOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleCompare" ):
                return visitor.visitSingleCompare(self)
            else:
                return visitor.visitChildren(self)



    def comparisonExpr(self):

        localctx = PolyUHFParser.ComparisonExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.SingleCompareContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.addSubExpr()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0):
                self.state = 65
                self.compOp()
                self.state = 66
                self.addSubExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(PolyUHFParser.EQ, 0)

        def NEQ(self):
            return self.getToken(PolyUHFParser.NEQ, 0)

        def LE(self):
            return self.getToken(PolyUHFParser.LE, 0)

        def GE(self):
            return self.getToken(PolyUHFParser.GE, 0)

        def LT(self):
            return self.getToken(PolyUHFParser.LT, 0)

        def GT(self):
            return self.getToken(PolyUHFParser.GT, 0)

        def getRuleIndex(self):
            return PolyUHFParser.RULE_compOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = PolyUHFParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            self.s6 = None # Token
            self.op = list() # of Tokens
            self.s7 = None # Token
            self._tset146 = None # Token
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
        self.enterRule(localctx, 14, self.RULE_addSubExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.AddSubContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.mulDivExpr()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 73
                localctx._tset146 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx._tset146 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset146)
                self.state = 74
                self.mulDivExpr()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.s8 = None # Token
            self.op = list() # of Tokens
            self.s9 = None # Token
            self._tset177 = None # Token
            self.copyFrom(ctx)

        def unaryMinusExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.UnaryMinusExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.UnaryMinusExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def mulDivExpr(self):

        localctx = PolyUHFParser.MulDivExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mulDivExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulDivContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.unaryMinusExpr()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 81
                localctx._tset177 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    localctx._tset177 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset177)
                self.state = 82
                self.unaryMinusExpr()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryMinusExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_unaryMinusExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UnaryAtomContext(UnaryMinusExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.UnaryMinusExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exponentExpr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExponentExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryAtom" ):
                return visitor.visitUnaryAtom(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(UnaryMinusExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.UnaryMinusExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryMinusExpr(self):
            return self.getTypedRuleContext(PolyUHFParser.UnaryMinusExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)



    def unaryMinusExpr(self):

        localctx = PolyUHFParser.UnaryMinusExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unaryMinusExpr)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PolyUHFParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(PolyUHFParser.T__6)
                self.state = 89
                self.unaryMinusExpr()
                pass
            elif token in [1, 6, 8, 15, 26, 27, 28, 29, 30]:
                localctx = PolyUHFParser.UnaryAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.exponentExpr()
                pass
            else:
                raise NoViableAltException(self)

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

        def exponentExpr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExponentExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)



    def exponentExpr(self):

        localctx = PolyUHFParser.ExponentExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exponentExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.ExponentContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.primary()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 94
                self.match(PolyUHFParser.T__9)
                self.state = 95
                self.exponentExpr()


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



    class HexBigIntExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEX_BIGINT(self):
            return self.getToken(PolyUHFParser.HEX_BIGINT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexBigIntExpr" ):
                return visitor.visitHexBigIntExpr(self)
            else:
                return visitor.visitChildren(self)


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


    class DecIntExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEC_INT(self):
            return self.getToken(PolyUHFParser.DEC_INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecIntExpr" ):
                return visitor.visitDecIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class DecBigIntExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEC_BIGINT(self):
            return self.getToken(PolyUHFParser.DEC_BIGINT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecBigIntExpr" ):
                return visitor.visitDecBigIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class CallExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.ExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class HexIntExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEX_INT(self):
            return self.getToken(PolyUHFParser.HEX_INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexIntExpr" ):
                return visitor.visitHexIntExpr(self)
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


    class IfElseExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(PolyUHFParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.ExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.ExprContext,i)

        def ELSE(self):
            return self.getToken(PolyUHFParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseExpr" ):
                return visitor.visitIfElseExpr(self)
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
        self.enterRule(localctx, 22, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(PolyUHFParser.T__0)
                self.state = 99
                self.expr()
                self.state = 100
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.IfElseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(PolyUHFParser.IF)
                self.state = 103
                self.expr()
                self.state = 104
                self.match(PolyUHFParser.T__3)
                self.state = 105
                self.expr()
                self.state = 106
                self.match(PolyUHFParser.T__4)
                self.state = 107
                self.match(PolyUHFParser.ELSE)
                self.state = 108
                self.match(PolyUHFParser.T__3)
                self.state = 109
                self.expr()
                self.state = 110
                self.match(PolyUHFParser.T__4)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.HexBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.match(PolyUHFParser.HEX_BIGINT)
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.DecBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.match(PolyUHFParser.DEC_BIGINT)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.HexIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.match(PolyUHFParser.HEX_INT)
                pass

            elif la_ == 6:
                localctx = PolyUHFParser.DecIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.match(PolyUHFParser.DEC_INT)
                pass

            elif la_ == 7:
                localctx = PolyUHFParser.CallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 116
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 117
                self.match(PolyUHFParser.T__0)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080408002) != 0):
                    self.state = 118
                    self.expr()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 119
                        self.match(PolyUHFParser.T__1)
                        self.state = 120
                        self.expr()
                        self.state = 125
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 128
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 8:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 129
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 130
                self.match(PolyUHFParser.T__10)
                self.state = 131
                self.expr()
                self.state = 132
                self.match(PolyUHFParser.T__11)
                pass

            elif la_ == 9:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 134
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 10:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 135
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==8):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 136
                self.match(PolyUHFParser.T__10)
                self.state = 137
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 138
                self.match(PolyUHFParser.T__1)
                self.state = 139
                self.expr()
                self.state = 140
                self.match(PolyUHFParser.T__12)
                self.state = 141
                self.expr()
                self.state = 142
                self.match(PolyUHFParser.T__12)
                self.state = 143
                self.expr()
                self.state = 144
                self.match(PolyUHFParser.T__11)
                self.state = 145
                self.match(PolyUHFParser.T__3)
                self.state = 146
                self.expr()
                self.state = 147
                self.match(PolyUHFParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





