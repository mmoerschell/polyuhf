from antlr4 import CommonTokenStream, InputStream

from .PolyUHFLexer import PolyUHFLexer
from .PolyUHFParser import PolyUHFParser


def parse_string(text: str):
    input_stream = InputStream(text)
    lexer = PolyUHFLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PolyUHFParser(token_stream)
    tree = parser.program()  # first rule to apply
    print(tree.toStringTree(recog=parser))

    # TODO: AST
    # ast = ASTBuilderVisitor().visit(tree)

    return tree


def parse_file(path: str):
    with open(path, mode="r", encoding="utf-8") as f:
        return parse_string(f.read())
