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

from analysis.graph import graphs
from analysis.opcount import opcount_and_traffic
from analysis.perf_benchmark import gather_cycles
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


def compile_string(  # noqa: C901
    text: str, flags: argparse.Namespace, module_name: str, settings: Settings
) -> None:
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

        # Opcount & memory traffic
        ops_and_traffic_per_function = opcount_and_traffic(ir, settings)
        if not ops_and_traffic_per_function:
            print(
                f"[{Fore.YELLOW}x{Style.RESET_ALL}] No ops/traffic "
                f"analysis for {module_name}"
            )
        else:
            ops, traffic, _ = ops_and_traffic_per_function
            if flags.verbose:
                print(
                    f"[{Fore.BLUE}i{Style.RESET_ALL}] {ir.funcs[0].name} has {ops} ops "
                    f"and {traffic} bytes of memory traffic"
                )

        # Codegen (pretty-printing & algorithms)
        gen = ModuleCodeGenerator(
            ir, settings, ops_and_traffic_per_function is not None
        )
        header, source, datastructures_h, datastructures_s, perf = gen.compile()
        if flags.verbose:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Codegen")

        # Write code to files
        written_files = []
        for name, ext, contents in [
            (f"{module_name}", "h", header),
            (f"{module_name}", "c", source),
            ("datastructures", "h", datastructures_h),
            ("datastructures", "c", datastructures_s),
        ] + ([(f"{module_name}_perf", "c", perf)] if perf else []):
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

        # Benchmark
        if ops_and_traffic_per_function:
            ops_expr, traffic_expr, B_symbol = ops_and_traffic_per_function  # noqa: N806
            data_B, data_cycles = gather_cycles(module_name, 8, 1200, 8)  # noqa: N806
            data_ops: list[float] = [ops_expr.evalf(subs={B_symbol: b}) for b in data_B]  # type: ignore
            # data_traffic = [traffic_expr.evalf(subs={B_symbol: b}) for b in data_B]
            data_traffic = [b * settings.field.chunk_size() for b in data_B]
            graphs(module_name, data_B, data_ops, data_traffic, data_cycles, settings)

    except NotImplementedError as e:
        raise e
    except (DSLParseError, TypeCheckingError, AssertionError, RuntimeError) as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] Compilation error: {e}",
            file=sys.stderr,
        )
        raise e
        exit(1)


def compile_file(
    path: str, module_name: str, flags: argparse.Namespace, settings: Settings
) -> None:

    # For debugging
    if flags.verbose:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Compiling '{path}'")

    with open(path, mode="r", encoding="utf-8") as f:
        compile_string(f.read(), flags, module_name, settings)


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

    # Extract progam name from path
    match = re.search(r"([^/\\]+)\.txt$", flags.input_file)
    assert match, "Can't find module name in path"
    module_name = match.group(1)
    if module_name in ["configuration", "helpers"]:
        raise ValueError("Illegal module name")

    vectorize = True
    settings = Settings(
        PrimeField(116, 3),
        18,
        "arm",
        64,
        64 if vectorize else None,
        2 if vectorize else None,
        4,
        "schoolbook",
    )

    # Compile
    module = compile_file(flags.input_file, module_name, flags, settings)
