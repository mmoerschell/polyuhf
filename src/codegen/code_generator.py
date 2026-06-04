from __future__ import annotations

from typing import assert_never

from jinja2 import Environment, FileSystemLoader, Template

import utils
from ir.ir_nodes import (
    IRBoundIdentifier,
    IRConst,
    IRFunction,
    IRIfElse,
    IRInstruction,
    IRLoop,
    IRModule,
    IROperand,
    IRReturn,
    IRStatement,
    IRTemporary,
)
from settings import Settings
from typesystem import (
    BufferView,
    IRType,
    PrimeField,
)


class FunctionCodeGenerator:
    def __init__(
        self, module_code_generator: ModuleCodeGenerator, func: IRFunction
    ) -> None:
        self.mcr = module_code_generator
        self.func = func
        self.temporaries: dict[int, str] = {}  # id(IRTemporary) -> C name

    def generate_signature(self) -> str:
        param_names: list[str] = []
        param_ctypes: list[str] = []
        for p in self.func.params:
            param_names.append(p.name)
            param_ctypes.append(self.mcr.compile_ir_type(p.ir_type))
        args_c = (
            ",".join(
                f"{t} {n}"
                for n, t in zip(
                    param_names,
                    param_ctypes,
                    strict=True,
                )
            )
            if len(param_names) > 0
            else "void"
        )
        return (
            f"{self.mcr.compile_ir_type(self.func.ir_return_type)} {self.func.name}"
            f"({args_c})"
        )

    def generate_definition(self, func: IRFunction, c_signature: str) -> str:
        lines: list[str] = []
        if self.mcr.settings.lanes:
            lines += [
                f"const uint64x2_t vlambda_mask = "
                f"vdupq_n_u64({self.mcr.settings.lambda_mask});",
                f"const uint64x2_t vlambda_prime_mask = "
                f"vdupq_n_u64({self.mcr.settings.lambda_prime_mask});",
            ]
        for s in self.func.body:
            text = self._compile_statement(s)
            lines.append(text)
        return f"{c_signature} {{\n{'\n'.join(lines)}\n}}"

    def _compile_statement(self, stmt: IRStatement) -> str:
        match stmt:
            case IRInstruction():
                return self._compile_instruction(stmt)
            case IRLoop(var, begin, end, increment, body):
                loop_header = (
                    f"for ({self.mcr.compile_ir_type(var.ir_type)} "
                    f"{var.name}={self._compile_operand(begin)};"
                    f"{var.name}<{self._compile_operand(end)};"
                    f"{var.name}+={self._compile_operand(increment)})"
                )
                loop_text = "\n".join(self._compile_statement(s) for s in body)
                return f"{loop_header} {'{'}\n{loop_text}\n{'}'}"
            case IRIfElse(condition, then_branch, else_branch):
                return (
                    f"if ({self._compile_operand(condition)}) "
                    f"{{{'\n'.join(self._compile_statement(s) for s in then_branch)}}}"
                    f" else "
                    f"{{{'\n'.join(self._compile_statement(s) for s in else_branch)}}}"
                )
            case IRReturn(value):
                return f"return {self._compile_operand(value)};"

    def _compile_instruction(self, insn: IRInstruction) -> str:  # noqa: C901
        optional_ctype = f"{self.mcr.compile_ir_type(insn.result.ir_type)} "
        match insn:
            # Scalar operations
            case IRInstruction(declare, result, operator, operands) if (
                result.ir_type == "scalar" and operator in utils.IR_TO_OP_TABLE.keys()
            ):
                return (
                    (optional_ctype if declare else "")
                    + f"{self._compile_operand(result)} = "
                    + utils.IR_TO_OP_TABLE[operator].join(
                        self._compile_operand(oa) for oa in operands
                    )
                    + ";"
                )
            # Prime field add/mul
            case IRInstruction(declare, result, "add" | "mul", operands) if isinstance(
                result.dsl_type, PrimeField
            ):
                if declare:
                    return (
                        f"{optional_ctype}{self._compile_operand(result)} = "
                        + "{0};"
                        + self._compile_pf_add_mul(insn)
                    )
                else:
                    return self._compile_pf_add_mul(insn)
            # Prime field carry
            case IRInstruction(
                declare,
                IRTemporary(
                    PrimeField(),
                    "vector" | "matrix",
                ) as result,
                "carry",
                operands,
            ):
                assert not declare, "carries should reuse temporaries"
                te_ctx = {
                    "x": self._compile_operand(result),
                    "settings": self.mcr.settings,
                }
                te_name = (
                    f"vcarry_{self.mcr.settings.platform}"
                    if result.ir_type == "matrix"
                    else "carry"
                )
                return self.mcr.get_template(te_name).render(te_ctx)
            # Scalar load
            case IRInstruction(
                declare,
                IRTemporary(_, "vector") as result,
                "load",
                operands,
            ):
                # TODO! remove matrix remnants from here, improve scalar loads
                assert declare, "load temporaries should not be reassigned"
                assert len(operands) >= 2
                assert isinstance(operands[0].dsl_type, BufferView), operands[0]
                assert all(isinstance(o, IRConst) for o in operands[2:])
                lanes = self.mcr.settings.lanes or 1
                assert len(operands[2:]) <= lanes
                dst = self._compile_operand(result)
                src = self._compile_operand(operands[0])
                position = self._compile_operand(operands[1])
                offsets: list[int] = [o.value for o in operands[2:]]  # type: ignore
                chunk_size = operands[0].dsl_type.chunk_size
                res: list[str] = [
                    f"/* {dst} = load {src} @ {position} w/ offsets {', '.join(map(str, offsets))} */",
                    f"{self.mcr.compile_ir_type(result.ir_type)} {dst};",
                ]
                # Figure out which byte affects which limb
                # row x col x [pair(pointer offset, shift)]
                distribution: list[list[list[tuple[int, int]]]] = [
                    [[] for _ in range(lanes)] for _ in range(self.mcr.settings.limbs)
                ]
                for j in range(len(offsets)):
                    for i in range(chunk_size):
                        byte_n = offsets[j] * chunk_size + i
                        for relevant_limb in {
                            8 * i // self.mcr.settings.lambda_,
                            min(
                                (8 * i + 7) // self.mcr.settings.lambda_,
                                self.mcr.settings.limbs - 1,
                            ),
                        }:
                            distribution[relevant_limb][j].append(
                                (
                                    byte_n,
                                    8 * i - relevant_limb * self.mcr.settings.lambda_,
                                )
                            )
                for i in range(self.mcr.settings.limbs):
                    mask = (
                        self.mcr.settings.lambda_prime_mask
                        if i == self.mcr.settings.limbs - 1
                        else self.mcr.settings.lambda_mask
                    )
                    if result.ir_type == "vector":
                        res.append(
                            f"{dst}.limb{i} = "
                            f"({
                                '|'.join(
                                    f'{src}[{chunk_size} * {position} + {by}] {'<<' if s >= 0 else '>>'} {abs(s)}'
                                    for by, s in distribution[i][0]
                                )
                            }) & {mask}ull;"
                        )
                    elif self.mcr.settings.platform == "arm":
                        res.append(
                            f"{dst}.limb{i} = (uint{self.mcr.settings.vector_lw}x{lanes}_t){{"
                            + ",".join(
                                "("
                                + "|".join(
                                    f"{src}[{chunk_size} * {position} + {by}] {'<<' if s >= 0 else '>>'} {abs(s)}"
                                    for by, s in distribution[i][j]
                                )
                                + f") & {mask}ull"
                                for j in range(lanes)
                            )
                            + "};"
                        )
                    else:
                        raise NotImplementedError()
                return "\n".join(res)
            # Vector load
            case IRInstruction(
                declare,
                IRTemporary(_dsl_type, "matrix") as result,
                "load",
                operands,
            ):
                assert declare, "load temporaries should not be reassigned"
                assert len(operands) > 2
                assert isinstance(operands[0].dsl_type, BufferView), operands[0]
                assert all(isinstance(o, IRConst) for o in operands[2:])
                assert self.mcr.settings.lanes
                assert len(operands[2:]) <= self.mcr.settings.lanes
                offsets: list[int] = [o.value for o in operands[2:]]  # type: ignore
                chunk_size = operands[0].dsl_type.chunk_size
                return self.mcr.get_template(
                    f"vload_{self.mcr.settings.platform}"
                ).render(
                    {
                        "var": self._compile_operand(result),
                        "settings": self.mcr.settings,
                        "buffer": self._compile_operand(operands[0]),
                        "position": self._compile_operand(operands[1]),
                        "offsets": offsets,
                        "chunk_size": chunk_size,
                        "min": min,
                    }
                )
            # const
            case IRInstruction(declare, result, "const", operands):
                res = []
                if declare:
                    res += optional_ctype
                res += f"{self._compile_operand(insn.result)} = "
                if isinstance(operands[0], IRConst) and operands[0].value == 0:
                    res += "{ 0 };"
                else:
                    res += f"{self._compile_operand(operands[0])};"
                return "".join(res)
            # Horizontal add (vectorization)
            case IRInstruction(declare, result, "horiz_add", (src_matrix,)):
                assert declare, "horizontal add should create a new temporary"
                assert result.ir_type == "vector"
                assert src_matrix.ir_type == "matrix"
                cres = self._compile_operand(result)
                csrc = self._compile_operand(src_matrix)
                intrinsic = (
                    f"vaddvq_u{self.mcr.settings.vector_lw}"
                    if self.mcr.settings.platform == "arm"
                    else "FIXME"  # FIXME
                )
                return (
                    f"// {cres} = horiz_add {csrc}\n"
                    f"{self.mcr.compile_ir_type(result.ir_type)} "
                    f"{(cres)};\n"
                    + "\n".join(
                        f"{cres}.limb{i} = {intrinsic}({csrc}.limb{i});"
                        for i in range(self.mcr.settings.limbs)
                    )
                )
            # Scalar if-else -> ternary
            case IRInstruction(False, dst, "copy", (src,)):
                return f"{self._compile_operand(dst)} = {self._compile_operand(src)};"
            case IRInstruction(declare, result, "call", operands):
                assert declare, "calls should not reuse temporaries"
                result_c = self._compile_operand(result)
                function = self._compile_operand(operands[0])
                arguments = [self._compile_operand(o) for o in operands[1:]]
                return (
                    f"{self.mcr.compile_ir_type(result.ir_type)} {result_c} = "
                    f"{function}({', '.join(arguments)});"
                )
            case _:
                # return f"// {insn.insn_name}..."
                raise NotImplementedError(f"{insn!r}")

    def _compile_operand(self, operand: IROperand) -> str:
        match operand:
            case IRConst(_, "scalar", value):
                return str(value)
            case IRConst(
                _,
                "vector" | "matrix" as ir_type,
                value,
            ):
                limb_values = [
                    value >> (i * self.mcr.settings.lambda_)
                    & self.mcr.settings.lambda_mask
                    for i in range(self.mcr.settings.limbs)
                ]
                limb_values[-1] &= self.mcr.settings.lambda_prime_mask
                if ir_type == "vector":
                    return (
                        "(bigint_t) {"
                        + ",".join(f"{lv}ull" for lv in limb_values)
                        + "}"
                    )
                else:
                    # TODO does this work with Intel intrinsics?
                    return (
                        "(vbigint_t) {"
                        + ",".join(
                            f"vdupq_n_u{self.mcr.settings.vector_lw}({lv})"
                            for lv in limb_values
                        )
                        + "}"
                    )
            case IRBoundIdentifier(_, _, name):
                return name
            case IRTemporary():
                return self.temporaries.setdefault(
                    id(operand), f"var{len(self.temporaries)}"
                )
            case _:
                assert_never(operand)  # type: ignore

    def _compile_pf_add_mul(self, insn: IRInstruction) -> str:
        # TODO is mul aliasing-safe?
        assert len(insn.operands) == 2
        assert isinstance(insn.result.dsl_type, PrimeField)
        assert insn.result.ir_type, "vector" or insn.result.ir_type == "matrix"
        te_ctx = {
            "dst": self._compile_operand(insn.result),
            "lhs": self._compile_operand(insn.operands[0]),
            "rhs": self._compile_operand(insn.operands[1]),
            "settings": self.mcr.settings,
        }
        match insn.insn_name, insn.result.ir_type:
            case ("add", "vector"):
                te_name = "add"
            case ("add", "matrix"):
                te_name = f"vadd_{self.mcr.settings.platform}"
            case ("mul", "vector"):
                te_name = f"mul_{self.mcr.settings.mul_algo}"
            case ("mul", "matrix"):
                te_name = (
                    f"vmul_{self.mcr.settings.mul_algo}_{self.mcr.settings.platform}"
                )
            case _:
                assert_never(insn)  # type: ignore
        return self.mcr.get_template(te_name).render(te_ctx)


