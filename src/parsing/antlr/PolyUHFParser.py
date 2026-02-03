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
        4,1,24,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,3,1,37,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,3,1,3,
        1,3,1,4,1,4,1,5,1,5,1,5,5,5,62,8,5,10,5,12,5,65,9,5,1,6,1,6,1,6,
        5,6,70,8,6,10,6,12,6,73,9,6,1,7,1,7,1,7,3,7,78,8,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,95,8,8,10,8,12,
        8,98,9,8,3,8,100,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,123,8,8,1,8,0,0,9,0,
        2,4,6,8,10,12,14,16,0,4,1,0,15,16,1,0,6,7,1,0,8,9,2,0,6,6,8,8,133,
        0,19,1,0,0,0,2,25,1,0,0,0,4,44,1,0,0,0,6,46,1,0,0,0,8,56,1,0,0,0,
        10,58,1,0,0,0,12,66,1,0,0,0,14,74,1,0,0,0,16,122,1,0,0,0,18,20,3,
        2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,
        23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,14,0,0,26,27,5,17,
        0,0,27,36,5,1,0,0,28,33,3,6,3,0,29,30,5,2,0,0,30,32,3,6,3,0,31,29,
        1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,37,1,0,0,0,
        35,33,1,0,0,0,36,28,1,0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,5,
        3,0,0,39,40,3,4,2,0,40,41,5,4,0,0,41,42,3,8,4,0,42,43,5,5,0,0,43,
        3,1,0,0,0,44,45,7,0,0,0,45,5,1,0,0,0,46,51,5,17,0,0,47,48,5,2,0,
        0,48,50,5,17,0,0,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,3,4,2,0,55,7,1,0,0,0,56,
        57,3,10,5,0,57,9,1,0,0,0,58,63,3,12,6,0,59,60,7,1,0,0,60,62,3,12,
        6,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,11,
        1,0,0,0,65,63,1,0,0,0,66,71,3,14,7,0,67,68,7,2,0,0,68,70,3,14,7,
        0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,13,
        1,0,0,0,73,71,1,0,0,0,74,77,3,16,8,0,75,76,5,10,0,0,76,78,3,14,7,
        0,77,75,1,0,0,0,77,78,1,0,0,0,78,15,1,0,0,0,79,80,5,7,0,0,80,123,
        3,16,8,0,81,82,5,1,0,0,82,83,3,8,4,0,83,84,5,3,0,0,84,123,1,0,0,
        0,85,123,5,18,0,0,86,123,5,19,0,0,87,123,5,20,0,0,88,123,5,21,0,
        0,89,90,5,17,0,0,90,99,5,1,0,0,91,96,3,8,4,0,92,93,5,2,0,0,93,95,
        3,8,4,0,94,92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,
        97,100,1,0,0,0,98,96,1,0,0,0,99,91,1,0,0,0,99,100,1,0,0,0,100,101,
        1,0,0,0,101,123,5,3,0,0,102,103,5,17,0,0,103,104,5,11,0,0,104,105,
        3,8,4,0,105,106,5,12,0,0,106,123,1,0,0,0,107,123,5,17,0,0,108,109,
        7,3,0,0,109,110,5,11,0,0,110,111,5,17,0,0,111,112,5,2,0,0,112,113,
        3,8,4,0,113,114,5,13,0,0,114,115,3,8,4,0,115,116,5,13,0,0,116,117,
        3,8,4,0,117,118,5,12,0,0,118,119,5,4,0,0,119,120,3,8,4,0,120,121,
        5,5,0,0,121,123,1,0,0,0,122,79,1,0,0,0,122,81,1,0,0,0,122,85,1,0,
        0,0,122,86,1,0,0,0,122,87,1,0,0,0,122,88,1,0,0,0,122,89,1,0,0,0,
        122,102,1,0,0,0,122,107,1,0,0,0,122,108,1,0,0,0,123,17,1,0,0,0,10,
        21,33,36,51,63,71,77,96,99,122
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "'+'", 
                     "'-'", "'*'", "'/'", "'^'", "'['", "']'", "':'", "'func'", 
                     "'bigint'", "'index'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNCTION", "TYPE_BIGINT", 
                      "TYPE_INDEX", "IDENTIFIER", "HEX_BIGINT", "DEC_BIGINT", 
                      "HEX_INT", "DEC_INT", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_type_annotation = 2
    RULE_param_group = 3
    RULE_expr = 4
    RULE_addSubExpr = 5
    RULE_mulDivExpr = 6
    RULE_exponentExpr = 7
    RULE_primary = 8

    ruleNames =  [ "program", "function", "type_annotation", "param_group", 
                   "expr", "addSubExpr", "mulDivExpr", "exponentExpr", "primary" ]

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
    TYPE_BIGINT=15
    TYPE_INDEX=16
    IDENTIFIER=17
    HEX_BIGINT=18
    DEC_BIGINT=19
    HEX_INT=20
    DEC_INT=21
    WS=22
    LINE_COMMENT=23
    BLOCK_COMMENT=24

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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.function()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 23
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
            self.state = 25
            self.match(PolyUHFParser.FUNCTION)
            self.state = 26
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 27
            self.match(PolyUHFParser.T__0)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 28
                self.param_group()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 29
                    self.match(PolyUHFParser.T__1)
                    self.state = 30
                    self.param_group()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 38
            self.match(PolyUHFParser.T__2)
            self.state = 39
            self.type_annotation()
            self.state = 40
            self.match(PolyUHFParser.T__3)
            self.state = 41
            self.expr()
            self.state = 42
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

        def TYPE_BIGINT(self):
            return self.getToken(PolyUHFParser.TYPE_BIGINT, 0)

        def TYPE_INDEX(self):
            return self.getToken(PolyUHFParser.TYPE_INDEX, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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
            self.state = 46
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 47
                self.match(PolyUHFParser.T__1)
                self.state = 48
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
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
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
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
            self.s6 = None # Token
            self.op = list() # of Tokens
            self.s7 = None # Token
            self._tset103 = None # Token
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
        self.enterRule(localctx, 10, self.RULE_addSubExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.AddSubContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.mulDivExpr()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 59
                localctx._tset103 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx._tset103 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset103)
                self.state = 60
                self.mulDivExpr()
                self.state = 65
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
            self._tset134 = None # Token
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
        self.enterRule(localctx, 12, self.RULE_mulDivExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulDivContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.exponentExpr()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 67
                localctx._tset134 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    localctx._tset134 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset134)
                self.state = 68
                self.exponentExpr()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 14, self.RULE_exponentExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.ExponentContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.primary()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 75
                self.match(PolyUHFParser.T__9)
                self.state = 76
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
        self.enterRule(localctx, 16, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(PolyUHFParser.T__6)
                self.state = 80
                self.primary()
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(PolyUHFParser.T__0)
                self.state = 82
                self.expr()
                self.state = 83
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.HexBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.match(PolyUHFParser.HEX_BIGINT)
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.DecBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.match(PolyUHFParser.DEC_BIGINT)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.HexIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.match(PolyUHFParser.HEX_INT)
                pass

            elif la_ == 6:
                localctx = PolyUHFParser.DecIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.match(PolyUHFParser.DEC_INT)
                pass

            elif la_ == 7:
                localctx = PolyUHFParser.CallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 90
                self.match(PolyUHFParser.T__0)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4063682) != 0):
                    self.state = 91
                    self.expr()
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 92
                        self.match(PolyUHFParser.T__1)
                        self.state = 93
                        self.expr()
                        self.state = 98
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 101
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 8:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 102
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 103
                self.match(PolyUHFParser.T__10)
                self.state = 104
                self.expr()
                self.state = 105
                self.match(PolyUHFParser.T__11)
                pass

            elif la_ == 9:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 107
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 10:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 108
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==8):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 109
                self.match(PolyUHFParser.T__10)
                self.state = 110
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 111
                self.match(PolyUHFParser.T__1)
                self.state = 112
                self.expr()
                self.state = 113
                self.match(PolyUHFParser.T__12)
                self.state = 114
                self.expr()
                self.state = 115
                self.match(PolyUHFParser.T__12)
                self.state = 116
                self.expr()
                self.state = 117
                self.match(PolyUHFParser.T__11)
                self.state = 118
                self.match(PolyUHFParser.T__3)
                self.state = 119
                self.expr()
                self.state = 120
                self.match(PolyUHFParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





