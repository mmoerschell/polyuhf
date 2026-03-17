from dataclasses import dataclass

from settings import BigIntConfiguration

# TODO Python type correctness

BUILTIN_BIGINT_FUNCTIONS = {
    "+": "_bigint_add",
    "*": "_bigint_mul",
    "^": "_bigint_exp",
    "carry_round": "_bigint_carry_round",
    "print": "_bigint_print",
}


@dataclass(frozen=True)
class Helpers:
    bigint_config: BigIntConfiguration

    def print(self) -> str:
        return f"""
inline void {BUILTIN_BIGINT_FUNCTIONS["print"]}(bigint_t x) {{
    printf("[");
    for (size_t i = 0; i < {self.bigint_config.limbs - 1}; ++i)
        printf("%06llx, ", x.limbs[i]);
    printf("%05llx]\\n", x.limbs[{self.bigint_config.limbs - 1}]);
}}
"""

    def carry(self) -> str:
        return f"""
inline bigint_t {BUILTIN_BIGINT_FUNCTIONS["carry_round"]}(bigint_t x) {{
    bigint_t dst = x;

    // All limbs except most significant: carry over to next limb
    for (size_t i = 0; i < {self.bigint_config.limbs - 1}; ++i) {{
        const uint64_t carry_amount = dst.limbs[i] >> LAMBDA;
        dst.limbs[i] &= LAMBDA_MASK;
        dst.limbs[i + 1] += carry_amount;
    }}

    // Most significant limb: take (& remove) high bits,
    // multiply by theta and add to first limb
    const uint64_t high_bits = dst.limbs[{self.bigint_config.limbs - 1}] >> LAMBDA_PRIME;
    dst.limbs[{self.bigint_config.limbs - 1}] &= LAMBDA_PRIME_MASK;
    dst.limbs[0] += {self.bigint_config.field.p.theta} * high_bits;

    // Propagate carry over lowest two limbs
    for (size_t i = 0; i < 2; ++i) {{
        const uint64_t carry_amount = dst.limbs[i] >> LAMBDA;
        dst.limbs[i] &= LAMBDA_MASK;
        dst.limbs[i + 1] += carry_amount;
    }}
    return dst;
}}
"""

    def add(self) -> str:
        return f"""
inline bigint_t {BUILTIN_BIGINT_FUNCTIONS["+"]}(const bigint_t lhs, const bigint_t rhs) {{
    bigint_t dst;
    for (size_t i = 0; i < {self.bigint_config.limbs}; ++i)
        dst.limbs[i] = lhs.limbs[i] + rhs.limbs[i];
    dst = {BUILTIN_BIGINT_FUNCTIONS["carry_round"]}(dst);
    return dst;
}}
"""

    def mul(self) -> str:
        kappa = hex(
            self.bigint_config.field.p.theta
            * (1 << (self.bigint_config.lambd - self.bigint_config.lambd_prime))
        )
        return f"""
inline bigint_t {BUILTIN_BIGINT_FUNCTIONS["*"]}(const bigint_t lhs, const bigint_t rhs) {{
    bigint_t dst;
    memset(&dst, 0, sizeof(bigint_t));
    for (size_t i = 0; i < {self.bigint_config.limbs}; ++i) {{
        for (size_t j = 0; j <= i; ++j)
            dst.limbs[i] += lhs.limbs[j] * rhs.limbs[i - j];
        for (size_t j = i + 1; j < {self.bigint_config.limbs}; ++j)
            dst.limbs[i] += lhs.limbs[j] * {kappa}UL * rhs.limbs[{self.bigint_config.limbs} + i - j];
    }}
    dst = {BUILTIN_BIGINT_FUNCTIONS["carry_round"]}(dst);
    return dst;
}}
"""

    def exp(self):
        return f"""
inline bigint_t {BUILTIN_BIGINT_FUNCTIONS["^"]}(const bigint_t base, const uint64_t power) {{
    bigint_t dst;
    memset(&dst, 0, sizeof(bigint_t));
    dst.limbs[0] = 1UL;
    for (uint64_t i = 0; i < power; ++i)
        dst = {BUILTIN_BIGINT_FUNCTIONS["*"]}(dst, base);
    return dst;
}}
"""

    def generate_header(self, output_path: str) -> None:
        lines = [
            "#pragma once",
            "",
            f"// Generated for "
            f"{str(self.bigint_config.field)} "
            f"({self.bigint_config.limbs}x{self.bigint_config.lambd} bits)",
            "",
            "#include <stddef.h>",
            "#include <stdio.h>",
            "#include <stdint.h>",
            "#include <string.h>",
            "",
            '#include "configuration.h"',
            "\n".join([self.print(), self.carry(), self.add(), self.mul(), self.exp()]),
        ]
        with open(output_path, "w") as f:
            f.write("\n".join(lines))
