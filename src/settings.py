from __future__ import annotations

from dataclasses import dataclass
from typing import Union
import math

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

    @staticmethod
    def from_field(field: Field) -> BigIntConfiguration:
        required_width = None
        match field: # type: ignore
            case PrimeField(CrandallPrime(pi, _)):
                required_width = pi
            case PrimeField(ArbitraryPrime(value)):
                required_width = value.bit_count() + 1
            case BinaryField(n):
                required_width = n
        assert required_width
        lambd = 22  # TODO, fixed for now
        limbs = math.ceil(required_width / lambd)
        assert limbs > 0
        return BigIntConfiguration(limbs, lambd)
