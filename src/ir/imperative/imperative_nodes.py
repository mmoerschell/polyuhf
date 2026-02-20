from dataclasses import dataclass
from typing import List, Optional

from ir.types import Type


@dataclass(frozen=True)
class IExpr:
    ty: Type


@dataclass(frozen=True)
class IConst(IExpr):
    value: int


@dataclass(frozen=True)
class IVar(IExpr):
    name: str


@dataclass(frozen=True)
class IArrayAccess(IExpr):
    array: IVar  # the array variable (must be a Var)
    index: IExpr


@dataclass(frozen=True)
class IBinOp(IExpr):
    op: str  # '+', '-', '*', '/'
    left: IExpr
    right: IExpr


@dataclass(frozen=True)
class IUnaryMinus(IExpr):
    expr: IExpr


@dataclass(frozen=True)
class IPower(IExpr):
    base: IExpr
    exponent: IExpr


@dataclass(frozen=True)
class ICall(IExpr):
    function: str
    args: List[IExpr]


@dataclass(frozen=True)
class IStmt:
    pass


@dataclass(frozen=True)
class IBlock(IStmt):
    stmts: List[IStmt]


@dataclass(frozen=True)
class IDecl(IStmt):
    """Variable declaration with optional initializer."""

    ty: Type
    name: str
    init: Optional[IExpr] = None


@dataclass(frozen=True)
class IAssign(IStmt):
    """Assignment to a variable or array element."""

    lhs: IExpr  # must be a Var or ArrayAccess
    rhs: IExpr


@dataclass(frozen=True)
class IReturn(IStmt):
    expr: IExpr


@dataclass(frozen=True)
class IWhile(IStmt):
    cond: IExpr  # condition as integer
    body: IBlock


@dataclass(frozen=True)
class IParam:
    name: str
    ty: Type


@dataclass(frozen=True)
class IFunction:
    name: str
    params: List[IParam]
    return_type: Type
    body: IBlock


@dataclass(frozen=True)
class IProgram:
    functions: List[IFunction]
