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
from settings import Settings
from typechecker import TypeCheckingError, typecheck_module
from typesystem import PrimeField


class BailErrorListener(ErrorListener):
    # Raises an exception if anything goes south
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # noqa: N802, N803
        raise DSLParseError(f"line {line}:{column} {msg}")


def compile_string(text: str, flags, module_name: str, settings: Settings):  # noqa: C901
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
        if flags.verbose:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Parsing")

        # Abstract Syntax tree
        builder = ASTBuilder()
        ast = builder.visit(parse_tree)
        assert ast, "AST generation failed"
        assert isinstance(ast, ASTModule), "AST root should be a program"
        # pprint(ast)
        if flags.verbose:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] AST")

        # Type-checking
        signatures = typecheck_module(ast)
        # pprint(ast)
        if flags.verbose:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Type-checking")

        ir_builder = IRModuleBuilder(ast, module_name, signatures, settings)
        ir = ir_builder.compile()
        if flags.verbose:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Intermediate Representation")
        if flags.show_ir:
            print(pprint_module(ir))

        # Codegen (pretty-printing & algorithms)
        gen = ModuleCodeGenerator(ir, settings)
        header, source, datastructures_h, datastructures_s = gen.compile()
        if flags.verbose:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Codegen")

        # Write code to files
        written_files = []
        for name, ext, contents in [
            (f"{module_name}", "h", header),
            (f"{module_name}", "c", source),
            ("datastructures", "h", datastructures_h),
            ("datastructures", "c", datastructures_s),
        ]:
            output_path = f"src/cpp/generated/{name}.{ext}"
            with open(output_path, "w") as code_output:
                code_output.write(contents)
            written_files.append(output_path)
            if flags.verbose:
                print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Wrote code to "{output_path}"')

        # Formatter
        if flags.format:
            for output_path in written_files:
                tidy_and_format_c(output_path)
            if flags.verbose:
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Optional formatting")

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


def compile_file(path: str, flags, settings: Settings):
    # Extract progam name from path
    match = re.search(r"([^/\\]+)\.txt$", path)
    assert match, "Can't find module name in path"
    module_name = match.group(1)
    if module_name in ["configuration", "helpers"]:
        raise ValueError("Illegal module name")

    # For debugging
    if flags.verbose:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Compiling '{path}'")

    with open(path, mode="r", encoding="utf-8") as f:
        return compile_string(f.read(), flags, module_name, settings)


if __name__ == "__main__":
    colorama.init(autoreset=True, strip=False)  # resets terminal color after each print

    # CL arguments
    cli = argparse.ArgumentParser(description="DSL Compiler")
    cli.add_argument("input_file", type=str, help="input file")
    cli.add_argument("--verbose", "-v", action="store_true", help="Verbose")
    cli.add_argument("--show-ir", "-i", action="store_true", help="Show IR")
    cli.add_argument(
        "--format", "-f", action="store_true", help="Format using clang-tidy"
    )
    flags = cli.parse_args()

    vectorize = True
    if vectorize:
        settings = Settings(PrimeField(116, 3), 11, "arm", 64, 32, 4, "schoolbook", 4)
    else:
        settings = Settings(
            PrimeField(116, 3), 10, "arm", 32, None, None, "schoolbook", 4
        )
    module = compile_file(flags.input_file, flags, settings)
