from abc import ABC, abstractmethod
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
class Field(ABC):
    @abstractmethod
    def bit_length(self) -> int:
        pass

    @abstractmethod
    def chunk_size(self) -> int:
        pass


@dataclass(frozen=True)
class PrimeField(Field):
    pi: int
    theta: int

    def __str__(self) -> str:
        return f"prime<{self.pi}, {self.theta}>"

    def bit_length(self) -> int:
        return self.pi

    def chunk_size(self) -> int:
        return self.pi // 8

    def prime_as_hex(self) -> str:
        return hex((1 << self.pi) - self.theta)


@dataclass(frozen=True)
class BinaryField(Field):
    n: int

    def __str__(self) -> str:
        return f"binary<{self.n}>"

    def bit_length(self) -> int:
        return self.n

    def chunk_size(self) -> int:
        return self.n // 8


@dataclass(frozen=True)
class Buffer:
    def __str__(self) -> str:
        return "buffer"


DSLType = Index | Field | Buffer

IRType = Literal["scalar", "vector", "matrix", "pod"]
