#!/usr/bin/env python3

import argparse

from parsing.frontend import parse_file

if __name__ == "__main__":
    cli = argparse.ArgumentParser(description="DSL Compiler")
    cli.add_argument("input", type=str, help="input file")
    args = cli.parse_args()

    program = parse_file(args.input)
    print(program)
