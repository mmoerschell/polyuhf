from antlr4 import InputStream, CommonTokenStream
from PolyUHFLexer import PolyUHFLexer
from PolyUHFParser import PolyUHFParser

def parse_program(text: str):
    input_stream = InputStream(text)
    lexer = PolyUHFLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PolyUHFParser(token_stream)
    tree = parser.program()  # first rule to apply
    print(tree.toStringTree(recog=parser))

    # TODO: AST
    # ast = ASTBuilderVisitor().visit(tree)

    return tree


if __name__ == "__main__":
    with open("nmh_simple.txt", "r", encoding="utf-8") as f:
        text = f.read()
    parse_program(text)
