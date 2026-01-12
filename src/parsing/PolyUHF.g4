grammar PolyUHF;

program
    : function+ EOF
    ;

function
    : 'function' IDENTIFIER '(' IDENTIFIER ( ',' IDENTIFIER )* ')' ':' expr
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
    : '(' expr ')'                 # Parentheses
    | reduction                    # ReductionExpr
    | array                        # ArrayExpr
    | IDENTIFIER                   # IdentifierExpression
    | INT                          # IntExpr
    ;

reduction
    : op=('*' | '+')
      '[' IDENTIFIER ',' expr ':' expr ':' expr ']'
      '{' expr '}'
    ;

array
    : IDENTIFIER '[' expr ']'
    ;

IDENTIFIER : [a-zA-Z]+ ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
