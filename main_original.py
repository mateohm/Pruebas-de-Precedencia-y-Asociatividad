from antlr4 import *
from ExprOriginalLexer import ExprOriginalLexer
from ExprOriginalParser import ExprOriginalParser
from eval_visitor_original import EvalVisitorOriginal


tests = [
    "2+3*4",
    "2+3+4",
    "2-3-4",
    "2*3+4",
    "2+3*(4-5)"
]

for s in tests:
    input_stream = InputStream(s)
    lexer = ExprOriginalLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprOriginalParser(stream)
    tree = parser.prog()
    visitor = EvalVisitorOriginal()
    result = visitor.visit(tree)
    print(f"{s} => {result}")
