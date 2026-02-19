#!/usr/bin/env python3
# pyright: standard

import argparse
import sys
from pprint import pprint

import colorama
import objgraph
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from codegen.formatter import format_c_code
from codegen.generator import generate_program
from ir.c_like.lower_to_c_like import lower_hl_program
from ir.high_level.lower_ast import lower_ast_program
from ir.types import LoweringError
from parsing.antlr.PolyUHFLexer import PolyUHFLexer
from parsing.antlr.PolyUHFParser import PolyUHFParser
from parsing.ast.ast_builder import ASTBuilder, DSLParseError


class BailErrorListener(ErrorListener):
    # Raises an exception if anything goes south
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # noqa: N802, N803
        raise DSLParseError(f"line {line}:{column} {msg}")


def compile_string(text: str, flags):
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

        # 3. High-level IR
        hl_ir = lower_ast_program(ast)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] High-level IR complete")

        # objgraph.show_refs(hl_ir.functions, max_depth=100, filter=lambda x:isinstance(x, IRNode), filename="hl_ir.png")

        # 4. C-Like
        clike = lower_hl_program(hl_ir)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] C nodes generated")

        # 5. Codegen
        text = generate_program(clike)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Codegen completed")

        # 6. Formatter
        if flags.format:
            text = format_c_code(text)

        if flags.verbose:
            print(text)

        return text
    except (DSLParseError, LoweringError) as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] Compilation error: {e}",
            file=sys.stderr,
        )
        exit(1)


def compile_file(path: str, flags):
    with open(path, mode="r", encoding="utf-8") as f:
        return compile_string(f.read(), flags)


if __name__ == "__main__":
    colorama.init(autoreset=True)  # resets terminal color after each print
    cli = argparse.ArgumentParser(description="DSL Compiler")
    cli.add_argument("input", type=str, help="input file")
    cli.add_argument("--verbose", "-v", action="store_true", help="Show IR")
    cli.add_argument(
        "--format", "-f", action="store_true", help="Format using clang-tidy"
    )
    flags = cli.parse_args()

    program = compile_file(flags.input, flags)
