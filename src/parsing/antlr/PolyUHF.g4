grammar PolyUHF;

// Parser rules

module
    : function+ EOF
    ;

function
    : hash_function
    | helper_function
    ;

hash_function
    : HASH IDENTIFIER '(' hash_params ')' '{' expr '}'
    ;

hash_params
    : IDENTIFIER BUFFER ',' IDENTIFIER BUFFER ',' IDENTIFIER INDEX
    ;

helper_function
    : FUNCTION IDENTIFIER '(' (param_group ( ',' param_group )*)? ')' helper_return_type '{' expr '}'
    ;

param_group
    : IDENTIFIER ( ',' IDENTIFIER )* ttype
    ;

helper_return_type
    : FIELDELEMENT
    | INDEX
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
HASH        : 'hash' ;
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
