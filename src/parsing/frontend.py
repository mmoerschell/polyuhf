# pyright: standard
import sys

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from ir.high_level.lowering import LoweringError, lower_program
from ir.high_level.nodes import IRProgram
from parsing.antlr.PolyUHFLexer import PolyUHFLexer
from parsing.antlr.PolyUHFParser import PolyUHFParser
from parsing.ast.ast_builder import ASTBuilder, DSLParseError


class BailErrorListener(ErrorListener):
    # Raises exception if anything goes south
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # noqa: N802, N803
        raise DSLParseError(f"line {line}:{column} {msg}")


def parse_string(text: str) -> IRProgram:
    input_stream = InputStream(text)

    lexer = PolyUHFLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(BailErrorListener())

    token_stream = CommonTokenStream(lexer)

    parser = PolyUHFParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(BailErrorListener())

    try:
        # 1. Parse tree
        parse_tree = parser.program()  # first rule to apply
        # print(parse_tree.toStringTree(recog=parser))
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Parsing complete")

        # 2. Abstract Syntax tree
        builder = ASTBuilder()
        ast = builder.visit(parse_tree)
        # pprint(ast)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] AST complete")

        # 3. IR
        ir = lower_program(ast)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] IR complete")
        return ir
    except (DSLParseError, LoweringError) as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] Compilation error: {e}",
            file=sys.stderr,
        )
        exit(1)


def parse_file(path: str) -> IRProgram:
    with open(path, mode="r", encoding="utf-8") as f:
        return parse_string(f.read())
