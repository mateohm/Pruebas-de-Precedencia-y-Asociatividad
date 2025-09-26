grammar ExprOriginal;


prog: expr EOF;


expr
: expr ('+'|'-') expr # addSubLeftRec
| expr ('*'|'/') expr # mulDivLeftRec
| '(' expr ')' # parens
| NUM # number
;


NUM : [0-9]+ ;
WS : [
]+ -> skip ;
