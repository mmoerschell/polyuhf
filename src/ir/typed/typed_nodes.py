from dataclasses import dataclass

from ir.types import Type


@dataclass(frozen=True)
class TNode:
    ty: Type


@dataclass(frozen=True)
class TConst(TNode):
    value: int


@dataclass(frozen=True)
class TVar(TNode):
    name: str


@dataclass(frozen=True)
class TArrayAccess(TNode):
    array: TVar  # variable, such as 'A' in 'A[i]'
    index: TNode  # index, such as 'i' in 'A[i]'


@dataclass(frozen=True)
class TBinOp(TNode):
    op: str
    left: TNode
    right: TNode


@dataclass(frozen=True)
class TUnaryMinus(TNode):
    body: TNode


@dataclass(frozen=True)
class TReduction(TNode):
    op: str
    var: str
    start: TNode
    stop: TNode
    step: TNode
    body: TNode


@dataclass(frozen=True)
class TPower(TNode):
    base: TNode
    exponent: TNode


@dataclass(frozen=True)
class TIfElse(TNode):
    cond: TNode
    then_branch: TNode
    else_branch: TNode


@dataclass(frozen=True)
class TFunctionSignature:
    name: str
    params: list[Type]
    return_type: Type


@dataclass(frozen=True)
class TFunction:
    name: str
    params: list[TVar]
    return_type: Type
    body: TNode


@dataclass(frozen=True)
class TCall(TNode):
    function: str  # function name, TODO actual pointer?
    args: list[TNode]  # evaluated arguments


@dataclass(frozen=True)
class TProgram:
    # NOT a TNode, doesn't have a type
    functions: list[TFunction]
