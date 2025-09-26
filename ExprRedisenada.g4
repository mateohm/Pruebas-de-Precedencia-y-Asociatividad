grammar ExprRedisenada;


prog: expr EOF;


// expr: multiplicación (menor precedencia)
expr
: expr ('*'|'/') term # mulDiv
| term # onlyTerm
;


// term: suma/resta con mayor precedencia y recursión derecha
term
: factor ('+'|'-') term # addSubRightRec
| factor # onlyFactor
;


factor
: '(' expr ')'
| NUM
;


NUM : [0-9]+ ;
WS : [
]+ -> skip ;
