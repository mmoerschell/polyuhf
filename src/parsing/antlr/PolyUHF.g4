grammar PolyUHF;

// Parser rules

module
    : function+ EOF
    ;

function
    : FUNCTION IDENTIFIER '(' (param_group ( ',' param_group )*)? ')' ttype '{' expr '}'
    ;

param_group
    : IDENTIFIER ( ',' IDENTIFIER )* ttype
    ;

ttype
    : BUFFER
    | FIELDELEMENT
    | INDEX
    ;

expr
    : comparisonExpr
    ;

comparisonExpr
    : addSubExpr (compOp addSubExpr)?                       # SingleCompare
    ;

compOp
    : EQ | NEQ | LE | GE | LT | GT
    ;

addSubExpr
    : mulDivExpr ( op+=( '+' | '-' ) mulDivExpr )*          # AddSub
    ;

mulDivExpr
    : unaryMinusExpr ( op+=( '*' | '/' | '%' ) unaryMinusExpr )*  # MulDiv
    ;

unaryMinusExpr
    : '-' unaryMinusExpr                                    # UnaryMinus
    | exponentExpr                                          # UnaryAtom
    ;

exponentExpr
    : primary ('**' exponentExpr)?                           # Exponent
    ;

primary
    : '(' expr ')'                                                              # Parentheses
    | IF expr '{' expr '}' ELSE '{' expr '}'                                    # CtIfElseExpr
    | NCTIF expr '{' expr '}' (ELSE '{' expr '}')?                              # NctIfExpr
    | HEXADECIMAL (AS ttype)?                                                   # HexadecimalExpression
    | DECIMAL (AS ttype)?                                                       # DecimalExpr
    | IDENTIFIER '(' (expr (',' expr)*)? ')'                                    # CallExpr
    | IDENTIFIER '[' expr ']'                                                   # BufferViewReadExpr
    | IDENTIFIER                                                                # IdentifierExpression
    | op=('*' | '+') '[' IDENTIFIER ',' expr ':' expr ':' expr ']' '{' expr '}' # ReductionExpr
    ;

// Lexer rules

FUNCTION    : 'func' ;
IF          : 'if' ;
NCTIF       : 'nctif' ;
ELSE        : 'else' ;
AS          : 'as' ;

BUFFER       : 'buffer' ;
FIELDELEMENT : 'fieldelement' ;
INDEX        : 'index' ;

EQ  : '==';
NEQ : '!=';
LE  : '<=';
GE  : '>=';
LT  : '<';
GT  : '>';

// Numeric literals
HEXADECIMAL : '0x' [0-9a-fA-F]+ ;
DECIMAL : [0-9]+ ;

// Identifiers
IDENTIFIER  : [a-zA-Z] [a-zA-Z0-9_]* ;

WS          : [ \t\r\n]+ -> skip ;

// Comment rules

LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
