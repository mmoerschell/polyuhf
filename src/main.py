#!/usr/bin/env python3

import argparse
from parsing.frontend import parse_program

if __name__ == "__main__":
    cli = argparse.ArgumentParser(description="Polynomial Universal Hash Functions")
    cli.add_argument("input", type=str, help="input file")
    args = cli.parse_args()

    with open(args.input, mode="r", encoding="utf-8") as f:
        input = f.read()
    
    program = parse_program(input)
    print(program)
