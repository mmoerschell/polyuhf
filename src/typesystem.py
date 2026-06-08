from dataclasses import dataclass
from typing import Literal

"""
DSL Types
"""


@dataclass(frozen=True)
class Index:
    def __str__(self) -> str:
        return "index"


@dataclass(frozen=True)
class PrimeField:
    pi: int
    theta: int

    def __str__(self) -> str:
        return f"prime<{self.pi}, {self.theta}>"

    def chunk_size(self) -> int:
        return self.pi // 8

    def prime_as_hex(self) -> str:
        return hex((1 << self.pi) - self.theta)


@dataclass(frozen=True)
class Buffer:
    def __str__(self) -> str:
        return "buffer"


DSLType = Index | PrimeField | Buffer

IRType = Literal["scalar", "vector", "matrix", "pod"]
