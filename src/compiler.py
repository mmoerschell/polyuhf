#!/usr/bin/env python3
# pyright: standard

import argparse
import sys
from pathlib import Path

# from pprint import pprint
import colorama
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Style

from analysis.opcount import opcount_and_traffic
from automatic_tests.boost_cpp_emitter import BoostCppTestEmitter
from codegen.code_generator import ModuleCodeGenerator
from codegen.formatter import tidy_and_format_c
from ir.ir_builder import IRModuleBuilder
from ir.ir_pretty_printing import pprint_module
from parsing.antlr.PolyUHFLexer import PolyUHFLexer
from parsing.antlr.PolyUHFParser import PolyUHFParser
from parsing.ast.ast_builder import ASTBuilder, DSLParseError
from parsing.ast.ast_nodes import ASTModule
from settings import Settings
from typechecker import Typechecker, TypeCheckingError

GENERATED_DIR = Path("src/cpp/generated")


class BailErrorListener(ErrorListener):
    # Raises an exception if anything goes south
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # noqa: N802, N803
        raise DSLParseError(f"line {line}:{column} {msg}")


def compile_string(  # noqa: C901
    text: str, flags: argparse.Namespace, module_name: str, settings: Settings
):
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
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
        if not flags.quiet:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Parsing")

        # Abstract Syntax tree
        builder = ASTBuilder(settings)
        ast = builder.visit(parse_tree)
        assert ast, "AST generation failed"
        assert isinstance(ast, ASTModule), "AST root should be a module"
        # pprint(ast)
        if not flags.quiet:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] AST")

        # Type-checking
        tc = Typechecker(settings)
        signatures = tc.typecheck_module(ast)
        # pprint(ast)
        if not flags.quiet:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Type-checking")

        ir_builder = IRModuleBuilder(ast, module_name, signatures, settings)
        ir = ir_builder.compile()
        if not flags.quiet:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Intermediate Representation")
        if flags.show_ir:
            print(pprint_module(ir))

        # Opcount & memory traffic
        if flags.analysis:
            ops_and_traffic = opcount_and_traffic(ir, settings)
            if not ops_and_traffic:
                if not flags.quiet:
                    print(
                        f"[{Fore.YELLOW}x{Style.RESET_ALL}] Ops/traffic "
                        f"analysis impossible for {module_name}"
                    )
            else:
                ops, traffic, _ = ops_and_traffic
                if not flags.quiet:
                    print(
                        f"[{Fore.BLUE}i{Style.RESET_ALL}] "
                        f"{ir.funcs[0].name} has {ops} ops "
                        f"and {traffic} bytes of memory traffic"
                    )
        else:
            ops_and_traffic = None

        # Codegen (pretty-printing & algorithms)
        generate_perf = bool(
            ops_and_traffic is not None
            and getattr(flags, "generate_perf", flags.analysis)
        )
        gen = ModuleCodeGenerator(ir, settings, generate_perf)
        header, source, datastructures_h, datastructures_s, perf = gen.compile()
        if not flags.quiet:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Codegen")

        # Write code to files
        written_files = []
        for name, ext, contents in [
            (f"{module_name}", "h", header),
            (f"{module_name}", "c", source),
            ("datastructures", "h", datastructures_h),
            ("datastructures", "c", datastructures_s),
        ] + ([(f"{module_name}_perf", "c", perf)] if perf else []):
            output_path = GENERATED_DIR / f"{name}.{ext}"
            with open(output_path, "w") as code_output:
                code_output.write(contents)
            written_files.append(output_path)
            if not flags.quiet:
                print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Wrote code to "{output_path}"')

        # Formatter
        if flags.format:
            for output_path in written_files:
                tidy_and_format_c(output_path)
            if not flags.quiet:
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Optional formatting")

        # Automatic tests
        if flags.automatic_tests:
            emitter = BoostCppTestEmitter(module_name, settings, flags.test_size)
            cpp_source = emitter.generate(ast)
            tests_cpp_path = GENERATED_DIR / f"{module_name}_autotests.cpp"
            with open(tests_cpp_path, "w") as f:
                f.write(cpp_source)
                if not flags.quiet:
                    print(
                        f"[{Fore.GREEN}+{Style.RESET_ALL}] Wrote code"
                        f' to "{tests_cpp_path}"'
                    )

        return ops_and_traffic

    except NotImplementedError as e:
        raise e
    except (DSLParseError, TypeCheckingError, AssertionError, RuntimeError) as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] Compilation error: {e}",
            file=sys.stderr,
        )


def compile_file(
    path: str, module_name: str, flags: argparse.Namespace, settings: Settings
):

    # For debugging
    if not flags.quiet:
        print(f"[{Fore.BLUE}i{Style.RESET_ALL}] Compiling '{path}'")

    with open(path, mode="r", encoding="utf-8") as f:
        return compile_string(f.read(), flags, module_name, settings)


if __name__ == "__main__":
    colorama.init(autoreset=True, strip=False)  # resets terminal color after each print

    # CL arguments
    cli = argparse.ArgumentParser(description="DSL Compiler")
    cli.add_argument("input_file", type=str, help="input file")
    cli.add_argument(
        "--vectorize",
        "-v",
        action="store_true",
        help="Vectorize big integer operations",
    )
    cli.add_argument("--quiet", "-q", action="store_true", help="Only report errors")
    cli.add_argument("--show-ir", "-i", action="store_true", help="Show IR")
    cli.add_argument(
        "--format", "-f", action="store_true", help="Format using clang-tidy"
    )
    cli.add_argument(
        "--automatic_tests",
        "-t",
        action="store_true",
        help="Automatically generate tests",
    )
    cli.add_argument(
        "--analysis",
        "-a",
        action="store_true",
        help="Generate opcount metadata and perf harness when possible",
    )
    cli.add_argument(
        "--test-size",
        type=int,
        default=500,
        help="Number of generated Boost data cases for automatic tests",
    )
    cli.add_argument(
        "--delay-limb-realignment",
        choices=("partial", "full"),
        default="partial",
        help="Delay limb realignment partially or fully until final reduction",
    )
    cli.add_argument("pi", type=int, help="Pi")
    cli.add_argument("theta", type=int, help="Theta")
    cli.add_argument("platform", type=str, help="NEON/AVX2")
    cli.add_argument(
        "--karatsuba", "-k", action="store_true", help="Use Karatsuba multiplication"
    )
    cli.add_argument("unroll", type=int, help="Unrolling factor")
    flags = cli.parse_args()

    # Extract progam name from path
    module_name = Path(flags.input_file).stem
    settings = Settings(
        flags.pi,
        flags.theta,
        flags.vectorize,
        flags.platform,
        flags.karatsuba,
        flags.unroll,
        flags.delay_limb_realignment,
    )

    # Compile
    module = compile_file(flags.input_file, module_name, flags, settings)
