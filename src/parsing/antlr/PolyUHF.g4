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
    : 'bufferview' '<' underlying=field_ttype ',' chunk_size=DECIMAL '>'    # BufferViewType
    | field_ttype                                                           # FieldType
    | INDEX                                                                 # IndexType
    ;

field_ttype
    : 'prime' '<' pi=DECIMAL ',' theta=DECIMAL '>'  # PrimeFieldType
    | 'binary' '<' DECIMAL '>'                      # BinaryFieldType
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
    : primary ('^' exponentExpr)?                           # Exponent
    ;

primary
    : '(' expr ')'                                                              # Parentheses
    | IF expr '{' expr '}' ELSE '{' expr '}'                                    # IfElseExpr
    | HEXADECIMAL (AS ttype)?                                                   # HexadecimalExpression
    | DECIMAL (AS ttype)?                                                       # DecimalExpr
    | IDENTIFIER '(' (expr (',' expr)*)? ')'                                    # CallExpr
    | IDENTIFIER '[' expr ']'                                                   # BufferViewReadExpr
    | IDENTIFIER                                                                # IdentifierExpression
    | op=('*' | '+') '[' IDENTIFIER ',' expr ':' expr ':' expr ']' '{' expr '}' # ReductionExpr
    ;

// Lexer rules

HASHFUNC    : 'hashfunc' ;
FUNCTION    : 'func' ;
IF          : 'if' ;
ELSE        : 'else' ;
AS          : 'as' ;
PADDING
    : 'zero'
    ;
ENDIANNESS
    : 'little'
    | 'big'
    ;
INDEX  : 'index' ;

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
