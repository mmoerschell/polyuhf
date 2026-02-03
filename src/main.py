#!/usr/bin/env python3

import argparse
from pprint import pprint

import colorama

from parsing.frontend import parse_file

if __name__ == "__main__":
    colorama.init(autoreset=True)  # resets terminal color after each print
    cli = argparse.ArgumentParser(description="DSL Compiler")
    cli.add_argument("input", type=str, help="input file")
    cli.add_argument("--verbose", "-v", action="store_true", help="Show IR")
    args = cli.parse_args()

    irprogam = parse_file(args.input)
    if args.verbose:
        pprint(irprogam)
