grammar PolyUHF;

program
    : function+ EOF
    ;

function
    : FUNCTION IDENTIFIER '(' (IDENTIFIER ( ',' IDENTIFIER )*)? ')' ':' expr
    ;

expr
    : addSubExpr
    ;

addSubExpr
    : mulDivExpr ( ( '+' | '-' ) mulDivExpr )*  # AddSub
    ;

mulDivExpr
    : primary ( ( '*' | '/' ) primary )*        # MulDiv
    ;

primary
    : '-' primary                                                               # UnaryMinus
    | '(' expr ')'                                                              # Parentheses
    | INT                                                                       # IntExpr
    | IDENTIFIER                                                                # IdentifierExpression
    | IDENTIFIER '[' expr ']'                                                   # ArrayExpr
    | op=('*' | '+') '[' IDENTIFIER ',' expr ':' expr ':' expr ']' '{' expr '}' # ReductionExpr
    ;

FUNCTION   : 'function' ;
IDENTIFIER : [a-zA-Z] [a-zA-Z0-9_]* ;
INT        : [0-9]+ ;
WS         : [ \t\r\n]+ -> skip ;
