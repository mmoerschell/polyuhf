grammar PolyUHF;

// Parser rules

program
    : function+ EOF
    ;

function
    : FUNCTION IDENTIFIER '(' (param_group ( ',' param_group )*)? ')' type_annotation '{' expr '}'
    ;

type_annotation
    : TYPE_ANNOTATION
    ;

param_group
    : IDENTIFIER ( ',' IDENTIFIER )* type_annotation
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
    : unaryMinusExpr ( op+=( '*' | '/' ) unaryMinusExpr )*  # MulDiv
    ;

unaryMinusExpr
    : '-' unaryMinusExpr                                    # UnaryMinus
    | exponentExpr                                          # UnaryAtom
    ;

exponentExpr
    : primary ('^' exponentExpr)?                           # Exponent
    ;

primary
    : '(' expr ')'                                                              # Parentheses
    | IF expr '{' expr '}' ELSE '{' expr '}'                                    # IfElseExpr
    | HEX_BIGINT                                                                # HexBigIntExpr
    | DEC_BIGINT                                                                # DecBigIntExpr
    | HEX_INT                                                                   # HexIntExpr
    | DEC_INT                                                                   # DecIntExpr
    | IDENTIFIER '(' (expr (',' expr)*)? ')'                                    # CallExpr
    | IDENTIFIER '[' expr ']'                                                   # ArrayExpr
    | IDENTIFIER                                                                # IdentifierExpression
    | op=('*' | '+') '[' IDENTIFIER ',' expr ':' expr ':' expr ']' '{' expr '}' # ReductionExpr
    ;

// Lexer rules

FUNCTION    : 'func' ;
IF          : 'if' ;
ELSE        : 'else' ;
TYPE_ANNOTATION
    : '[' DEC_INT? ']' (TYPE_BIGINT | TYPE_INDEX)
    | TYPE_BIGINT
    | TYPE_INDEX
    ;
TYPE_BIGINT : 'bigint' ;
TYPE_INDEX  : 'index' ;

EQ  : '==';
NEQ : '!=';
LE  : '<=';
GE  : '>=';
LT  : '<';
GT  : '>';

// Bigint literals

HEX_BIGINT : '0x' [0-9a-fA-F]+ ('L' | 'l') ;
DEC_BIGINT : [0-9]+ ('L' | 'l') ;

// Index literals
HEX_INT : '0x' [0-9a-fA-F]+ ;
DEC_INT : [0-9]+ ;

// Identifiers
IDENTIFIER  : [a-zA-Z] [a-zA-Z0-9_]* ;

WS          : [ \t\r\n]+ -> skip ;

// Comment rules

LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
