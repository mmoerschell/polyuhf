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


@dataclass(frozen=True)
class BinaryField:
    n: int

    def __str__(self) -> str:
        return f"binary<{self.n}>"


Field = PrimeField | BinaryField


@dataclass(frozen=True)
class BufferView:
    element_type: Field
    chunk_size: int  # in bytes. could be slightly less than field's bitwidth

    def __str__(self) -> str:
        return f"view {self.element_type}"


DSLType = Index | Field | BufferView
"""
IR Types
"""

# Holds indices
@dataclass(frozen=True)
class IRTypeScalar:
    machine_width: int

    def __str__(self) -> str:
        return f"i{self.machine_width}"


# Holds one bigint
@dataclass(frozen=True)
class IRTypeVector:
    machine_width: int
    limbs: int
    lambd: int
    lambd_prime: int
    lambd_mask: int
    lambd_prime_mask: int

    def __str__(self) -> str:
        return f"i{self.machine_width}[{self.limbs}]"


# Holds <lanes> bigints
@dataclass(frozen=True)
class IRTypeMatrix:
    machine_width: int
    lanes: int
    limbs: int
    lambd: int
    lambd_prime: int
    lambd_mask: int
    lambd_prime_mask: int

    def __str__(self) -> str:
        return f"i{self.machine_width}x{self.lanes}[{self.limbs}]"


IRType = IRTypeScalar | IRTypeVector | IRTypeMatrix | Literal["pod"]


"""
C Types
"""
