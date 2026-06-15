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
        4,1,35,202,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,1,1,1,
        3,1,42,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,68,8,4,10,4,12,4,71,
        9,4,3,4,73,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,84,8,5,10,
        5,12,5,87,9,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,3,
        9,101,8,9,1,10,1,10,1,11,1,11,1,11,5,11,108,8,11,10,11,12,11,111,
        9,11,1,12,1,12,1,12,5,12,116,8,12,10,12,12,12,119,9,12,1,13,1,13,
        1,13,3,13,124,8,13,1,14,1,14,1,14,3,14,129,8,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,155,8,15,1,15,1,15,1,
        15,3,15,160,8,15,1,15,1,15,1,15,3,15,165,8,15,1,15,1,15,1,15,1,15,
        1,15,5,15,172,8,15,10,15,12,15,175,9,15,3,15,177,8,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,3,15,200,8,15,1,15,0,0,16,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,0,6,1,0,22,23,1,0,21,23,1,0,24,
        29,1,0,6,7,1,0,8,10,2,0,6,6,8,8,208,0,33,1,0,0,0,2,41,1,0,0,0,4,
        43,1,0,0,0,6,52,1,0,0,0,8,61,1,0,0,0,10,80,1,0,0,0,12,90,1,0,0,0,
        14,92,1,0,0,0,16,94,1,0,0,0,18,96,1,0,0,0,20,102,1,0,0,0,22,104,
        1,0,0,0,24,112,1,0,0,0,26,123,1,0,0,0,28,125,1,0,0,0,30,199,1,0,
        0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,37,1,0,0,0,37,38,5,0,0,1,38,1,1,0,0,0,39,42,3,4,2,0,40,
        42,3,8,4,0,41,39,1,0,0,0,41,40,1,0,0,0,42,3,1,0,0,0,43,44,5,16,0,
        0,44,45,5,32,0,0,45,46,5,1,0,0,46,47,3,6,3,0,47,48,5,2,0,0,48,49,
        5,3,0,0,49,50,3,16,8,0,50,51,5,4,0,0,51,5,1,0,0,0,52,53,5,32,0,0,
        53,54,5,21,0,0,54,55,5,5,0,0,55,56,5,32,0,0,56,57,5,21,0,0,57,58,
        5,5,0,0,58,59,5,32,0,0,59,60,5,23,0,0,60,7,1,0,0,0,61,62,5,15,0,
        0,62,63,5,32,0,0,63,72,5,1,0,0,64,69,3,10,5,0,65,66,5,5,0,0,66,68,
        3,10,5,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,
        70,73,1,0,0,0,71,69,1,0,0,0,72,64,1,0,0,0,72,73,1,0,0,0,73,74,1,
        0,0,0,74,75,5,2,0,0,75,76,3,12,6,0,76,77,5,3,0,0,77,78,3,16,8,0,
        78,79,5,4,0,0,79,9,1,0,0,0,80,85,5,32,0,0,81,82,5,5,0,0,82,84,5,
        32,0,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,
        88,1,0,0,0,87,85,1,0,0,0,88,89,3,14,7,0,89,11,1,0,0,0,90,91,7,0,
        0,0,91,13,1,0,0,0,92,93,7,1,0,0,93,15,1,0,0,0,94,95,3,18,9,0,95,
        17,1,0,0,0,96,100,3,22,11,0,97,98,3,20,10,0,98,99,3,22,11,0,99,101,
        1,0,0,0,100,97,1,0,0,0,100,101,1,0,0,0,101,19,1,0,0,0,102,103,7,
        2,0,0,103,21,1,0,0,0,104,109,3,24,12,0,105,106,7,3,0,0,106,108,3,
        24,12,0,107,105,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,
        1,0,0,0,110,23,1,0,0,0,111,109,1,0,0,0,112,117,3,26,13,0,113,114,
        7,4,0,0,114,116,3,26,13,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,25,1,0,0,0,119,117,1,0,0,0,120,121,5,
        7,0,0,121,124,3,26,13,0,122,124,3,28,14,0,123,120,1,0,0,0,123,122,
        1,0,0,0,124,27,1,0,0,0,125,128,3,30,15,0,126,127,5,11,0,0,127,129,
        3,28,14,0,128,126,1,0,0,0,128,129,1,0,0,0,129,29,1,0,0,0,130,131,
        5,1,0,0,131,132,3,16,8,0,132,133,5,2,0,0,133,200,1,0,0,0,134,135,
        5,17,0,0,135,136,3,16,8,0,136,137,5,3,0,0,137,138,3,16,8,0,138,139,
        5,4,0,0,139,140,5,19,0,0,140,141,5,3,0,0,141,142,3,16,8,0,142,143,
        5,4,0,0,143,200,1,0,0,0,144,145,5,18,0,0,145,146,3,16,8,0,146,147,
        5,3,0,0,147,148,3,16,8,0,148,154,5,4,0,0,149,150,5,19,0,0,150,151,
        5,3,0,0,151,152,3,16,8,0,152,153,5,4,0,0,153,155,1,0,0,0,154,149,
        1,0,0,0,154,155,1,0,0,0,155,200,1,0,0,0,156,159,5,30,0,0,157,158,
        5,20,0,0,158,160,3,14,7,0,159,157,1,0,0,0,159,160,1,0,0,0,160,200,
        1,0,0,0,161,164,5,31,0,0,162,163,5,20,0,0,163,165,3,14,7,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,200,1,0,0,0,166,167,5,32,0,0,167,176,
        5,1,0,0,168,173,3,16,8,0,169,170,5,5,0,0,170,172,3,16,8,0,171,169,
        1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,177,
        1,0,0,0,175,173,1,0,0,0,176,168,1,0,0,0,176,177,1,0,0,0,177,178,
        1,0,0,0,178,200,5,2,0,0,179,180,5,32,0,0,180,181,5,12,0,0,181,182,
        3,16,8,0,182,183,5,13,0,0,183,200,1,0,0,0,184,200,5,32,0,0,185,186,
        7,5,0,0,186,187,5,12,0,0,187,188,5,32,0,0,188,189,5,5,0,0,189,190,
        3,16,8,0,190,191,5,14,0,0,191,192,3,16,8,0,192,193,5,14,0,0,193,
        194,3,16,8,0,194,195,5,13,0,0,195,196,5,3,0,0,196,197,3,16,8,0,197,
        198,5,4,0,0,198,200,1,0,0,0,199,130,1,0,0,0,199,134,1,0,0,0,199,
        144,1,0,0,0,199,156,1,0,0,0,199,161,1,0,0,0,199,166,1,0,0,0,199,
        179,1,0,0,0,199,184,1,0,0,0,199,185,1,0,0,0,200,31,1,0,0,0,16,35,
        41,69,72,85,100,109,117,123,128,154,159,164,173,176,199
    ]

