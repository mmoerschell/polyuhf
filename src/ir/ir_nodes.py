from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from typesystem import DSLType, IRType


@dataclass(frozen=True)
class IROperand:
    dsl_type: DSLType
    ir_type: IRType


@dataclass(frozen=True)
class IRConst(IROperand):
    value: int


@dataclass(frozen=True)
class IRBoundIdentifier(IROperand):
    # params and loop indices
    name: str


@dataclass(frozen=True)
class IRTemporary(IROperand):
    pass


@dataclass(frozen=True)
class IRInstruction:
    declare: bool  # true iff result is a new temporary
    result: IRTemporary
    insn_name: str
    operands: tuple[IROperand, ...]


@dataclass(frozen=True)
class IRLoop:
    variable: IRBoundIdentifier
    begin: IROperand
    end: IROperand
    increment: IROperand
    body: list[IRStatement]
    bound: sp.Expr


@dataclass(frozen=True)
class IRIfElse:
    cond: IROperand
    then_branch: list[IRStatement]
    else_branch: list[IRStatement] | None
    constant_time: bool


@dataclass(frozen=True)
class IRReturn:
    value: IROperand


IRStatement = IRInstruction | IRLoop | IRIfElse | IRReturn


@dataclass(frozen=True)
class IRFunctionSignature:
    name: str
    params: tuple[tuple[str, IRType], ...]
    return_type: IRType


@dataclass(frozen=True)
class IRFunction:
    name: str
    params: list[IRBoundIdentifier]
    body: list[IRStatement]
    return_value: IROperand
    dsl_return_type: DSLType
    ir_return_type: IRType


@dataclass(frozen=True)
class IRModule:
    name: str
    funcs: list[IRFunction]
