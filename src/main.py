#!/usr/bin/env python3
# pyright: standard

import argparse
import re
import sys
import traceback

# from pprint import pprint
import colorama
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from codegen.formatter import tidy_and_format_c
from codegen.generator import generate_program
from field_configuration import BinaryField, FieldConfiguration, PrimeField
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


def compile_string(text: str, flags, program_name: str):
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

        # Set up field configuration
        field = None
        match flags.field_type:
            case "prime":
                field = PrimeField(int(flags.pi), int(flags.theta))
            case "binary":
                field = BinaryField(int(flags.n))
        assert field, "invalid field"
        field_configuration = FieldConfiguration.from_field(
            field, lambda_=int(flags.limb_size)
        )
        # pprint(field)
        # pprint(field_configuration)
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
        text = generate_program(c_ir, field_configuration)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Codegen")

        # Write code to file
        output_path = f"src/cpp/generated/{program_name}.h"
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
    except NotImplementedError as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] NotImplementedError {e}\n"
            f"{traceback.format_exc()}",
            file=sys.stderr,
        )
        exit(1)
    except (DSLParseError, LoweringError, AssertionError, RuntimeError) as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] Compilation error: {e}",
            file=sys.stderr,
        )
        exit(1)


def compile_file(path: str, flags):
    # Extract progam name from path
    match = re.search(r"([^/\\]+)\.txt$", path)
    assert match, "Can't find program name in path"
    program_name = match.group(1)
    if program_name in ["configuration", "helpers"]:
        raise ValueError("Illegal program name")

    with open(path, mode="r", encoding="utf-8") as f:
        return compile_string(f.read(), flags, program_name)


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
    subparsers = cli.add_subparsers(dest="field_type", required=True, help="Field type")

    # Optional global limb size request
    cli.add_argument(
        "--limb-size",
        "-l",
        type=int,
        default=22,
        help="Limb size in bits (default: 22)",
    )
    # Prime field subparser: usage -> prime <PI> <THETA>
    prime_parser = subparsers.add_parser("prime", help="Prime field GF(2^pi-theta)")
    prime_parser.add_argument("pi", type=int, help="Exponent pi")
    prime_parser.add_argument("theta", type=int, help="Subtrahend theta")

    # Binary field subparser: usage -> binary <N>
    binary_parser = subparsers.add_parser("binary", help="Binary field GF(2^n)")
    binary_parser.add_argument("n", type=int, help="Exponent n")
    flags = cli.parse_args()

    program = compile_file(flags.input_file, flags)
