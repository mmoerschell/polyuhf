from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from typesystem import DSLType

# ---------- Base nodes ----------


class ASTNode:
    pass


@dataclass
class ASTExpr(ASTNode):
    ttype: DSLType | None


# ---------- Expressions ----------


@dataclass
class ASTInt(ASTExpr):
    value: int


@dataclass
class ASTLocalIdentifier(ASTExpr):
    name: str


@dataclass
class ASTUnaryMinus(ASTExpr):
    operand: ASTExpr


@dataclass
class ASTBinaryOperation(ASTExpr):
    operator: Literal["+", "-", "*", "/", "%", "^"]
    left: ASTExpr
    right: ASTExpr

@dataclass
class ASTComparison(ASTExpr):
    operator: Literal["==", "!=", "<", "<=", ">", ">="]
    left: ASTExpr
    right: ASTExpr

@dataclass
class ASTIfElse(ASTExpr):
    condition: ASTExpr
    then_branch: ASTExpr
    else_branch: ASTExpr


@dataclass
class ASTCall(ASTExpr):
    func_name: str
    args: list[ASTExpr]


@dataclass
class ASTBufferViewRead(ASTExpr):
    buffer: ASTLocalIdentifier
    index: ASTExpr


@dataclass
class ASTReduction(ASTExpr):
    op: str
    var: str
    start: ASTExpr
    stop: ASTExpr
    step: ASTExpr
    body: ASTExpr


# ---------- Functions, modules ----------


@dataclass
class ASTFunction(ASTNode):
    name: str
    params: list[tuple[str, DSLType]]
    return_type: DSLType
    body: ASTExpr


@dataclass
class ASTModule:
    functions: list[ASTFunction]
