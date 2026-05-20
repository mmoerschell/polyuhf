#!/usr/bin/env python3
# pyright: standard

import argparse
import re
import sys

# from pprint import pprint
import colorama
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from codegen.code_generator import ModuleCodeGenerator
from codegen.formatter import tidy_and_format_c
from ir.ir_builder import IRModuleBuilder
from ir.ir_pretty_printing import pprint_module
from parsing.antlr.PolyUHFLexer import PolyUHFLexer
from parsing.antlr.PolyUHFParser import PolyUHFParser
from parsing.ast.ast_builder import ASTBuilder, DSLParseError
from parsing.ast.ast_nodes import ASTModule
from typechecker import TypeCheckingError, typecheck_module


class BailErrorListener(ErrorListener):
    # Raises an exception if anything goes south
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # noqa: N802, N803
        raise DSLParseError(f"line {line}:{column} {msg}")


def compile_string(text: str, flags, module_name: str):
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
        parse_tree = parser.module()  # first rule to apply
        # print(parse_tree.toStringTree(recog=parser))
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Parsing")

        # Abstract Syntax tree
        builder = ASTBuilder()
        ast = builder.visit(parse_tree)
        assert ast, "AST generation failed"
        assert isinstance(ast, ASTModule), "AST root should be a program"
        # pprint(ast)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] AST")

        # Vectorization, unrolling
        # TODO

        # Type-checking
        signatures = typecheck_module(ast)
        # pprint(ast)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Type-checking")

        ir_builder = IRModuleBuilder(
            ast, module_name, signatures, 4
        )  # TODO FIXME CONST
        ir = ir_builder.compile()
        if flags.verbose:
            print(pprint_module(ir))
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Intermediate Representation")

        # Codegen (pretty-printing & algorithms)
        gen = ModuleCodeGenerator(ir, "arm")  # TODO FIXME CONST
        header, source = gen.compile()
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Header & source")

        # Write code to files
        written_files = []
        for ext, contents in [("h", header), ("c", source)]:
            output_path = f"src/cpp/generated/{module_name}.{ext}"
            with open(output_path, "w") as code_output:
                code_output.write(contents)
            written_files.append(output_path)
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Wrote code to "{output_path}"')

        # Formatter
        if flags.format:
            for output_path in written_files:
                tidy_and_format_c(output_path)
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Optional formatting")

        # Verbose output
        if flags.verbose:
            for output_path in written_files:
                with open(output_path) as f:
                    print("".join(f.readlines()))

        return f"{header}\n{source}"
    except NotImplementedError as e:
        raise e
    except (DSLParseError, TypeCheckingError, AssertionError, RuntimeError) as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] Compilation error: {e}",
            file=sys.stderr,
        )
        raise e
        exit(1)


def compile_file(path: str, flags):
    # Extract progam name from path
    match = re.search(r"([^/\\]+)\.txt$", path)
    assert match, "Can't find module name in path"
    module_name = match.group(1)
    if module_name in ["configuration", "helpers"]:
        raise ValueError("Illegal module name")

    # For debugging
    print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Compiling '{path}'")

    with open(path, mode="r", encoding="utf-8") as f:
        return compile_string(f.read(), flags, module_name)


if __name__ == "__main__":
    colorama.init(autoreset=True)  # resets terminal color after each print

    # CL arguments
    cli = argparse.ArgumentParser(description="DSL Compiler")
    cli.add_argument("input_file", type=str, help="input file")
    cli.add_argument("--verbose", "-v", action="store_true", help="Show IR")
    cli.add_argument(
        "--format", "-f", action="store_true", help="Format using clang-tidy"
    )
    flags = cli.parse_args()

    module = compile_file(flags.input_file, flags)
