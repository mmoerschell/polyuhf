grammar PolyUHF;

program
    : expr EOF
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
    | VARIABLE                     # VariableExpr
    | INT                          # IntExpr
    ;

reduction
    : op=('*' | '+')
      '[' VARIABLE ',' expr ':' expr ':' expr ']'
      '{' expr '}'
    ;

array
    : VARIABLE '[' expr ']'
    ;

VARIABLE : [a-zA-Z]+ ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