class PolyUHFParser ( Parser ):

    grammarFileName = "PolyUHF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "','", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'**'", "'['", "']'", "':'", 
                     "'func'", "'hash'", "'if'", "'nctif'", "'else'", "'as'", 
                     "'buffer'", "'fieldelement'", "'index'", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FUNCTION", 
                      "HASH", "IF", "NCTIF", "ELSE", "AS", "BUFFER", "FIELDELEMENT", 
                      "INDEX", "EQ", "NEQ", "LE", "GE", "LT", "GT", "HEXADECIMAL", 
                      "DECIMAL", "IDENTIFIER", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_module = 0
    RULE_function = 1
    RULE_hash_function = 2
    RULE_hash_params = 3
    RULE_helper_function = 4
    RULE_param_group = 5
    RULE_helper_return_type = 6
    RULE_ttype = 7
    RULE_expr = 8
    RULE_comparisonExpr = 9
    RULE_compOp = 10
    RULE_addSubExpr = 11
    RULE_mulDivExpr = 12
    RULE_unaryMinusExpr = 13
    RULE_exponentExpr = 14
    RULE_primary = 15

    ruleNames =  [ "module", "function", "hash_function", "hash_params", 
                   "helper_function", "param_group", "helper_return_type", 
                   "ttype", "expr", "comparisonExpr", "compOp", "addSubExpr", 
                   "mulDivExpr", "unaryMinusExpr", "exponentExpr", "primary" ]

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
    FUNCTION=15
    HASH=16
    IF=17
    NCTIF=18
    ELSE=19
    AS=20
    BUFFER=21
    FIELDELEMENT=22
    INDEX=23
    EQ=24
    NEQ=25
    LE=26
    GE=27
    LT=28
    GT=29
    HEXADECIMAL=30
    DECIMAL=31
    IDENTIFIER=32
    WS=33
    LINE_COMMENT=34
    BLOCK_COMMENT=35

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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.function()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15 or _la==16):
                    break

            self.state = 37
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

        def hash_function(self):
            return self.getTypedRuleContext(PolyUHFParser.Hash_functionContext,0)


        def helper_function(self):
            return self.getTypedRuleContext(PolyUHFParser.Helper_functionContext,0)


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
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.hash_function()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.helper_function()
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


    class Hash_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(PolyUHFParser.HASH, 0)

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)

        def hash_params(self):
            return self.getTypedRuleContext(PolyUHFParser.Hash_paramsContext,0)


        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_hash_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHash_function" ):
                return visitor.visitHash_function(self)
            else:
                return visitor.visitChildren(self)




    def hash_function(self):

        localctx = PolyUHFParser.Hash_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_hash_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(PolyUHFParser.HASH)
            self.state = 44
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 45
            self.match(PolyUHFParser.T__0)
            self.state = 46
            self.hash_params()
            self.state = 47
            self.match(PolyUHFParser.T__1)
            self.state = 48
            self.match(PolyUHFParser.T__2)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(PolyUHFParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hash_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PolyUHFParser.IDENTIFIER)
            else:
                return self.getToken(PolyUHFParser.IDENTIFIER, i)

        def BUFFER(self, i:int=None):
            if i is None:
                return self.getTokens(PolyUHFParser.BUFFER)
            else:
                return self.getToken(PolyUHFParser.BUFFER, i)

        def INDEX(self):
            return self.getToken(PolyUHFParser.INDEX, 0)

        def getRuleIndex(self):
            return PolyUHFParser.RULE_hash_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHash_params" ):
                return visitor.visitHash_params(self)
            else:
                return visitor.visitChildren(self)




    def hash_params(self):

        localctx = PolyUHFParser.Hash_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_hash_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 53
            self.match(PolyUHFParser.BUFFER)
            self.state = 54
            self.match(PolyUHFParser.T__4)
            self.state = 55
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 56
            self.match(PolyUHFParser.BUFFER)
            self.state = 57
            self.match(PolyUHFParser.T__4)
            self.state = 58
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 59
            self.match(PolyUHFParser.INDEX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Helper_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PolyUHFParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(PolyUHFParser.IDENTIFIER, 0)

        def helper_return_type(self):
            return self.getTypedRuleContext(PolyUHFParser.Helper_return_typeContext,0)


        def expr(self):
            return self.getTypedRuleContext(PolyUHFParser.ExprContext,0)


        def param_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.Param_groupContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.Param_groupContext,i)


        def getRuleIndex(self):
            return PolyUHFParser.RULE_helper_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelper_function" ):
                return visitor.visitHelper_function(self)
            else:
                return visitor.visitChildren(self)




    def helper_function(self):

        localctx = PolyUHFParser.Helper_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_helper_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(PolyUHFParser.FUNCTION)
            self.state = 62
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 63
            self.match(PolyUHFParser.T__0)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 64
                self.param_group()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 65
                    self.match(PolyUHFParser.T__4)
                    self.state = 66
                    self.param_group()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 74
            self.match(PolyUHFParser.T__1)
            self.state = 75
            self.helper_return_type()
            self.state = 76
            self.match(PolyUHFParser.T__2)
            self.state = 77
            self.expr()
            self.state = 78
            self.match(PolyUHFParser.T__3)
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
        self.enterRule(localctx, 10, self.RULE_param_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(PolyUHFParser.IDENTIFIER)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 81
                self.match(PolyUHFParser.T__4)
                self.state = 82
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.ttype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Helper_return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIELDELEMENT(self):
            return self.getToken(PolyUHFParser.FIELDELEMENT, 0)

        def INDEX(self):
            return self.getToken(PolyUHFParser.INDEX, 0)

        def getRuleIndex(self):
            return PolyUHFParser.RULE_helper_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelper_return_type" ):
                return visitor.visitHelper_return_type(self)
            else:
                return visitor.visitChildren(self)




    def helper_return_type(self):

        localctx = PolyUHFParser.Helper_return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_helper_return_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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


    class TtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BUFFER(self):
            return self.getToken(PolyUHFParser.BUFFER, 0)

        def FIELDELEMENT(self):
            return self.getToken(PolyUHFParser.FIELDELEMENT, 0)

        def INDEX(self):
            return self.getToken(PolyUHFParser.INDEX, 0)

        def getRuleIndex(self):
            return PolyUHFParser.RULE_ttype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTtype" ):
                return visitor.visitTtype(self)
            else:
                return visitor.visitChildren(self)




    def ttype(self):

        localctx = PolyUHFParser.TtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ttype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
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
        self.enterRule(localctx, 18, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.SingleCompareContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.addSubExpr()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0):
                self.state = 97
                self.compOp()
                self.state = 98
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
        self.enterRule(localctx, 20, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
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
            self._tset222 = None # Token
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
        self.enterRule(localctx, 22, self.RULE_addSubExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.AddSubContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.mulDivExpr()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 105
                localctx._tset222 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx._tset222 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset222)
                self.state = 106
                self.mulDivExpr()
                self.state = 111
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
            self._tset253 = None # Token
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
        self.enterRule(localctx, 24, self.RULE_mulDivExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.MulDivContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.unaryMinusExpr()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 113
                localctx._tset253 = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                    localctx._tset253 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.op.append(localctx._tset253)
                self.state = 114
                self.unaryMinusExpr()
                self.state = 119
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
        self.enterRule(localctx, 26, self.RULE_unaryMinusExpr)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PolyUHFParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(PolyUHFParser.T__6)
                self.state = 121
                self.unaryMinusExpr()
                pass
            elif token in [1, 6, 8, 17, 18, 30, 31, 32]:
                localctx = PolyUHFParser.UnaryAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 122
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
        self.enterRule(localctx, 28, self.RULE_exponentExpr)
        self._la = 0 # Token type
        try:
            localctx = PolyUHFParser.ExponentContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.primary()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 126
                self.match(PolyUHFParser.T__10)
                self.state = 127
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



    class NctIfExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PolyUHFParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NCTIF(self):
            return self.getToken(PolyUHFParser.NCTIF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyUHFParser.ExprContext)
            else:
                return self.getTypedRuleContext(PolyUHFParser.ExprContext,i)

        def ELSE(self):
            return self.getToken(PolyUHFParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNctIfExpr" ):
                return visitor.visitNctIfExpr(self)
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


    class CtIfElseExprContext(PrimaryContext):

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
            if hasattr( visitor, "visitCtIfElseExpr" ):
                return visitor.visitCtIfElseExpr(self)
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
        self.enterRule(localctx, 30, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = PolyUHFParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(PolyUHFParser.T__0)
                self.state = 131
                self.expr()
                self.state = 132
                self.match(PolyUHFParser.T__1)
                pass

            elif la_ == 2:
                localctx = PolyUHFParser.CtIfElseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(PolyUHFParser.IF)
                self.state = 135
                self.expr()
                self.state = 136
                self.match(PolyUHFParser.T__2)
                self.state = 137
                self.expr()
                self.state = 138
                self.match(PolyUHFParser.T__3)
                self.state = 139
                self.match(PolyUHFParser.ELSE)
                self.state = 140
                self.match(PolyUHFParser.T__2)
                self.state = 141
                self.expr()
                self.state = 142
                self.match(PolyUHFParser.T__3)
                pass

            elif la_ == 3:
                localctx = PolyUHFParser.NctIfExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.match(PolyUHFParser.NCTIF)
                self.state = 145
                self.expr()
                self.state = 146
                self.match(PolyUHFParser.T__2)
                self.state = 147
                self.expr()
                self.state = 148
                self.match(PolyUHFParser.T__3)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 149
                    self.match(PolyUHFParser.ELSE)
                    self.state = 150
                    self.match(PolyUHFParser.T__2)
                    self.state = 151
                    self.expr()
                    self.state = 152
                    self.match(PolyUHFParser.T__3)


                pass

            elif la_ == 4:
                localctx = PolyUHFParser.HexadecimalExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(PolyUHFParser.HEXADECIMAL)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 157
                    self.match(PolyUHFParser.AS)
                    self.state = 158
                    self.ttype()


                pass

            elif la_ == 5:
                localctx = PolyUHFParser.DecimalExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.match(PolyUHFParser.DECIMAL)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 162
                    self.match(PolyUHFParser.AS)
                    self.state = 163
                    self.ttype()


                pass

            elif la_ == 6:
                localctx = PolyUHFParser.CallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 166
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 167
                self.match(PolyUHFParser.T__0)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7516586434) != 0):
                    self.state = 168
                    self.expr()
                    self.state = 173
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 169
                        self.match(PolyUHFParser.T__4)
                        self.state = 170
                        self.expr()
                        self.state = 175
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 178
                self.match(PolyUHFParser.T__1)
                pass

            elif la_ == 7:
                localctx = PolyUHFParser.BufferViewReadExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 179
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 180
                self.match(PolyUHFParser.T__11)
                self.state = 181
                self.expr()
                self.state = 182
                self.match(PolyUHFParser.T__12)
                pass

            elif la_ == 8:
                localctx = PolyUHFParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 184
                self.match(PolyUHFParser.IDENTIFIER)
                pass

            elif la_ == 9:
                localctx = PolyUHFParser.ReductionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 185
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==8):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.match(PolyUHFParser.T__11)
                self.state = 187
                self.match(PolyUHFParser.IDENTIFIER)
                self.state = 188
                self.match(PolyUHFParser.T__4)
                self.state = 189
                self.expr()
                self.state = 190
                self.match(PolyUHFParser.T__13)
                self.state = 191
                self.expr()
                self.state = 192
                self.match(PolyUHFParser.T__13)
                self.state = 193
                self.expr()
                self.state = 194
                self.match(PolyUHFParser.T__12)
                self.state = 195
                self.match(PolyUHFParser.T__2)
                self.state = 196
                self.expr()
                self.state = 197
                self.match(PolyUHFParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





