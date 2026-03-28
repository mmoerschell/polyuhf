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
        4,1,27,140,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,3,1,39,8,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,55,
        9,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,5,5,64,8,5,10,5,12,5,67,9,5,1,6,
        1,6,1,6,5,6,72,8,6,10,6,12,6,75,9,6,1,7,1,7,1,7,3,7,80,8,7,1,8,1,
        8,1,8,3,8,85,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,110,8,9,10,9,12,
        9,113,9,9,3,9,115,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,138,8,9,1,9,0,0,10,
        0,2,4,6,8,10,12,14,16,18,0,3,1,0,6,7,1,0,8,9,2,0,6,6,8,8,148,0,21,
        1,0,0,0,2,27,1,0,0,0,4,46,1,0,0,0,6,48,1,0,0,0,8,58,1,0,0,0,10,60,
        1,0,0,0,12,68,1,0,0,0,14,79,1,0,0,0,16,81,1,0,0,0,18,137,1,0,0,0,
        20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,
        0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,28,5,14,0,0,28,
        29,5,24,0,0,29,38,5,1,0,0,30,35,3,6,3,0,31,32,5,2,0,0,32,34,3,6,
        3,0,33,31,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,39,
        1,0,0,0,37,35,1,0,0,0,38,30,1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,
        40,41,5,3,0,0,41,42,3,4,2,0,42,43,5,4,0,0,43,44,3,8,4,0,44,45,5,
        5,0,0,45,3,1,0,0,0,46,47,5,17,0,0,47,5,1,0,0,0,48,53,5,24,0,0,49,
        50,5,2,0,0,50,52,5,24,0,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,
        0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,3,4,2,0,57,7,
        1,0,0,0,58,59,3,10,5,0,59,9,1,0,0,0,60,65,3,12,6,0,61,62,7,0,0,0,
        62,64,3,12,6,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,
        0,0,0,66,11,1,0,0,0,67,65,1,0,0,0,68,73,3,14,7,0,69,70,7,1,0,0,70,
        72,3,14,7,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,
        0,0,74,13,1,0,0,0,75,73,1,0,0,0,76,77,5,7,0,0,77,80,3,14,7,0,78,
        80,3,16,8,0,79,76,1,0,0,0,79,78,1,0,0,0,80,15,1,0,0,0,81,84,3,18,
        9,0,82,83,5,10,0,0,83,85,3,16,8,0,84,82,1,0,0,0,84,85,1,0,0,0,85,
        17,1,0,0,0,86,87,5,1,0,0,87,88,3,8,4,0,88,89,5,3,0,0,89,138,1,0,
        0,0,90,91,5,15,0,0,91,92,3,8,4,0,92,93,5,4,0,0,93,94,3,8,4,0,94,
        95,5,5,0,0,95,96,5,16,0,0,96,97,5,4,0,0,97,98,3,8,4,0,98,99,5,5,
        0,0,99,138,1,0,0,0,100,138,5,20,0,0,101,138,5,21,0,0,102,138,5,22,
        0,0,103,138,5,23,0,0,104,105,5,24,0,0,105,114,5,1,0,0,106,111,3,
        8,4,0,107,108,5,2,0,0,108,110,3,8,4,0,109,107,1,0,0,0,110,113,1,
        0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,115,1,0,0,0,113,111,1,
        0,0,0,114,106,1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,138,5,
        3,0,0,117,118,5,24,0,0,118,119,5,11,0,0,119,120,3,8,4,0,120,121,
        5,12,0,0,121,138,1,0,0,0,122,138,5,24,0,0,123,124,7,2,0,0,124,125,
        5,11,0,0,125,126,5,24,0,0,126,127,5,2,0,0,127,128,3,8,4,0,128,129,
        5,13,0,0,129,130,3,8,4,0,130,131,5,13,0,0,131,132,3,8,4,0,132,133,
        5,12,0,0,133,134,5,4,0,0,134,135,3,8,4,0,135,136,5,5,0,0,136,138,
        1,0,0,0,137,86,1,0,0,0,137,90,1,0,0,0,137,100,1,0,0,0,137,101,1,
        0,0,0,137,102,1,0,0,0,137,103,1,0,0,0,137,104,1,0,0,0,137,117,1,
        0,0,0,137,122,1,0,0,0,137,123,1,0,0,0,138,19,1,0,0,0,11,23,35,38,
        53,65,73,79,84,111,114,137
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "'+'", 
                     "'-'", "'*'", "'/'", "'^'", "'['", "']'", "':'", "'func'", 
                     "'if'", "'else'", "<INVALID>", "'bigint'", "'index'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNCTION", "IF", "ELSE", 
                      "TYPE_ANNOTATION", "TYPE_BIGINT", "TYPE_INDEX", "HEX_BIGINT", 
                      "DEC_BIGINT", "HEX_INT", "DEC_INT", "IDENTIFIER", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_type_annotation = 2
    RULE_param_group = 3
    RULE_expr = 4
    RULE_addSubExpr = 5
    RULE_mulDivExpr = 6
    RULE_unaryMinusExpr = 7
    RULE_exponentExpr = 8
    RULE_primary = 9

    ruleNames =  [ "program", "function", "type_annotation", "param_group", 
                   "expr", "addSubExpr", "mulDivExpr", "unaryMinusExpr", 
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
    IF=15
    ELSE=16
    TYPE_ANNOTATION=17
    TYPE_BIGINT=18
    TYPE_INDEX=19
    HEX_BIGINT=20
    DEC_BIGINT=21
    HEX_INT=22
    DEC_INT=23
    IDENTIFIER=24
    WS=25
    LINE_COMMENT=26
    BLOCK_COMMENT=27

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.function()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 25
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
            self.state = 27
            self.match(PolyUHFParser.FUNCTION)
            self.state = 28
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 29
            self.match(PolyUHFParser.T__0)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 30
                self.param_group()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 31
                    self.match(PolyUHFParser.T__1)
                    self.state = 32
                    self.param_group()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 40
            self.match(PolyUHFParser.T__2)
            self.state = 41
            self.type_annotation()
            self.state = 42
            self.match(PolyUHFParser.T__3)
            self.state = 43
            self.expr()
            self.state = 44
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
            self.state = 46
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
            self.state = 48
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 49
                self.match(PolyUHFParser.T__1)
                self.state = 50
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
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
            self.state = 58
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
            self._tset99 = None # Token
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
            self.state = 60
            self.mulDivExpr()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 61
                localctx._tset99 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx._tset99 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset99)
                self.state = 62
                self.mulDivExpr()
                self.state = 67
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
            self._tset130 = None # Token
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
        self.enterRule(localctx, 12, self.RULE_mulDivExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulDivContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.unaryMinusExpr()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 69
                localctx._tset130 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    localctx._tset130 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset130)
                self.state = 70
                self.unaryMinusExpr()
                self.state = 75
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
        self.enterRule(localctx, 14, self.RULE_unaryMinusExpr)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PolyUHFParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(PolyUHFParser.T__6)
                self.state = 77
                self.unaryMinusExpr()
                pass
            elif token in [1, 6, 8, 15, 20, 21, 22, 23, 24]:
                localctx = PolyUHFParser.UnaryAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
        self.enterRule(localctx, 16, self.RULE_exponentExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.ExponentContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.primary()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 82
                self.match(PolyUHFParser.T__9)
                self.state = 83
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
        self.enterRule(localctx, 18, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(PolyUHFParser.T__0)
                self.state = 87
                self.expr()
                self.state = 88
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.IfElseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(PolyUHFParser.IF)
                self.state = 91
                self.expr()
                self.state = 92
                self.match(PolyUHFParser.T__3)
                self.state = 93
                self.expr()
                self.state = 94
                self.match(PolyUHFParser.T__4)
                self.state = 95
                self.match(PolyUHFParser.ELSE)
                self.state = 96
                self.match(PolyUHFParser.T__3)
                self.state = 97
                self.expr()
                self.state = 98
                self.match(PolyUHFParser.T__4)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.HexBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.match(PolyUHFParser.HEX_BIGINT)
                pass

            elif la_ == 4:
                localctx = PolyUHFParser.DecBigIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.match(PolyUHFParser.DEC_BIGINT)
                pass

            elif la_ == 5:
                localctx = PolyUHFParser.HexIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.match(PolyUHFParser.HEX_INT)
                pass

            elif la_ == 6:
                localctx = PolyUHFParser.DecIntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 103
                self.match(PolyUHFParser.DEC_INT)
                pass

            elif la_ == 7:
                localctx = PolyUHFParser.CallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 104
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 105
                self.match(PolyUHFParser.T__0)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32539074) != 0):
                    self.state = 106
                    self.expr()
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 107
                        self.match(PolyUHFParser.T__1)
                        self.state = 108
                        self.expr()
                        self.state = 113
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 116
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 8:
                localctx = PolyUHFParser.ArrayExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 117
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 118
                self.match(PolyUHFParser.T__10)
                self.state = 119
                self.expr()
                self.state = 120
                self.match(PolyUHFParser.T__11)
                pass

            elif la_ == 9:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 122
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 10:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 123
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==8):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 124
                self.match(PolyUHFParser.T__10)
                self.state = 125
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 126
                self.match(PolyUHFParser.T__1)
                self.state = 127
                self.expr()
                self.state = 128
                self.match(PolyUHFParser.T__12)
                self.state = 129
                self.expr()
                self.state = 130
                self.match(PolyUHFParser.T__12)
                self.state = 131
                self.expr()
                self.state = 132
                self.match(PolyUHFParser.T__11)
                self.state = 133
                self.match(PolyUHFParser.T__3)
                self.state = 134
                self.expr()
                self.state = 135
                self.match(PolyUHFParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





