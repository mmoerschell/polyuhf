from dataclasses import dataclass

from settings import BigIntConfiguration

BUILTIN_BIGINT_FUNCTIONS = {
    "+": "_bigint_add",
    "*": "_bigint_mult",
    "carry": "_bigint_carry",
}


@dataclass(frozen=True)
class Helpers:
    bigint_config: BigIntConfiguration

    def carry(self) -> str:
        # TODO: field arithmetic, carry last limb back to first?
        return f"""
inline bigint_t {BUILTIN_BIGINT_FUNCTIONS["carry"]}(bigint_t x) {{
    bigint_t dst = x;
    for (size_t i = 0; i < {self.bigint_config.limbs} - 1; ++i) {{
        const int64_t carry_amount = dst.limbs[i] >> LAMBDA;
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
    {BUILTIN_BIGINT_FUNCTIONS["carry"]}(dst);
    return dst;
}}
"""

    def mul(self) -> str:
        return f"""
inline bigint_t {BUILTIN_BIGINT_FUNCTIONS["*"]}(const bigint_t lhs, const bigint_t rhs) {{
    bigint_t dst;
    memset(&dst, 0, sizeof(bigint_t));
    for (size_t i = 0; i < {self.bigint_config.limbs}; ++i) {{
        for (size_t j = 0; j <= i; ++j) {{
            dst.limbs[i] += lhs.limbs[j] * rhs.limbs[i - j];
        }}
    }}
    {BUILTIN_BIGINT_FUNCTIONS["carry"]}(dst);
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
            "#include <stdint.h>",
            "#include <string.h>",
            "",
            '#include "configuration.h"',
            "\n".join([self.carry(), self.add(), self.mul()]),
        ]
        with open(output_path, "w") as f:
            f.write("\n".join(lines))
