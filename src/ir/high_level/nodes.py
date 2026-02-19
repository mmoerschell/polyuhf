from dataclasses import dataclass

from ir.types import Type


@dataclass(frozen=True)
class IRNode:
    ty: Type


@dataclass(frozen=True)
class IRConst(IRNode):
    value: int


@dataclass(frozen=True)
class IRVar(IRNode):
    name: str


@dataclass(frozen=True)
class IRArrayAccess(IRNode):
    array: IRVar  # variable, such as 'A' in 'A[i]'
    index: IRNode  # index, such as 'i' in 'A[i]'


@dataclass(frozen=True)
class IRBinOp(IRNode):
    op: str
    left: IRNode
    right: IRNode


@dataclass(frozen=True)
class IRReduction(IRNode):
    op: str
    var: str
    start: IRNode
    stop: IRNode
    step: IRNode
    body: IRNode


@dataclass(frozen=True)
class IRPower(IRNode):
    base: IRNode
    exponent: IRNode


@dataclass(frozen=True)
class FunctionSignature:
    name: str
    params: list[Type]
    return_type: Type


@dataclass(frozen=True)
class IRFunction(IRNode):
    # TODO: remove IRNode inheritance?
    name: str
    params: list[IRVar]
    body: IRNode


@dataclass(frozen=True)
class IRCall(IRNode):
    function: str  # function name, TODO actual pointer?
    args: list[IRNode]  # evaluated arguments


@dataclass(frozen=True)
class IRProgram:
    # NOT an IRNode, doesn't have a type
    functions: list[IRFunction]
