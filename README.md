# Pruebas de Precedencia y Asociatividad

## Introducción

Este proyecto implementa un analizador de expresiones aritméticas usando ANTLR4 y el patrón Visitor en Python. Se desarrollaron dos versiones de la gramática para comparar cómo cambian los resultados cuando se modifica la precedencia y la asociatividad de los operadores.

## Descripción

El sistema recibe expresiones matemáticas que contienen números, paréntesis y operadores (+, -, *, /). La primera gramática respeta la precedencia tradicional (multiplicación/división antes que suma/resta y asociatividad izquierda). La segunda invierte la precedencia (suma/resta antes que multiplicación/división y asociatividad derecha). De esta manera se evidencian las diferencias en la evaluación de las mismas cadenas de prueba.

## Desarrollo de la actividad

- Se definieron dos gramáticas en ANTLR4: la original y la rediseñada.

- Se generaron los analizadores léxicos y sintácticos en Python usando el target de ANTLR.

- Se implementaron dos visitantes (uno por versión) para recorrer el árbol sintáctico y calcular el valor de cada expresión.

- Se probaron expresiones de ejemplo como 2+3*4, 2-3-4 y 2+3*(4-5) para comparar los resultados bajo ambas gramáticas.

## Conclusiones

- La precedencia de los operadores define qué operaciones se realizan primero en ausencia de paréntesis.

- La asociatividad cambia el resultado en operaciones no conmutativas como la resta.

- Al modificar la gramática, se pueden obtener resultados distintos para las mismas expresiones, lo que demuestra la importancia del diseño gramatical.

- Los paréntesis siguen siendo el recurso más seguro para controlar la evaluación y evitar ambigüedad.
