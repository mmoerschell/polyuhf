from antlr4 import CommonTokenStream, InputStream

from parsing.ast.ast_builder import ASTBuilder

from .PolyUHFLexer import PolyUHFLexer
from .PolyUHFParser import PolyUHFParser


def parse_string(text: str):
    input_stream = InputStream(text)
    lexer = PolyUHFLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PolyUHFParser(token_stream)
    syntax_tree = parser.program()  # first rule to apply
    # print(syntax_tree.toStringTree(recog=parser))

    builder = ASTBuilder()
    ast = builder.visit(syntax_tree)
    # pprint(ast)

    return ast


def parse_file(path: str):
    with open(path, mode="r", encoding="utf-8") as f:
        return parse_string(f.read())
