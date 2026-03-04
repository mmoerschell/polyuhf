from dataclasses import dataclass
from typing import Union


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
