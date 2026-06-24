# Table of Contents

## Introduction

- Detailed problem description

## Background

- UHF
- Related work + existing approaches
- New designs from other paper

## Implementation

- Biginteger arithmetic
    - (Un)saturated representations
    - (Un)balanced representations
    - En/decodings

- Description of compiler
- Common polynomial operations

### Prime field arithmetic
- Add, Mul, Sums, Horner, Foldl
- Squaring (faster)
- Karatsuba

### Limb realignment and carry propagation

- Modular reduction, carries, whatever else
- Immediate
- Partial (at the end of every iteration -> WATCH OUT: Poly1305 doesn't like unrolling too much)
- Fully delayed (some functions!?)
- Classical polynomial evaluation strategy: Horner

- Squeeze in:
    - Carry propagation over bottom 2 limbs
    - Unrolling factor of at most 4

## Compiler/Design + Implementation

- Split this into language vs compiler (flags) + optionally compiler implementation

### DSL

- Three types of reductions: sums, horners and left folds. All may unroll (partially delay), only sum and horner are vectorized
- Vectoization with correctness on the shoulders of the programmer: accesses must be linear
- A little context table somewhere

### IR
### Codegen

- AVX2
- Neon

## Correctness

- Automatically generated tests
- A handful of hand-written ones

## Evaluation

- Code is fully compute-bound
- On x86, we report raw invariant-TSC deltas and follow the common convention of treating them as cycles. On Apple Silicon, the architectural counter does not tick at core frequency, so we convert counter ticks to estimated cycles using the counter frequency and an assumed 4.05 GHz performance-core frequency.
### Results

- Unrolling only really useful if used to delay carry-propagation -> spills?
- Iterative rewrites of HKM, MHP

### Selection of experiments graphs

### Confirm GF(2^116-3) as a good field

### Performance Model

## Summary
## Conclusion

- Future work
## References

- Papers
- ASL 2026 homework 1 headers

## Appendix
