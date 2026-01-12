#!/usr/bin/env python3

import argparse

from parsing.frontend import parse_file

if __name__ == "__main__":
    cli = argparse.ArgumentParser(description="Polynomial Universal Hash Functions")
    cli.add_argument("input", type=str, help="input file")
    args = cli.parse_args()

    program = parse_file(args.input)
    print(program)
