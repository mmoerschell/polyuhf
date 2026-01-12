grammar PolyUHF;

program
    : function+ EOF
    ;

function
    : 'function' IDENTIFIER '(' (IDENTIFIER ( ',' IDENTIFIER )*)? ')' ':' expr
    ;

expr 
    : addExpr
    ;

addExpr
    : mulExpr ( '+' mulExpr )*     # Add
    ;

mulExpr
    : primary ( '*' primary )*     # Mul
    ;

primary
    : '(' expr ')'                                                              # Parentheses
    | INT                                                                       # IntExpr
    | IDENTIFIER                                                                # IdentifierExpression
    | IDENTIFIER '[' expr ']'                                                   # ArrayExpr
    | op=('*' | '+') '[' IDENTIFIER ',' expr ':' expr ':' expr ']' '{' expr '}' # ReductionExpr
    ;

IDENTIFIER : [a-zA-Z]+ ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
