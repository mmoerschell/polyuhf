grammar PolyUHF;

// Parser rules

program
    : function+ EOF
    ;

function
    : FUNCTION IDENTIFIER '(' (param_group ( ',' param_group )*)? ')' type_annotation '{' expr '}'
    ;

type_annotation
    : BIGINT
    | INDEX
    ;

param_group
    : IDENTIFIER ( ',' IDENTIFIER )* type_annotation
    ;

expr
    : addSubExpr
    ;

addSubExpr
    : mulDivExpr ( ( '+' | '-' ) mulDivExpr )*      # AddSub
    ;

mulDivExpr
    : exponentExpr ( ( '*' | '/' ) exponentExpr )*  # MulDiv
    ;

exponentExpr
    : primary ('^' expr)?                           # Exponent
    ;

primary
    : '-' primary                                                               # UnaryMinus
    | '(' expr ')'                                                              # Parentheses
    | INT                                                                       # IntExpr
    | IDENTIFIER '(' (expr (',' expr)*)? ')'                                    # CallExpr
    | IDENTIFIER '[' expr ']'                                                   # ArrayExpr
    | IDENTIFIER                                                                # IdentifierExpression
    | op=('*' | '+') '[' IDENTIFIER ',' expr ':' expr ':' expr ']' '{' expr '}' # ReductionExpr
    ;

// Lexer rules

FUNCTION   : 'func' ;
BIGINT     : 'bigint' ;
INDEX      : 'index' ;
IDENTIFIER : [a-zA-Z] [a-zA-Z0-9_]* ;
INT        : [0-9]+ ;
WS         : [ \t\r\n]+ -> skip ;

// Comment rules

LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
