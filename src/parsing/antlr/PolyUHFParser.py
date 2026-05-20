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
        4,1,37,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,3,1,45,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,
        56,8,2,10,2,12,2,59,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,72,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,84,8,
        4,1,5,1,5,1,6,1,6,1,6,1,6,3,6,92,8,6,1,7,1,7,1,8,1,8,1,8,5,8,99,
        8,8,10,8,12,8,102,9,8,1,9,1,9,1,9,5,9,107,8,9,10,9,12,9,110,9,9,
        1,10,1,10,1,10,3,10,115,8,10,1,11,1,11,1,11,3,11,120,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,139,8,12,1,12,1,12,1,12,3,12,144,8,12,1,12,1,12,
        1,12,1,12,1,12,5,12,151,8,12,10,12,12,12,154,9,12,3,12,156,8,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,179,8,12,1,12,0,0,13,
        0,2,4,6,8,10,12,14,16,18,20,22,24,0,4,1,0,26,31,1,0,9,10,1,0,11,
        13,2,0,9,9,11,11,190,0,27,1,0,0,0,2,33,1,0,0,0,4,52,1,0,0,0,6,71,
        1,0,0,0,8,83,1,0,0,0,10,85,1,0,0,0,12,87,1,0,0,0,14,93,1,0,0,0,16,
        95,1,0,0,0,18,103,1,0,0,0,20,114,1,0,0,0,22,116,1,0,0,0,24,178,1,
        0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,
        30,1,0,0,0,30,31,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,34,5,19,0,
        0,34,35,5,34,0,0,35,44,5,1,0,0,36,41,3,4,2,0,37,38,5,2,0,0,38,40,
        3,4,2,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,
        42,45,1,0,0,0,43,41,1,0,0,0,44,36,1,0,0,0,44,45,1,0,0,0,45,46,1,
        0,0,0,46,47,5,3,0,0,47,48,3,6,3,0,48,49,5,4,0,0,49,50,3,10,5,0,50,
        51,5,5,0,0,51,3,1,0,0,0,52,57,5,34,0,0,53,54,5,2,0,0,54,56,5,34,
        0,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,
        1,0,0,0,59,57,1,0,0,0,60,61,3,6,3,0,61,5,1,0,0,0,62,63,5,6,0,0,63,
        64,5,30,0,0,64,65,3,8,4,0,65,66,5,2,0,0,66,67,5,33,0,0,67,68,5,31,
        0,0,68,72,1,0,0,0,69,72,3,8,4,0,70,72,5,25,0,0,71,62,1,0,0,0,71,
        69,1,0,0,0,71,70,1,0,0,0,72,7,1,0,0,0,73,74,5,7,0,0,74,75,5,30,0,
        0,75,76,5,33,0,0,76,77,5,2,0,0,77,78,5,33,0,0,78,84,5,31,0,0,79,
        80,5,8,0,0,80,81,5,30,0,0,81,82,5,33,0,0,82,84,5,31,0,0,83,73,1,
        0,0,0,83,79,1,0,0,0,84,9,1,0,0,0,85,86,3,12,6,0,86,11,1,0,0,0,87,
        91,3,16,8,0,88,89,3,14,7,0,89,90,3,16,8,0,90,92,1,0,0,0,91,88,1,
        0,0,0,91,92,1,0,0,0,92,13,1,0,0,0,93,94,7,0,0,0,94,15,1,0,0,0,95,
        100,3,18,9,0,96,97,7,1,0,0,97,99,3,18,9,0,98,96,1,0,0,0,99,102,1,
        0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,17,1,0,0,0,102,100,1,0,
        0,0,103,108,3,20,10,0,104,105,7,2,0,0,105,107,3,20,10,0,106,104,
        1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,19,1,
        0,0,0,110,108,1,0,0,0,111,112,5,10,0,0,112,115,3,20,10,0,113,115,
        3,22,11,0,114,111,1,0,0,0,114,113,1,0,0,0,115,21,1,0,0,0,116,119,
        3,24,12,0,117,118,5,14,0,0,118,120,3,22,11,0,119,117,1,0,0,0,119,
        120,1,0,0,0,120,23,1,0,0,0,121,122,5,1,0,0,122,123,3,10,5,0,123,
        124,5,3,0,0,124,179,1,0,0,0,125,126,5,20,0,0,126,127,3,10,5,0,127,
        128,5,4,0,0,128,129,3,10,5,0,129,130,5,5,0,0,130,131,5,21,0,0,131,
        132,5,4,0,0,132,133,3,10,5,0,133,134,5,5,0,0,134,179,1,0,0,0,135,
        138,5,32,0,0,136,137,5,22,0,0,137,139,3,6,3,0,138,136,1,0,0,0,138,
        139,1,0,0,0,139,179,1,0,0,0,140,143,5,33,0,0,141,142,5,22,0,0,142,
        144,3,6,3,0,143,141,1,0,0,0,143,144,1,0,0,0,144,179,1,0,0,0,145,
        146,5,34,0,0,146,155,5,1,0,0,147,152,3,10,5,0,148,149,5,2,0,0,149,
        151,3,10,5,0,150,148,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,
        153,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,155,147,1,0,0,0,155,
        156,1,0,0,0,156,157,1,0,0,0,157,179,5,3,0,0,158,159,5,34,0,0,159,
        160,5,15,0,0,160,161,3,10,5,0,161,162,5,16,0,0,162,179,1,0,0,0,163,
        179,5,34,0,0,164,165,7,3,0,0,165,166,5,15,0,0,166,167,5,34,0,0,167,
        168,5,2,0,0,168,169,3,10,5,0,169,170,5,17,0,0,170,171,3,10,5,0,171,
        172,5,17,0,0,172,173,3,10,5,0,173,174,5,16,0,0,174,175,5,4,0,0,175,
        176,3,10,5,0,176,177,5,5,0,0,177,179,1,0,0,0,178,121,1,0,0,0,178,
        125,1,0,0,0,178,135,1,0,0,0,178,140,1,0,0,0,178,145,1,0,0,0,178,
        158,1,0,0,0,178,163,1,0,0,0,178,164,1,0,0,0,179,25,1,0,0,0,16,29,
        41,44,57,71,83,91,100,108,114,119,138,143,152,155,178
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "'bufferview'", 
                     "'prime'", "'binary'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'['", "']'", "':'", "'hashfunc'", "'func'", 
                     "'if'", "'else'", "'as'", "'zero'", "<INVALID>", "'index'", 
                     "'=='", "'!='", "'<='", "'>='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "HASHFUNC", "FUNCTION", 
                      "IF", "ELSE", "AS", "PADDING", "ENDIANNESS", "INDEX", 
                      "EQ", "NEQ", "LE", "GE", "LT", "GT", "HEXADECIMAL", 
                      "DECIMAL", "IDENTIFIER", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_module = 0
    RULE_function = 1
    RULE_param_group = 2
    RULE_ttype = 3
    RULE_field_ttype = 4
    RULE_expr = 5
    RULE_comparisonExpr = 6
    RULE_compOp = 7
    RULE_addSubExpr = 8
    RULE_mulDivExpr = 9
    RULE_unaryMinusExpr = 10
    RULE_exponentExpr = 11
    RULE_primary = 12

    ruleNames =  [ "module", "function", "param_group", "ttype", "field_ttype", 
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
    T__14=15
    T__15=16
    T__16=17
    HASHFUNC=18
    FUNCTION=19
    IF=20
    ELSE=21
    AS=22
    PADDING=23
    ENDIANNESS=24
    INDEX=25
    EQ=26
    NEQ=27
    LE=28
    GE=29
    LT=30
    GT=31
    HEXADECIMAL=32
    DECIMAL=33
    IDENTIFIER=34
    WS=35
    LINE_COMMENT=36
    BLOCK_COMMENT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
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
            return PolyUHFParser.RULE_module

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule" ):
                return visitor.visitModule(self)
            else:
                return visitor.visitChildren(self)




    def module(self):

        localctx = PolyUHFParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.function()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==19):
                    break

            self.state = 31
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

        def ttype(self):
            return self.getTypedRuleContext(PolyUHFParser.TtypeContext,0)


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
            self.state = 33
            self.match(PolyUHFParser.FUNCTION)
            self.state = 34
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 35
            self.match(PolyUHFParser.T__0)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 36
                self.param_group()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 37
                    self.match(PolyUHFParser.T__1)
                    self.state = 38
                    self.param_group()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 46
            self.match(PolyUHFParser.T__2)
            self.state = 47
            self.ttype()
            self.state = 48
            self.match(PolyUHFParser.T__3)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(PolyUHFParser.T__4)
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

        def ttype(self):
            return self.getTypedRuleContext(PolyUHFParser.TtypeContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_param_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_group" ):
                return visitor.visitParam_group(self)
            else:
                return visitor.visitChildren(self)




    def param_group(self):

        localctx = PolyUHFParser.Param_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_param_group)
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
            self.ttype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_ttype

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BufferViewTypeContext(TtypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.TtypeContext
            super().__init__(parser)
            self.underlying = None # Field_ttypeContext
            self.chunk_size = None # Token
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(PolyUHFParser.LT, 0)
        def GT(self):
            return self.getToken(PolyUHFParser.GT, 0)
        def field_ttype(self):
            return self.getTypedRuleContext(PolyUHFParser.Field_ttypeContext,0)

        def DECIMAL(self):
            return self.getToken(PolyUHFParser.DECIMAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBufferViewType" ):
                return visitor.visitBufferViewType(self)
            else:
                return visitor.visitChildren(self)


    class IndexTypeContext(TtypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.TtypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INDEX(self):
            return self.getToken(PolyUHFParser.INDEX, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexType" ):
                return visitor.visitIndexType(self)
            else:
                return visitor.visitChildren(self)


    class FieldTypeContext(TtypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.TtypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def field_ttype(self):
            return self.getTypedRuleContext(PolyUHFParser.Field_ttypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldType" ):
                return visitor.visitFieldType(self)
            else:
                return visitor.visitChildren(self)



    def ttype(self):

        localctx = PolyUHFParser.TtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ttype)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = PolyUHFParser.BufferViewTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(PolyUHFParser.T__5)
                self.state = 63
                self.match(PolyUHFParser.LT)
                self.state = 64
                localctx.underlying = self.field_ttype()
                self.state = 65
                self.match(PolyUHFParser.T__1)
                self.state = 66
                localctx.chunk_size = self.match(PolyUHFParser.DECIMAL)
                self.state = 67
                self.match(PolyUHFParser.GT)
                pass
            elif token in [7, 8]:
                localctx = PolyUHFParser.FieldTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.field_ttype()
                pass
            elif token in [25]:
                localctx = PolyUHFParser.IndexTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(PolyUHFParser.INDEX)
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


    class Field_ttypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PolyUHFParser.RULE_field_ttype

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BinaryFieldTypeContext(Field_ttypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.Field_ttypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(PolyUHFParser.LT, 0)
        def DECIMAL(self):
            return self.getToken(PolyUHFParser.DECIMAL, 0)
        def GT(self):
            return self.getToken(PolyUHFParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryFieldType" ):
                return visitor.visitBinaryFieldType(self)
            else:
                return visitor.visitChildren(self)


    class PrimeFieldTypeContext(Field_ttypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.Field_ttypeContext
            super().__init__(parser)
            self.pi = None # Token
            self.theta = None # Token
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(PolyUHFParser.LT, 0)
        def GT(self):
            return self.getToken(PolyUHFParser.GT, 0)
        def DECIMAL(self, i:int=None):
            if i is None:
                return self.getTokens(PolyUHFParser.DECIMAL)
            else:
                return self.getToken(PolyUHFParser.DECIMAL, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimeFieldType" ):
                return visitor.visitPrimeFieldType(self)
            else:
                return visitor.visitChildren(self)



    def field_ttype(self):

        localctx = PolyUHFParser.Field_ttypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field_ttype)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PolyUHFParser.PrimeFieldTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(PolyUHFParser.T__6)
                self.state = 74
                self.match(PolyUHFParser.LT)
                self.state = 75
                localctx.pi = self.match(PolyUHFParser.DECIMAL)
                self.state = 76
                self.match(PolyUHFParser.T__1)
                self.state = 77
                localctx.theta = self.match(PolyUHFParser.DECIMAL)
                self.state = 78
                self.match(PolyUHFParser.GT)
                pass
            elif token in [8]:
                localctx = PolyUHFParser.BinaryFieldTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(PolyUHFParser.T__7)
                self.state = 80
                self.match(PolyUHFParser.LT)
                self.state = 81
                self.match(PolyUHFParser.DECIMAL)
                self.state = 82
                self.match(PolyUHFParser.GT)
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
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
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
        self.enterRule(localctx, 12, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.SingleCompareContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.addSubExpr()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0):
                self.state = 88
                self.compOp()
                self.state = 89
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
        self.enterRule(localctx, 14, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
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
            self.s9 = None # Token
            self.op = list() # of Tokens
            self.s10 = None # Token
            self._tset220 = None # Token
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
        self.enterRule(localctx, 16, self.RULE_addSubExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.AddSubContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.mulDivExpr()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 96
                localctx._tset220 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    localctx._tset220 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset220)
                self.state = 97
                self.mulDivExpr()
                self.state = 102
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
            self.s11 = None # Token
            self.op = list() # of Tokens
            self.s12 = None # Token
            self.s13 = None # Token
            self._tset251 = None # Token
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
        self.enterRule(localctx, 18, self.RULE_mulDivExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulDivContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.unaryMinusExpr()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0):
                self.state = 104
                localctx._tset251 = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    localctx._tset251 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset251)
                self.state = 105
                self.unaryMinusExpr()
                self.state = 110
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
        self.enterRule(localctx, 20, self.RULE_unaryMinusExpr)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = PolyUHFParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(PolyUHFParser.T__9)
                self.state = 112
                self.unaryMinusExpr()
                pass
            elif token in [1, 9, 11, 20, 32, 33, 34]:
                localctx = PolyUHFParser.UnaryAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
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
        self.enterRule(localctx, 22, self.RULE_exponentExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.ExponentContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.primary()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 117
                self.match(PolyUHFParser.T__13)
                self.state = 118
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


    class BufferViewReadExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBufferViewReadExpr" ):
                return visitor.visitBufferViewReadExpr(self)
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


    class HexadecimalExpressionContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEXADECIMAL(self):
            return self.getToken(PolyUHFParser.HEXADECIMAL, 0)
        def AS(self):
            return self.getToken(PolyUHFParser.AS, 0)
        def ttype(self):
            return self.getTypedRuleContext(PolyUHFParser.TtypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexadecimalExpression" ):
                return visitor.visitHexadecimalExpression(self)
            else:
                return visitor.visitChildren(self)


    class DecimalExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(PolyUHFParser.DECIMAL, 0)
        def AS(self):
            return self.getToken(PolyUHFParser.AS, 0)
        def ttype(self):
            return self.getTypedRuleContext(PolyUHFParser.TtypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalExpr" ):
                return visitor.visitDecimalExpr(self)
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
        self.enterRule(localctx, 24, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(PolyUHFParser.T__0)
                self.state = 122
                self.expr()
                self.state = 123
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.IfElseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(PolyUHFParser.IF)
                self.state = 126
                self.expr()
                self.state = 127
                self.match(PolyUHFParser.T__3)
                self.state = 128
                self.expr()
                self.state = 129
                self.match(PolyUHFParser.T__4)
                self.state = 130
                self.match(PolyUHFParser.ELSE)
                self.state = 131
                self.match(PolyUHFParser.T__3)
                self.state = 132
                self.expr()
                self.state = 133
                self.match(PolyUHFParser.T__4)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.HexadecimalExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(PolyUHFParser.HEXADECIMAL)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 136
                    self.match(PolyUHFParser.AS)
                    self.state = 137
                    self.ttype()


                pass

            elif la_ == 4:
                localctx = PolyUHFParser.DecimalExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.match(PolyUHFParser.DECIMAL)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 141
                    self.match(PolyUHFParser.AS)
                    self.state = 142
                    self.ttype()


                pass

            elif la_ == 5:
                localctx = PolyUHFParser.CallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 146
                self.match(PolyUHFParser.T__0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30065823234) != 0):
                    self.state = 147
                    self.expr()
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 148
                        self.match(PolyUHFParser.T__1)
                        self.state = 149
                        self.expr()
                        self.state = 154
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 157
                self.match(PolyUHFParser.T__2)
                pass

            elif la_ == 6:
                localctx = PolyUHFParser.BufferViewReadExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 158
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 159
                self.match(PolyUHFParser.T__14)
                self.state = 160
                self.expr()
                self.state = 161
                self.match(PolyUHFParser.T__15)
                pass

            elif la_ == 7:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 8:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==9 or _la==11):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                self.match(PolyUHFParser.T__14)
                self.state = 166
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 167
                self.match(PolyUHFParser.T__1)
                self.state = 168
                self.expr()
                self.state = 169
                self.match(PolyUHFParser.T__16)
                self.state = 170
                self.expr()
                self.state = 171
                self.match(PolyUHFParser.T__16)
                self.state = 172
                self.expr()
                self.state = 173
                self.match(PolyUHFParser.T__15)
                self.state = 174
                self.match(PolyUHFParser.T__3)
                self.state = 175
                self.expr()
                self.state = 176
                self.match(PolyUHFParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





