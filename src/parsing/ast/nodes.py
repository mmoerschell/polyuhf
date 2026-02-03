from dataclasses import dataclass
from typing import List, Tuple

from parsing.ir.types import Type

# ---------- Base nodes ----------


class ASTNode:
    pass


class Expr(ASTNode):
    pass


@dataclass
class Int(Expr):
    value: int
    type: Type  # index, bigint


@dataclass
class Var(Expr):
    name: str


@dataclass
class Add(Expr):
    left: Expr
    right: Expr


@dataclass
class Sub(Expr):
    left: Expr
    right: Expr


@dataclass
class Mul(Expr):
    left: Expr
    right: Expr


@dataclass
class Div(Expr):
    left: Expr
    right: Expr


@dataclass
class Power(Expr):
    base: Expr
    exponent: Expr  # could restrict this to Int


@dataclass
class Neg(Expr):
    body: Expr


@dataclass
class Call(Expr):
    func: str  # function name. TODO make this point to IRFunction?
    args: List[Expr]  # argument expressions


@dataclass
class ArrayAccess(Expr):
    array: str
    index: Expr


@dataclass
class Reduction(Expr):
    op: str
    var: str
    start: Expr
    stop: Expr
    step: Expr
    body: Expr


# ---------- Program structure ----------


@dataclass
class Program(ASTNode):
    functions: List["Function"]


@dataclass
class Function(ASTNode):
    name: str
    params: List[Tuple[str, Type]]
    return_type: Type
    body: Expr