class ModuleCodeGenerator:
    def __init__(self, module: IRModule, settings: Settings, perf: bool) -> None:
        self.module = module
        self.settings = settings
        self._templates_env = Environment(
            loader=FileSystemLoader("src/codegen/templates")
        )
        self._templates: dict[str, Template] = {}
        self.perf = perf

    def compile(self) -> tuple[str, str, str, str, str | None]:
        declarations: list[str] = []
        definitions: list[str] = []
        perf_function_names: list[str] = []
        for func in self.module.funcs:
            fgen = FunctionCodeGenerator(self, func)
            signature = fgen.generate_signature()
            declarations.append(f"{signature};")
            definitions.append(fgen.generate_definition(func, signature))
            # Check whether function can be perfed
            if (
                len(func.params) == 3
                and func.params[0].ir_type == "pod"  # key
                and func.params[1].ir_type == "pod"  # message
                and func.params[2].ir_type == "scalar"  # n. of blocks
            ):
                perf_function_names.append(func.name)

        context = {
            "declarations": declarations,
            "settings": self.settings,
            "module_name": self.module.name,
            "intrinsics_header": "arm_neon.h"
            if self.settings.platform == "arm"
            else "UNIMPLEMENTED",
            "n_bytes": (self.settings.field.bit_length() + 7) // 8,
            "definitions": definitions,
        }

        header = self.get_template("header").render(context)
        source = self.get_template("source").render(context)
        datastructures_header = self.get_template("datastructures_h").render(context)
        datastructures_source = self.get_template("datastructures_c").render(context)

        perf = (
            self.get_template("perf.c").render(
                {
                    "module_name": self.module.name,
                    "func": self.module.funcs[0].name,
                    "settings": self.settings,
                }
            )
            if self.perf
            else None
        )

        return header, source, datastructures_header, datastructures_source, perf

    def compile_ir_type(self, ir_type: IRType) -> str:
        match ir_type:
            case "scalar":
                return f"uint{self.settings.scalar_mw}_t"
            case "vector":
                return "bigint_t"
            case "matrix":
                return "vbigint_t"
            case "pod":
                return "const uint8_t*"

    def get_template(self, template: str) -> Template:
        return self._templates.setdefault(
            template, self._templates_env.get_template(f"{template}.j2")
        )
