from antlr4 import *
from ExprRedisenadaLexer import ExprRedisenadaLexer
from ExprRedisenadaParser import ExprRedisenadaParser
from eval_visitor_redisenada import EvalVisitorRedisenada


tests = [
    "2+3*4",
    "2+3+4",
    "2-3-4",
    "2*3+4",
    "2+3*(4-5)"
]

for s in tests:
    input_stream = InputStream(s)
    lexer = ExprRedisenadaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprRedisenadaParser(stream)
    tree = parser.prog()
    visitor = EvalVisitorRedisenada()
    result = visitor.visit(tree)
    print(f"{s} => {result}")

