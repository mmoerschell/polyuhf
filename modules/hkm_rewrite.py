#!/usr/bin/env python3

print("kl  B    HKM(kl, B)")
print(" 1  1 -> (r1 + M1)")

for B in range(2, 51):
    kl = B // 2 + 1
    odd_term = f" + M{B}" if B & 1 else ""
    print(
        f"{kl:2} {B:2} -> "
        f"HKM({B // 2:2}, {2 * (B // 2) - 1:2}) * "
        f"(r{B // 2 + 1} + M{2 * (B // 2)})"
        f"{odd_term}"
    )

"""
Pattern:
B           HKM
1       ->  r1 + M1
even    ->  acc * (r.. + M..)
odd     ->  acc + M..

Clearly a left fold.
From paper: "no support for fully delayed limb realignment and parallelization"
"""
