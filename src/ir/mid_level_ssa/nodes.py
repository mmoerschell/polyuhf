from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from ir.high_level.nodes import IRVar
from ir.types import Type


@dataclass
class SSAValue:
    type: Type | None
    # TODO: use-list?


@dataclass
class SSAConstant(SSAValue):
    value: int

    def __repr__(self) -> str:
        return f"{self.value}"


@dataclass
class Instruction(SSAValue):
    pass


@dataclass
class Allocate(Instruction):
    # For stack allocations
    n_bytes: int


@dataclass
class Load(Instruction):
    # Loads (bigint) pointers
    # TODO unimplemented
    pointer: SSAValue  # bigint pointer


@dataclass
class SSAUnaryOp(Instruction):
    operator: str
    operand: SSAValue


@dataclass
class SSABinaryOp(Instruction):
    operator: str
    operand1: SSAValue
    operand2: SSAValue


@dataclass
class Terminator(SSAValue):
    type = None


@dataclass
class Jump(Terminator):
    block: BasicBlock


@dataclass
class Branch(Terminator):
    condition: SSAValue
    then_branch: BasicBlock
    else_branch: BasicBlock


@dataclass
class Return(Terminator):
    value: SSAValue


@dataclass
class BasicBlock:
    instructions: List[Instruction]
    terminator: Terminator | None = None  # lec07 slide 28, why would it need a UID?


@dataclass
class ControlFlowGraph:
    entry: BasicBlock
    subsequent: List[Tuple[str, BasicBlock]]  # name, block


@dataclass
class SSAFunction:
    name: str
    params: List[Tuple[IRVar, SSAValue]]
    # return type, etc.
    # TODO
    cfg: ControlFlowGraph

    def __repr__(self) -> str:
        fp = FunctionPrinter(self)
        return repr(fp)


# Pretty-printing pass for debugging
class FunctionPrinter:
    def __init__(self, function: SSAFunction) -> None:
        self.function = function
        self.counter: int = 0
        self.names: Dict[int, str] = {}

        # Assign names to all parameters
        for var, ssa_value in function.params:
            self.names[id(ssa_value)] = var.name

        # Assign names to all instructions
        for _, block in [(None, function.cfg.entry)] + function.cfg.subsequent:
            for instr in block.instructions:
                self.assign_name(instr)

    def assign_name(self, val: SSAValue):
        if not val.type:
            return
        if isinstance(val, SSAConstant):
            return
        self.names[id(val)] = f"%{self.counter}"
        self.counter += 1

    def get_name(self, val: SSAValue):
        if isinstance(val, SSAConstant):
            return str(val.value)
        return self.names.get(id(val), "<???>")

    def __repr__(self) -> str:
        lines: List[str] = []
        lines.append(
            f"func @{self.function.name} ({', '.join([f'{p[0].type} {p[0].name}' for p in self.function.params])}) "
            + "{"
        )
        # TODO params, whatever
        for label, block in [
            (None, self.function.cfg.entry)
        ] + self.function.cfg.subsequent:
            if label:
                lines.append(f"{label}:")
            for instr in block.instructions:
                if isinstance(instr, SSABinaryOp):
                    lines.append(
                        f"  {self.get_name(instr)} = {instr.operator} "
                        f"{self.get_name(instr.operand1)}, "
                        f"{self.get_name(instr.operand2)}"
                    )
                else:
                    raise NotImplementedError(f"Print {type(instr)} instruction")
            if isinstance(block.terminator, Return):
                lines.append(f"  ret {self.get_name(block.terminator.value)}")
            else:
                raise NotImplementedError(f"Print {type(block.terminator)} terminator")
        lines.append("}")
        return "\n".join(lines)

    __str__ = __repr__
