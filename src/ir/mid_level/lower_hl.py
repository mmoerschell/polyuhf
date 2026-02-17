from typing import Dict, List, Tuple

from ir.high_level.nodes import IRBinOp, IRConst, IRFunction, IRNode, IRProgram, IRVar
from ir.mid_level_ssa.nodes import (
    BasicBlock,
    Branch,
    ControlFlowGraph,
    Instruction,
    Jump,
    Return,
    SSABinaryOp,
    SSAConstant,
    SSAFunction,
    SSAValue,
)
from ir.types import Type


class CFGBuilder:
    blocks: List[Tuple[str, BasicBlock]]
    current_block: BasicBlock
    params: List[Tuple[IRVar, SSAValue]]
    constants: Dict[Tuple[Type, int], SSAConstant]

    def __init__(self, hl_function: IRFunction) -> None:
        self.blocks = [("", BasicBlock([]))]
        self.current_block = self.blocks[0][1]
        self.params = []
        for param in hl_function.params:
            self.params.append((param, SSAValue(param.type)))
        self.constants = {}

    def get_param(self, var: IRVar) -> SSAValue:
        # Linear search but usually over tiny range
        # Allows us to preserve function signature
        for p in self.params:
            if p[0] == var:
                return p[1]
        raise ValueError(f"Unkonwn parameter {var.name}")

    def emit(self, instr: Instruction) -> SSAValue:
        self.current_block.instructions.append(instr)
        return instr

    def branch(self, cond: SSAValue, then_branch: BasicBlock, else_branch: BasicBlock):
        if self.current_block.terminator:
            raise ValueError("Current block already has a terminator")
        self.current_block.terminator = Branch(None, cond, then_branch, else_branch)

    def jump(self, target: BasicBlock):
        if self.current_block.terminator:
            raise ValueError("Current block already has a terminator")
        self.current_block.terminator = Jump(None, target)

    def new_block(self, name: str):
        self.current_block = BasicBlock([])
        self.blocks.append((name, self.current_block))
        return self.current_block

    def finalize(self, name: str, type: Type) -> SSAFunction:
        return SSAFunction(name, self.params, ControlFlowGraph(self.blocks[0][1], self.blocks[1:]))


def compile_node(n: IRNode, b: CFGBuilder) -> SSAValue:
    if isinstance(n, IRConst):
        return b.constants.setdefault((n.type, n.value), SSAConstant(n.type, n.value))
    if isinstance(n, IRVar):
        return b.get_param(n)
    if isinstance(n, IRBinOp):
        operator = None
        match n.type, n.op:
            case Type.INDEX, "+":
                operator = "add"
            case Type.INDEX, "-":
                operator = "sub"
            case Type.INDEX, "*":
                operator = "mul"
            case Type.INDEX, "/":
                operator = "sdiv"
            case Type.INDEX, op:
                raise ValueError(f"Unknown {Type.INDEX} binop {op}")
            case Type.BIGINT, "+":
                operator = "bigint_add"
            case Type.BIGINT, "*":
                # TODO decided between algorithms
                operator = "bigint_mul"
            case t, op:
                raise ValueError(f"Unknwon {t} operator {op}")
        left = compile_node(n.left, b)
        right = compile_node(n.right, b)
        value = b.emit(SSABinaryOp(n.type, operator, left, right))
        return value
    else:
        raise NotImplementedError(f"Unexpected {type(n)} node")


def lower_hl_function(f: IRFunction) -> SSAFunction:
    builder = CFGBuilder(f)
    # TODO: add params, name whatever
    # Compile body node
    try:
        body_value = compile_node(f.body, builder)
    except RecursionError as re:
        raise RuntimeError("Iterative solution required") from re
    # TODO: phi nodes, multiple sources etc
    builder.current_block.terminator = Return(None, body_value)
    return builder.finalize(f.name, f.type)


def lower_hl_program(hl_ir: IRProgram) -> List[SSAFunction]:
    return [lower_hl_function(f) for f in hl_ir.functions]
