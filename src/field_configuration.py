import math
from dataclasses import dataclass
from typing import List, Union


@dataclass(frozen=True)
class PrimeField:
    pi: int
    theta: int
    # GF(2^pi-theta)


@dataclass(frozen=True)
class BinaryField:
    n: int
    # GF(2^n)


Field = Union[PrimeField, BinaryField]


@dataclass(frozen=True)
class FieldConfiguration:
    field: Field
    bitwidth: int
    limbs: int
    lambda_: int
    lambda_prime: int
    lambda_mask: int
    lambda_prime_mask: int

    @classmethod
    def from_field(cls, field: Field, lambda_: int):
        match field:
            case PrimeField(pi, _):
                bitwidth = pi
            case BinaryField(n):
                bitwidth = n
        limbs = math.ceil(bitwidth / lambda_)
        lambda_prime = (
            (bitwidth - 1) % lambda_ + 1
        )  # sets lambda = lambda_prime if remainderless division is possible
        lambda_mask = (1 << lambda_) - 1
        lambda_prime_mask = (1 << lambda_prime) - 1
        return cls(
            field=field,
            bitwidth=bitwidth,
            limbs=limbs,
            lambda_=lambda_,
            lambda_prime=lambda_prime,
            lambda_mask=lambda_mask,
            lambda_prime_mask=lambda_prime_mask,
        )

    def generate_header(self, output_path: str) -> None:
        lines: List[str] = [
            "#pragma once",
            "",
            f"// Generated for {self}",
            "",
            "#include <stddef.h>",
            "#include <stdint.h>",
            "",
            # TODO: are these all necessary?
            f"#define BITWIDTH {self.bitwidth}ULL",
            f"#define LIMBS {self.limbs}ULL",
            f"#define LAMBDA {self.lambda_}ULL",
            f"#define LAMBDA_PRIME {self.lambda_prime}ULL",
            f"#define LAMBDA_MASK {hex(self.lambda_mask)}ULL",
            f"#define LAMBDA_PRIME_MASK {hex(self.lambda_prime_mask)}ULL",
            "",
            "typedef union {",
            f"    alignas(64) uint64_t limbs[{self.limbs}];",
            # optionally other views into the data
            "} bigint_t;",
            "",
        ]
        with open(output_path, "w") as f:
            f.write("\n".join(lines))
