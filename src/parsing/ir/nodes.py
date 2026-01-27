from dataclasses import dataclass

from .types import Type


class IRNode:
    type: Type


@dataclass(frozen=True)
class IRConst(IRNode):
    value: int
    type: Type


@dataclass(frozen=True)
class IRVar(IRNode):
    name: str
    type: Type


@dataclass(frozen=True)
class IRArrayAccess(IRNode):
    array: IRVar  # variable, such as 'A' in 'A[i]'
    index: IRNode  # index, such as 'i' in 'A[i]'
    type: Type = Type.FIELD


@dataclass(frozen=True)
class IRBinOp(IRNode):
    op: str
    left: IRNode
    right: IRNode
    type: Type


@dataclass(frozen=True)
class IRReduction(IRNode):
    op: str
    var: str
    start: IRNode
    stop: IRNode
    step: IRNode
    body: IRNode
    type: Type


@dataclass(frozen=True)
class IRPower(IRNode):
    base: IRNode
    exponent: IRNode
    type: Type


@dataclass(frozen=True)
class IRFunction(IRNode):
    name: str
    params: list[tuple[str, Type]]  # name, type
    body: IRNode
    type: Type


@dataclass(frozen=True)
class IRProgram(IRNode):
    functions: list[IRFunction]
