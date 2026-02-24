from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Union


class LoweringError(Exception):
    pass


@dataclass(frozen=True)
class IndexType:
    # TODO # of bits?

    def __str__(self) -> str:
        return "index"


@dataclass(frozen=True)
class BigIntType:
    # TODO # of limbs?

    def __str__(self) -> str:
        return "bigint"


@dataclass(frozen=True)
class ArrayType:
    size: Optional[int]
    elem: Type

    def __str__(self) -> str:
        return f"[{self.size if self.size else ''}]{self.elem}"


Type = Union[IndexType, BigIntType, ArrayType]
