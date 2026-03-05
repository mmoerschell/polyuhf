from dataclasses import dataclass

from settings import BigIntConfiguration


@dataclass(frozen=True)
class Helpers:
    bigint_config: BigIntConfiguration

    def carry(self) -> str:
        # TODO: field arithmetic, carry last limb back to first?
        return f"""
void carry(bigint_t* x) {{
    for (size_t i = 0; i < {self.bigint_config.limbs} - 1; ++i) {{
        const int64_t carry_amount = x->limbs[i] >> LAMBDA;
        x->limbs[i] &= LAMBDA_MASK;
        x->limbs[i + 1] += carry_amount;
    }}
}}
"""

    def add(self) -> str:
        return f"""
void add(bigint_t* dst, const bigint_t* lhs, const bigint_t* rhs) {{
    for (size_t i = 0; i < {self.bigint_config.limbs}; ++i)
        dst->limbs[i] = lhs->limbs[i] + rhs->limbs[i];
    carry(dst);
}}
"""

    def mul(self) -> str:
        return f"""
void mul(bigint_t* dst, const bigint_t* lhs, const bigint_t* rhs) {{
    for (size_t i = 0; i < {self.bigint_config.limbs}; ++i) {{
        for (size_t j = 0; j <= i; ++j) {{
            dst->limbs[i] += lhs->limbs[j] * rhs->limbs[i - j];
        }}
    }}
    carry(dst);
}}
"""

    def generate_header(self, output_path: str) -> None:
        lines = [
            "#pragma once",
            "",
            "#include <stddef.h>",
            "#include <stdint.h>",
            "#include <string.h>",
            "",
            "#include \"configuration.h\"",
            "\n".join([self.carry(), self.add(), self.mul()]),
        ]
        with open(output_path, "w") as f:
            f.write("\n".join(lines))
