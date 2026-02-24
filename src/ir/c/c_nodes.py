from dataclasses import dataclass
from typing import List, Optional, Tuple

from ir.types import Type


@dataclass(frozen=True)
class CExpression:
    pass


@dataclass(frozen=True)
class CIdentifier(CExpression):
    name: str


@dataclass(frozen=True)
class CArrayAccess(CExpression):
    array: CIdentifier
    index: CExpression


@dataclass(frozen=True)
class CConst(CExpression):
    ty: Type
    value: int


@dataclass(frozen=True)
class CParameter(CExpression):
    name: str


@dataclass(frozen=True)
class CBinOp(CExpression):
    operator: str
    operand1: CExpression
    operand2: CExpression


@dataclass(frozen=True)
class CUnaryMinus(CExpression):
    body: CExpression


@dataclass(frozen=True)
class CFunctionCall(CExpression):
    func: str
    args: List[CExpression]


@dataclass(frozen=True)
class CStatement:
    pass


@dataclass(frozen=True)
class CDeclaration(CStatement):
    type: Type
    name: str
    init: Optional[CExpression] = None


@dataclass(frozen=True)
class CAssign(CStatement):
    lhs: CExpression  # must be identifier or array
    rhs: CExpression


@dataclass(frozen=True)
class CReturn(CStatement):
    expression: CExpression | None


@dataclass(frozen=True)
class CWhile(CStatement):
    condition: CExpression
    statements: List[CStatement]


@dataclass(frozen=True)
class CFunction:
    name: str
    parameters: List[Tuple[Type, str]]
    statements: List[CStatement]
    return_type: Type


@dataclass(frozen=True)
class CProgram:
    functions: List[CFunction]
