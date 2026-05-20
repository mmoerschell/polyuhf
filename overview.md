# Overview

## (a) Intermediate Representation for UHFs

Following SPHGen’s structure, design an intermediate representation (IR) for UHFs that models common polynomial operations from paper.

1. Do NOT lower reductions to loops before vectorization
1. Finalize IR levels & lowering

## (b) Domain-Specific Language (DSL)

Define a domain specific language (DSL) to describe polynomial hash functions and implement the translation from DSL to IR.

1. Make if-else ternary
1. Add casts for constants, e.g. field<...>(42)

## (c) Backend & codegen

Implement the backend that generates C/C++ code from the IR. Ideally, both ARM and x86 need to be targeted.

1. Scalar field arithmetic
    - Parameterize fields
    - Prime & binary fields
    - Pick appropriate limb sizes to stay in 16-byte territory
    - Karatsuba & schoolbook multiplication?
1. Vectorization of reductions!
    - Abstract platform away
    - Requirements:
        - Read-only arrays
        - Affine indexing!
        - Side-effect free functions, no global state
        - No variables
        - No control flow (or maybe with masks)
1. Keep limbs in variables (and thereby hopefully in registers), not local stack arrays
1. Keep # of live variables low to reduce register pressure
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
1. Update requirements.txt

## Presentation

1. When?
1. Summary?
