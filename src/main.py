#!/usr/bin/env python3
# pyright: standard

import argparse
import sys

# from pprint import pprint
import colorama
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from codegen.formatter import tidy_and_format_c
from codegen.generator import generate_program
from helpers import Helpers
from ir.c.lower_imperative_ir import lower_imperative_program
from ir.imperative.lower_typed_ir import lower_typed_program
from ir.typed.lower_ast import lower_ast_program
from ir.types import LoweringError
from parsing.antlr.PolyUHFLexer import PolyUHFLexer
from parsing.antlr.PolyUHFParser import PolyUHFParser
from parsing.ast.ast_builder import ASTBuilder, DSLParseError
from settings import (
    ArbitraryPrime,
    BigIntConfiguration,
    BinaryField,
    CrandallPrime,
    PrimeField,
)


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
        # Settings/config

        # Build field object
        field = None
        match flags.field_type:
            case "prime":
                if flags.crandall:
                    pi, theta = map(int, flags.crandall)
                    prime = CrandallPrime(pi, theta)
                elif flags.arbitrary:
                    value = int(flags.arbitrary[0])
                    prime = ArbitraryPrime(value)
                else:
                    raise ValueError()
                field = PrimeField(prime)
            case "binary":
                field = BinaryField(int(flags.n))
        assert field, "invalid field"
        # pprint(field)

        # Deduce bigint configuration
        bigint_config = BigIntConfiguration.from_field(field)
        # pprint(bigint_config)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Settings")

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
        # pprint(c_ir)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] C nodes")

        # Codegen (pretty-printing)
        text = generate_program(c_ir)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Codegen")

        # Generate settings header
        config_header_path = "src/cpp/configuration.h"
        bigint_config.generate_header(config_header_path)
        print(
            f"[{Fore.GREEN}+{Style.RESET_ALL}] Wrote configuration "
            f'header to "{config_header_path}"'
        )

        # Generate add/mul/carry helpers
        helpers_path = "src/cpp/helpers.h"
        helpers = Helpers(bigint_config)
        helpers.generate_header(helpers_path)
        print(
            f"[{Fore.GREEN}+{Style.RESET_ALL}] Wrote add-mul helpers "
            f'header to "{helpers_path}"'
        )

        # Write code to file
        output_path = "src/cpp/library.h"
        with open(output_path, "w") as code_output:
            code_output.write(text)
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Wrote code to "{output_path}"')

        # Formatter
        if flags.format:
            tidy_and_format_c(output_path)
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Optional formatting")

        # Verbose output
        if flags.verbose:
            with open(output_path) as f:
                print("".join(f.readlines()))

        return text
    except (DSLParseError, LoweringError, AssertionError, RuntimeError) as e:
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

    # CL arguments
    cli = argparse.ArgumentParser(description="DSL Compiler")

    # File
    cli.add_argument("input_file", type=str, help="input file")

    # Verbosity
    cli.add_argument("--verbose", "-v", action="store_true", help="Show IR")

    # Post-processing
    cli.add_argument(
        "--format", "-f", action="store_true", help="Format using clang-tidy"
    )

    # Subcommands for field selection
    subparsers = cli.add_subparsers(
        dest="field_type", required=True, help="Field type: prime or binary"
    )

    # Prime field subparser
    prime_parser = subparsers.add_parser("prime", help="Prime field GF(p)")
    prime_group = prime_parser.add_mutually_exclusive_group(required=True)
    prime_group.add_argument(
        "--crandall",
        nargs=2,
        type=int,
        metavar=("PI", "THETA"),
        help="Crandall prime: 2^PI - THETA",
    )
    prime_group.add_argument(
        "--arbitrary", nargs=1, type=int, metavar="VALUE", help="Arbitrary prime p"
    )

    # Binary field subparser
    binary_parser = subparsers.add_parser("binary", help="Binary field GF(2^n)")
    binary_parser.add_argument("n", type=int, help="Exponent n for GF(2^n)")
    flags = cli.parse_args()

    program = compile_file(flags.input_file, flags)
