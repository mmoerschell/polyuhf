from antlr4 import CommonTokenStream, InputStream

from parsing.ast.ast_builder import ASTBuilder
from parsing.ir.lower import lower_program
from parsing.ir.nodes import IRProgram

from .PolyUHFLexer import PolyUHFLexer
from .PolyUHFParser import PolyUHFParser


def parse_string(text: str) -> IRProgram:
    input_stream = InputStream(text)
    lexer = PolyUHFLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PolyUHFParser(token_stream)

    # 1. Parse tree
    parse_tree = parser.program()  # first rule to apply
    # print(parse_tree.toStringTree(recog=parser))

    # 2. Abstract Syntax tree
    builder = ASTBuilder()
    ast = builder.visit(parse_tree)
    # pprint(ast)

    # 3. IR
    ir = lower_program(ast)

    return ir


def parse_file(path: str) -> IRProgram:
    with open(path, mode="r", encoding="utf-8") as f:
        return parse_string(f.read())
