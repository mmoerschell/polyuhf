#!/usr/bin/env python3

import argparse

# from pprint import pprint
from colorama import init

from parsing.frontend import parse_file

init(autoreset=True)  # resets terminal color after each print


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description="DSL Compiler")
    cli.add_argument("input", type=str, help="input file")
    args = cli.parse_args()

    irprogam = parse_file(args.input)
    # pprint(irprogam)
