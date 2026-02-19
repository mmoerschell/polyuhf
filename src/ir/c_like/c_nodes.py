from dataclasses import dataclass
from typing import List, Tuple

from ir.types import Type


@dataclass(frozen=True)
class CScalarExpression:
    pass


@dataclass(frozen=True)
class CScalarConst(CScalarExpression):
    value: int


@dataclass(frozen=True)
class CScalarParameter(CScalarExpression):
    name: str



@dataclass(frozen=True)
class CScalarAddition(CScalarExpression):
    operand1: CScalarExpression
    operand2: CScalarExpression


@dataclass(frozen=True)
class CScalarSubtraction(CScalarExpression):
    operand1: CScalarExpression
    operand2: CScalarExpression


@dataclass(frozen=True)
class CScalarMultiplication(CScalarExpression):
    operand1: CScalarExpression
    operand2: CScalarExpression


@dataclass(frozen=True)
class CScalarDivision(CScalarExpression):
    dividend: CScalarExpression
    divisor: CScalarExpression


@dataclass(frozen=True)
class CVectorExpression:
    pass

@dataclass(frozen=True)
class CStatement:
    pass


@dataclass(frozen=True)
class CReturn(CStatement):
    expression: CScalarExpression | None


@dataclass(frozen=True)
class CFunction:
    name: str
    parameters: List[Tuple[Type, str]]
    statements: List[CStatement]
    return_type: Type


@dataclass(frozen=True)
class CProgram:
    functions: List[CFunction]
