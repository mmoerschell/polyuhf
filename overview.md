# Overview

## (a) Intermediate Representation for UHFs

Following SPHGen’s structure, design an intermediate representation (IR) for UHFs that models common polynomial operations from paper.

1. Adapt current IR s.t. it better models UHFs
    - Main function with signature: (key, message, [length]) => tag, where key and message are in raw bytes
    - Admit other helper functions in int/bigint types?
    - Paper ops (field arithmetic)
    - Helper ops (for indices: +-/% etc.)
    - Expression-based and/or Imperative form?
    - (SymPy)
    - No control flow!
1. "The critical rule for your compiler: Do NOT lower reductions to loops before vectorization. This is the #1 thing that would cripple your pipeline."

## (b) Domain-Specific Language (DSL)

Define a domain specific language (DSL) to describe polynomial hash functions and implement the translation from DSL to IR.

1. Recycle & fine-tune current grammar
1. Make if-else ternary
1. Expression-based
1. Reductions
1. More types (e.g. raw bytes), generalize type-checking

## (c) Backend & codegen

Implement the backend that generates C/C++ code from the IR. Ideally, both ARM and x86 need to be targeted.

1. Scalar field arithmetic
    - Parameterize fields
    - Prime & binary fields
    - Pick appropriate limb sizes to stay in 16-byte territory
    - Karatsuba & schoolbook multiplication?
1. Vectorization of reductions!
    - Generalize?
    - Heuristics?
    - Abstract platform away
1. Unrolling (by a specific width > #lanes)
    - Multiple accumulators to remove dependencies
1. (arm-specific): smaller limb sizes for more lanes? better performance?
1. Have a look at OpenSSL asm

## (d) Automatic Verification via Symbolic Execution

Implement automatic verification via symbolic execution.

1. Have a look at SPH
1. SymPy ?
1. Make IR friendly for this

## (e) Performance Model

Automatically derive a performance model given a definition of a UHF and a target CPU.

1. Last but not least
1. Have a look at SPH

## Testing

1. End-to-end testing
1. Generalize/parameterize fields
    - A single program should work fine on all fields
1. Have a look at other (Polynomial) UHFs out in the wild
1. Aliasing issues on OPs

## Report

1. Structure
1. Boilerplate?

## Reproducible setup

1. Readme and some scripts
1. Point to tests

## Presentation

1. When?
1. Summary?
