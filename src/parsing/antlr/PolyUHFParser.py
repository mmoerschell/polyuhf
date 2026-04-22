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
        4,1,35,160,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,
        9,1,3,1,43,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,57,8,1,1,2,1,2,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,1,3,1,3,
        1,4,1,4,1,5,1,5,1,5,1,5,3,5,77,8,5,1,6,1,6,1,7,1,7,1,7,5,7,84,8,
        7,10,7,12,7,87,9,7,1,8,1,8,1,8,5,8,92,8,8,10,8,12,8,95,9,8,1,9,1,
        9,1,9,3,9,100,8,9,1,10,1,10,1,10,3,10,105,8,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,130,8,11,10,11,12,11,133,9,
        11,3,11,135,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,158,
        8,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,4,1,0,22,27,1,
        0,6,7,1,0,8,10,2,0,6,6,8,8,168,0,25,1,0,0,0,2,56,1,0,0,0,4,58,1,
        0,0,0,6,60,1,0,0,0,8,70,1,0,0,0,10,72,1,0,0,0,12,78,1,0,0,0,14,80,
        1,0,0,0,16,88,1,0,0,0,18,99,1,0,0,0,20,101,1,0,0,0,22,157,1,0,0,
        0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,
        1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,32,5,16,0,0,
        32,33,5,32,0,0,33,42,5,1,0,0,34,39,3,6,3,0,35,36,5,2,0,0,36,38,3,
        6,3,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,
        43,1,0,0,0,41,39,1,0,0,0,42,34,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,
        0,44,45,5,3,0,0,45,46,3,4,2,0,46,47,5,4,0,0,47,48,3,8,4,0,48,49,
        5,5,0,0,49,57,1,0,0,0,50,51,5,15,0,0,51,52,5,32,0,0,52,53,5,4,0,
        0,53,54,3,8,4,0,54,55,5,5,0,0,55,57,1,0,0,0,56,31,1,0,0,0,56,50,
        1,0,0,0,57,3,1,0,0,0,58,59,5,19,0,0,59,5,1,0,0,0,60,65,5,32,0,0,
        61,62,5,2,0,0,62,64,5,32,0,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,1,
        0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,3,4,2,0,69,
        7,1,0,0,0,70,71,3,10,5,0,71,9,1,0,0,0,72,76,3,14,7,0,73,74,3,12,
        6,0,74,75,3,14,7,0,75,77,1,0,0,0,76,73,1,0,0,0,76,77,1,0,0,0,77,
        11,1,0,0,0,78,79,7,0,0,0,79,13,1,0,0,0,80,85,3,16,8,0,81,82,7,1,
        0,0,82,84,3,16,8,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,
        86,1,0,0,0,86,15,1,0,0,0,87,85,1,0,0,0,88,93,3,18,9,0,89,90,7,2,
        0,0,90,92,3,18,9,0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,
        94,1,0,0,0,94,17,1,0,0,0,95,93,1,0,0,0,96,97,5,7,0,0,97,100,3,18,
        9,0,98,100,3,20,10,0,99,96,1,0,0,0,99,98,1,0,0,0,100,19,1,0,0,0,
        101,104,3,22,11,0,102,103,5,11,0,0,103,105,3,20,10,0,104,102,1,0,
        0,0,104,105,1,0,0,0,105,21,1,0,0,0,106,107,5,1,0,0,107,108,3,8,4,
        0,108,109,5,3,0,0,109,158,1,0,0,0,110,111,5,17,0,0,111,112,3,8,4,
        0,112,113,5,4,0,0,113,114,3,8,4,0,114,115,5,5,0,0,115,116,5,18,0,
        0,116,117,5,4,0,0,117,118,3,8,4,0,118,119,5,5,0,0,119,158,1,0,0,
        0,120,158,5,28,0,0,121,158,5,29,0,0,122,158,5,30,0,0,123,158,5,31,
        0,0,124,125,5,32,0,0,125,134,5,1,0,0,126,131,3,8,4,0,127,128,5,2,
        0,0,128,130,3,8,4,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,
        0,0,131,132,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,134,126,1,0,
        0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,158,5,3,0,0,137,138,5,32,
        0,0,138,139,5,12,0,0,139,140,3,8,4,0,140,141,5,13,0,0,141,158,1,
        0,0,0,142,158,5,32,0,0,143,144,7,3,0,0,144,145,5,12,0,0,145,146,
        5,32,0,0,146,147,5,2,0,0,147,148,3,8,4,0,148,149,5,14,0,0,149,150,
        3,8,4,0,150,151,5,14,0,0,151,152,3,8,4,0,152,153,5,13,0,0,153,154,
        5,4,0,0,154,155,3,8,4,0,155,156,5,5,0,0,156,158,1,0,0,0,157,106,
        1,0,0,0,157,110,1,0,0,0,157,120,1,0,0,0,157,121,1,0,0,0,157,122,
        1,0,0,0,157,123,1,0,0,0,157,124,1,0,0,0,157,137,1,0,0,0,157,142,
        1,0,0,0,157,143,1,0,0,0,158,23,1,0,0,0,13,27,39,42,56,65,76,85,93,
        99,104,131,134,157
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'^'", "'['", "']'", "':'", 
                     "'hashfunc'", "'func'", "'if'", "'else'", "<INVALID>", 
                     "'bigint'", "'index'", "'=='", "'!='", "'<='", "'>='", 
                     "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "HASHFUNC", 
                      "FUNCTION", "IF", "ELSE", "TYPE_ANNOTATION", "TYPE_BIGINT", 
                      "TYPE_INDEX", "EQ", "NEQ", "LE", "GE", "LT", "GT", 
                      "HEX_BIGINT", "DEC_BIGINT", "HEX_INT", "DEC_INT", 
                      "IDENTIFIER", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

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
    T__13=14
    HASHFUNC=15
    FUNCTION=16
    IF=17
    ELSE=18
    TYPE_ANNOTATION=19
    TYPE_BIGINT=20
    TYPE_INDEX=21
    EQ=22
    NEQ=23
    LE=24
    GE=25
    LT=26
    GT=27
    HEX_BIGINT=28
    DEC_BIGINT=29
    HEX_INT=30
    DEC_INT=31
    IDENTIFIER=32
    WS=33
    LINE_COMMENT=34
    BLOCK_COMMENT=35

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
                if not (_la==15 or _la==16):
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


        def getRuleIndex(self):
            return PolyUHFParser.RULE_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HashFunctionContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HASHFUNC(self):
            return self.getToken(PolyUHFParser.HASHFUNC, 0)
        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashFunction" ):
                return visitor.visitHashFunction(self)
            else:
                return visitor.visitChildren(self)


    class HelperFunctionContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelperFunction" ):
                return visitor.visitHelperFunction(self)
            else:
                return visitor.visitChildren(self)



    def function(self):

        localctx = PolyUHFParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = PolyUHFParser.HelperFunctionContext(self, localctx)
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
                if _la==32:
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
                pass
            elif token in [15]:
                localctx = PolyUHFParser.HashFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(PolyUHFParser.HASHFUNC)
                self.state = 51
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 52
                self.match(PolyUHFParser.T__3)
                self.state = 53
                self.expr()
                self.state = 54
                self.match(PolyUHFParser.T__4)
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
            self.state = 58
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
            self.state = 60
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 61
                self.match(PolyUHFParser.T__1)
                self.state = 62
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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
            self.state = 70
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
            self.state = 72
            self.addSubExpr()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0):
                self.state = 73
                self.compOp()
                self.state = 74
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
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
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
            self._tset166 = None # Token
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
            self.state = 80
            self.mulDivExpr()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 81
                localctx._tset166 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx._tset166 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset166)
                self.state = 82
                self.mulDivExpr()
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
            self.s10 = None # Token
            self._tset197 = None # Token
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
            self.state = 88
            self.unaryMinusExpr()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 89
                localctx._tset197 = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                    localctx._tset197 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset197)
                self.state = 90
                self.unaryMinusExpr()
                self.state = 95
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
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PolyUHFParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(PolyUHFParser.T__6)
                self.state = 97
                self.unaryMinusExpr()
                pass
            elif token in [1, 6, 8, 17, 28, 29, 30, 31, 32]:
                localctx = PolyUHFParser.UnaryAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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
            self.state = 101
            self.primary()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 102
                self.match(PolyUHFParser.T__10)
                self.state = 103
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(PolyUHFParser.T__0)
                self.state = 107
                self.expr()
                self.state = 108
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.IfElseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(PolyUHFParser.IF)
                self.state = 111
                self.expr()
                self.state = 112
                self.match(PolyUHFParser.T__3)
                self.state = 113
                self.expr()
                self.state = 114
                self.match(PolyUHFParser.T__4)
                self.state = 115
                self.match(PolyUHFParser.ELSE)
                self.state = 116
                self.match(PolyUHFParser.T__3)
                self.state = 117
                self.expr()
                self.state = 118
                self.match(PolyUHFParser.T__4)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.HexBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(PolyUHFParser.HEX_BIGINT)
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.DecBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.match(PolyUHFParser.DEC_BIGINT)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.HexIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.match(PolyUHFParser.HEX_INT)
                pass

            elif la_ == 6:
                localctx = PolyUHFParser.DecIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self.match(PolyUHFParser.DEC_INT)
                pass

            elif la_ == 7:
                localctx = PolyUHFParser.CallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 124
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 125
                self.match(PolyUHFParser.T__0)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8321630658) != 0):
                    self.state = 126
                    self.expr()
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 127
                        self.match(PolyUHFParser.T__1)
                        self.state = 128
                        self.expr()
                        self.state = 133
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 136
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 8:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 137
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 138
                self.match(PolyUHFParser.T__11)
                self.state = 139
                self.expr()
                self.state = 140
                self.match(PolyUHFParser.T__12)
                pass

            elif la_ == 9:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 142
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 10:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 143
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==8):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.match(PolyUHFParser.T__11)
                self.state = 145
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 146
                self.match(PolyUHFParser.T__1)
                self.state = 147
                self.expr()
                self.state = 148
                self.match(PolyUHFParser.T__13)
                self.state = 149
                self.expr()
                self.state = 150
                self.match(PolyUHFParser.T__13)
                self.state = 151
                self.expr()
                self.state = 152
                self.match(PolyUHFParser.T__12)
                self.state = 153
                self.match(PolyUHFParser.T__3)
                self.state = 154
                self.expr()
                self.state = 155
                self.match(PolyUHFParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





