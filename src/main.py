#!/usr/bin/env python3
# pyright: standard

import argparse
import sys
from pprint import pprint

import colorama
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from codegen.formatter import format_c_code
from codegen.generator import generate_program
from ir.c.lower_imperative_ir import lower_imperative_program
from ir.imperative.lower_typed_ir import lower_typed_program
from ir.typed.lower_ast import lower_ast_program
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
        # Parse tree
        parse_tree = parser.program()  # first rule to apply
        # print(parse_tree.toStringTree(recog=parser))
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Parsing")

        # Abstract Syntax tree
        builder = ASTBuilder()
        ast = builder.visit(parse_tree)
        # pprint(ast)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] AST")

        # Typed IR
        typed_ir = lower_ast_program(ast)  # type: ignore
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Typed IR")

        # Imperative IR
        imperative_ir = lower_typed_program(typed_ir)
        # pprint(imperative_ir)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Imperative IR")

        # C IR
        c_ir = lower_imperative_program(imperative_ir)
        pprint(c_ir)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] C nodes")

        # Codegen (pretty-printing)
        text = generate_program(c_ir)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Codegen")

        # Formatter
        if flags.format:
            text = format_c_code(text)
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Optional formatting")

        # Verbose output
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
