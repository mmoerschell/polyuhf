# Domain-Specific Language for Polynomial Universal Hash Functions

## Pipeline

1. DSL source code
1. Parse tree
1. Abstract syntax tree (AST)
1. Expression-based IR (typed DAG) <> Roundtrip to SymPy for algebraic optimizations
1. Imperative IR
1. C nodes IR
1. Codegen
1. Formatter (optional, for debugging)
