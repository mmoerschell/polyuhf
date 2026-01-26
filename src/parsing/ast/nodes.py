from dataclasses import dataclass
from typing import List

# ---------- Base nodes ----------


class ASTNode:
    pass


class Expr(ASTNode):
    pass


@dataclass
class Int(Expr):
    value: int


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
    power: Expr  # could restrict this to Int


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
    params: List[str]
    body: Expr
