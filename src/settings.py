from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Union


@dataclass(frozen=True)
class CrandallPrime:
    pi: int
    theta: int
    # 2^pi - theta, e.g. 2^130-5


@dataclass(frozen=True)
class ArbitraryPrime:
    value: int


Prime = Union[CrandallPrime, ArbitraryPrime]


@dataclass(frozen=True)
class PrimeField:
    p: Prime
    # GF(prime)


@dataclass(frozen=True)
class BinaryField:
    n: int
    # GF(2^n)


Field = Union[PrimeField, BinaryField]


@dataclass(frozen=True)
class BigIntConfiguration:
    limbs: int
    lambd: int
    lambd_prime: int
    field: Field

    @staticmethod
    def from_field(field: Field) -> BigIntConfiguration:
        required_width = None
        match field:  # type: ignore
            case PrimeField(CrandallPrime(pi, _)):
                required_width = pi
            case PrimeField(ArbitraryPrime(value)): # pyright: ignore[reportUnusedVariable]
                raise NotImplementedError("how many bits do we need??")
            case BinaryField(n):
                required_width = n
        assert required_width
        lambd = 22  # TODO, fixed for now
        lambd_prime = required_width % lambd
        limbs = math.ceil(required_width / lambd)
        assert limbs > 0
        return BigIntConfiguration(limbs, lambd, lambd_prime, field)

    def generate_header(self, output_path: str) -> None:
        lambd_mask = hex((1 << self.lambd) - 1)
        lambd_prime_mask = hex((1 << self.lambd_prime) - 1)
        assert lambd_mask.startswith("0x"), "skill issue"
        lines: List[str] = [
            "#pragma once",
            "",
            f"// Generated for {str(self.field)} ({self.limbs}x{self.lambd} bits)",
            "",
            "#include <stddef.h>",
            "#include <stdint.h>",
            "",
            f"#define LIMBS {self.limbs}",
            f"#define LAMBDA {self.lambd}",
            f"#define LAMBDA_PRIME {self.lambd_prime}",
            f"#define LAMBDA_MASK {lambd_mask}",
            f"#define LAMBDA_PRIME_MASK {lambd_prime_mask}",
            "",
            "typedef union {",
            f"    alignas(64) uint64_t limbs[{self.limbs}];",
            # optionally other views into the data
            "} bigint_t;",
            "",
        ]
        with open(output_path, "w") as f:
            f.write("\n".join(lines))
