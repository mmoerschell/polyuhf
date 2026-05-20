from __future__ import annotations

import math
from typing import assert_never

from jinja2 import Environment, FileSystemLoader, Template

import utils
from ir.ir_nodes import (
    IRAssigningInstruction,
    IRBoundIdentifier,
    IRConst,
    IRFunction,
    IRLoop,
    IRModule,
    IROperand,
    IRReturn,
    IRStatement,
    IRTemporary,
)
from typesystem import (
    BufferView,
    IRType,
    IRTypeMatrix,
    IRTypeScalar,
    IRTypeVector,
    PrimeField,
)


class FunctionCodeGenerator:
    def __init__(
        self, module_code_generator: ModuleCodeGenerator, func: IRFunction
    ) -> None:
        self.module_code_generator = module_code_generator
        self.func = func
        self.temporaries: dict[int, str] = {}  # id(IRTemporary) -> C name

    def generate_signature(self) -> str:
        param_names: list[str] = []
        param_ctypes: list[str] = []
        for p in self.func.params:
            param_names.append(p.name)
            param_ctypes.append(self.module_code_generator.compile_ir_type(p.ir_type))
        return (
            f"void {self.func.name}"
            f"({
                ','.join(
                    f'{t} {n}'
                    for n, t in zip(
                        ['output'] + param_names,
                        ['uint8_t*'] + param_ctypes,
                        strict=True,
                    )
                )
            })"
        )

    def generate_definition(self, func: IRFunction, c_signature: str) -> str:
        lines: list[str] = []
        for s in self.func.body:
            text = self._compile_statement(s)
            lines.append(text)
        return f"{c_signature} {{\n{'\n'.join(lines)}\n}}"

    def _compile_statement(self, stmt: IRStatement) -> str:
        match stmt:
            case IRAssigningInstruction():
                return self._compile_instruction(stmt)
            case IRLoop(var, begin, end, increment, body):
                loop_header = (
                    f"for ({self.module_code_generator.compile_ir_type(var.ir_type)} "
                    f"{var.name}={self._compile_operand(begin)};"
                    f"{var.name}<{self._compile_operand(end)};"
                    f"{var.name}+={self._compile_operand(increment)})"
                )
                loop_text = "\n".join(self._compile_statement(s) for s in body)
                return f"{loop_header} {'{'}\n{loop_text}\n{'}'}"
            case IRReturn(value) if isinstance(value.ir_type, IRTypeVector):
                assert value.ir_type.lambd >= 8, "sto. assumptions break for lambda < 8"
                return self.module_code_generator.get_template("store").render(
                    {
                        "dst_ptr": "output",
                        "rhs": self._compile_operand(value),
                        "n_bytes": math.ceil(
                            (
                                value.ir_type.lambd * (value.ir_type.limbs - 1)
                                + value.ir_type.lambd_prime
                            )
                            / 8
                        ),
                        "lambd": value.ir_type.lambd,
                        "limbs": value.ir_type.limbs,
                    }
                )
            case _:
                raise NotImplementedError(f"{stmt!r}")

    def _compile_instruction(self, insn: IRAssigningInstruction) -> str:  # noqa: C901
        optional_ctype = (
            f"{self.module_code_generator.compile_ir_type(insn.result.ir_type)} "
            if id(insn.result) not in self.temporaries
            else ""
        )
        match insn:
            # Scalar operations
            case IRAssigningInstruction(result, operator, operands) if isinstance(
                result.ir_type, IRTypeScalar
            ):
                return (
                    optional_ctype
                    + f"{self._compile_operand(result)} = "
                    + utils.IR_TO_OP_TABLE[operator].join(
                        self._compile_operand(oa) for oa in operands
                    )
                    + ";"
                )
            # Prime field add/mul
            case IRAssigningInstruction(result, "add" | "mul", operands) if isinstance(
                result.dsl_type, PrimeField
            ):
                if len(optional_ctype) > 0:
                    return (
                        f"{optional_ctype}{self._compile_operand(result)} = "
                        + "{0};"
                        + self._compile_pf_add_mul(insn)
                    )
                else:
                    return self._compile_pf_add_mul(insn)
            # Prime field carry
            case IRAssigningInstruction(
                IRTemporary(
                    PrimeField(_, theta),
                    IRTypeVector(
                        mw,
                        limbs,
                        lambd,
                        lambd_prime,
                        lambd_mask,
                        lambd_prime_mask,
                    )
                    | IRTypeMatrix(
                        mw,
                        _,
                        limbs,
                        lambd,
                        lambd_prime,
                        lambd_mask,
                        lambd_prime_mask,
                    ) as ir_type,
                ) as result,
                "carry",
                operands,
            ):
                te_ctx = {
                    "x": self._compile_operand(result),
                    "mw": mw,
                    "limbs": limbs,
                    "lambda": lambd,
                    "lambda_prime": lambd_prime,
                    "lambda_mask": lambd_mask,
                    "lambda_prime_mask": lambd_prime_mask,
                    "theta": theta,
                }
                if isinstance(ir_type, IRTypeMatrix):
                    te_ctx["lanes"] = ir_type.lanes
                    te_name = f"vcarry_{self.module_code_generator.platform}"
                else:
                    te_name = "carry"
                return self.module_code_generator.get_template(te_name).render(te_ctx)
            # Scalar & vector load
            case IRAssigningInstruction(
                IRTemporary(
                    _,
                    IRTypeVector(
                        mw, limbs, lambd, lambd_prime, lambd_mask, lambd_prime_mask
                    )
                    | IRTypeMatrix(
                        mw, _, limbs, lambd, lambd_prime, lambd_mask, lambd_prime_mask
                    ),
                ) as result,
                "load",
                operands,
            ):
                assert lambd >= 8, "assumptions break"
                assert id(result) not in self.temporaries
                assert len(operands) == 2
                assert isinstance(operands[0].dsl_type, BufferView), operands[0]
                if isinstance(result.ir_type, IRTypeMatrix):
                    lanes = result.ir_type.lanes
                else:
                    lanes = 1
                dst = self._compile_operand(result)
                src = self._compile_operand(operands[0])
                position = self._compile_operand(operands[1])
                chunk_size = operands[0].dsl_type.chunk_size
                res: list[str] = [
                    f"/* {dst} = load {src} {position} */",
                    f"{self.module_code_generator.compile_ir_type(result.ir_type)} "
                    f"{dst};",
                ]
                # Figure out which byte affects which limb
                # row x col x [pair(pointer offset, shift)]
                distribution: list[list[list[tuple[int, int]]]] = [
                    [[] for _ in range(lanes)] for _ in range(limbs)
                ]
                for j in range(lanes):
                    for i in range(chunk_size):
                        byte_n = j * chunk_size + i
                        for relevant_limb in {
                            8 * i // lambd,
                            min((8 * i + 7) // lambd, limbs - 1),
                        }:
                            distribution[relevant_limb][j].append(
                                (byte_n, 8 * i - relevant_limb * lambd)
                            )
                for i in range(limbs):
                    mask = lambd_prime_mask if i == limbs - 1 else lambd_mask
                    if lanes == 1:
                        res.append(
                            f"{dst}.limbs[{i}] = "
                            f"({
                                '|'.join(
                                    f'{src}[{chunk_size} * {position} + {by}] {'<<' if s >= 0 else '>>'} {abs(s)}'
                                    for by, s in distribution[i][0]
                                )
                            }) & {mask}ull;"
                        )
                    elif self.module_code_generator.platform == "arm":
                        res.append(
                            f"{dst}.limbs[{i}] = (uint{mw}x{lanes}_t){{"
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
                return "\n".join(res)
            # const
            case IRAssigningInstruction(result, "const", operands):
                return (
                    f"{optional_ctype}{self._compile_operand(insn.result)} = "
                    f"{self._compile_operand(operands[0])};"
                )
            # Horizontal add (vectorization)
            case IRAssigningInstruction(result, "horiz_add", (src_matrix,)):
                assert id(result) not in self.temporaries, "uh-oh"
                assert isinstance(result.ir_type, IRTypeVector)
                assert isinstance(src_matrix.ir_type, IRTypeMatrix)
                cres = self._compile_operand(result)
                csrc = self._compile_operand(src_matrix)
                intrinsic = (
                    f"vaddvq_u{src_matrix.ir_type.machine_width}"
                    if self.module_code_generator.platform == "arm"
                    else "FIXME"  # FIXME
                )
                return (
                    f"// {cres} = horiz_add {csrc}\n"
                    f"{self.module_code_generator.compile_ir_type(result.ir_type)} "
                    f"{(cres)};\n"
                    + "\n".join(
                        f"{cres}.limbs[{i}] = {intrinsic}({csrc}.limbs[{i}]);"
                        for i in range(result.ir_type.limbs)
                    )
                )
            # Scalar if-else -> ternary
            case IRAssigningInstruction(result, "ifelse", (cond, then, else_)):
                declare = id(result) not in self.temporaries
                result_c = self._compile_operand(result)
                cond_c = self._compile_operand(cond)
                then_c = self._compile_operand(then)
                else_c = self._compile_operand(else_)
                res = [f"{result_c} = {cond_c} ? {then_c} : {else_c};"]
                if declare:
                    res.insert(
                        0,
                        f"{self.module_code_generator.compile_ir_type(result.ir_type)} {result_c};",
                    )
                return "\n".join(res)
            # Call bigint functions
            case IRAssigningInstruction(result, "call", operands) if not isinstance(
                result.ir_type, IRTypeScalar
            ):
                declare = id(result) not in self.temporaries
                result_c = self._compile_operand(result)
                function = self._compile_operand(operands[0])
                arguments = [self._compile_operand(o) for o in operands[1:]]
                call_stmt : list[str]= []
                if declare:
                    call_stmt.append(
                        f"{self.module_code_generator.compile_ir_type(result.ir_type)} {result_c};"
                    )
                call_stmt.append(f"{function}({', '.join([result_c] + arguments)});")
                return "\n".join(call_stmt)
            case _:
                # return f"// {insn.insn_name}..."
                raise NotImplementedError(f"{insn!r}")

    def _compile_operand(self, operand: IROperand) -> str:
        match operand:
            case IRConst(_, IRTypeScalar(), value):
                return str(value)
            case IRConst(
                _,
                IRTypeVector(mw, limbs, _, lambd, _, lambd_mask)
                | IRTypeMatrix(mw, _, limbs, _, lambd, _, lambd_mask) as ir_type,
                value,
            ):
                limb_values = [
                    value & (lambd_mask << (i * lambd)) for i in range(limbs)
                ]
                if isinstance(ir_type, IRTypeVector):
                    return "{" + ",".join(f"{lv}" for lv in limb_values) + "}"
                else:
                    # TODO does this work with Intel intrinsics?
                    return (
                        "{"
                        + ",".join(f"vdupq_n_u{mw}({lv})" for lv in limb_values)
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

    def _compile_pf_add_mul(self, insn: IRAssigningInstruction) -> str:
        # TODO is mul aliasing-safe?
        assert len(insn.operands) == 2
        assert isinstance(insn.result.dsl_type, PrimeField)
        assert isinstance(insn.result.ir_type, IRTypeVector) or isinstance(
            insn.result.ir_type, IRTypeMatrix
        )
        theta = insn.result.dsl_type.theta
        kappa = theta * (
            1 << (insn.result.ir_type.lambd - insn.result.ir_type.lambd_prime)
        )
        te_ctx = {
            "dst": self._compile_operand(insn.result),
            "lhs": self._compile_operand(insn.operands[0]),
            "rhs": self._compile_operand(insn.operands[1]),
            "machine_width": insn.result.ir_type.machine_width,
            "limbs": insn.result.ir_type.limbs,
            "kappa": kappa,
        }
        match insn.insn_name, insn.result.ir_type:
            case ("add", IRTypeVector()):
                te_name = "add"
            case ("add", IRTypeMatrix(mw, lanes, _)):
                te_ctx["mw"] = mw
                te_ctx["lanes"] = lanes
                te_name = f"vadd_{self.module_code_generator.platform}"
            case ("mul", IRTypeVector()):
                te_name = "mul"
            case ("mul", IRTypeMatrix(mw, lanes, _)):
                te_ctx["mw"] = mw
                te_ctx["lanes"] = lanes
                te_name = f"vmul_{self.module_code_generator.platform}"
            case _:
                assert_never(insn)  # type: ignore
        return self.module_code_generator.get_template(te_name).render(te_ctx)


class ModuleCodeGenerator:
    def __init__(self, module: IRModule, platform: str) -> None:
        self.module = module
        self._templates_env = Environment(
            loader=FileSystemLoader("src/codegen/templates")
        )
        self._templates: dict[str, Template] = {}
        self.custom_types: dict[IRType, tuple[str, str]] = {}  # type -> (def x name)
        self.platform = platform

    def compile(self) -> tuple[str, str]:
        declarations: list[str] = []
        definitions: list[str] = []
        for func in self.module.funcs:
            fgen = FunctionCodeGenerator(self, func)
            signature = fgen.generate_signature()
            declarations.append(f"{signature};")
            definitions.append(fgen.generate_definition(func, signature))

        header = self.get_template("header").render(
            {
                "declarations": declarations,
            }
        )

        source = self.get_template("source").render(
            {
                "intrinsics_header": "arm_neon.h"
                if self.platform == "arm"
                else "UNIMPLEMENTED",
                "module_name": self.module.name,
                "custom_types": self.custom_types,
                "definitions": definitions,
            }
        )

        return header, source

    def compile_ir_type(self, ir_type: IRType) -> str:
        match ir_type:
            case IRTypeScalar(machine_width):
                return f"int{machine_width}_t"
            case IRTypeVector(machine_width, limbs, _):
                return self.custom_types.setdefault(
                    ir_type,
                    (
                        self.get_template("bigint").render(
                            {
                                "machine_width": machine_width,
                                "limbs": limbs,
                            }
                        ),
                        f"bigint_t{len(self.custom_types) + 1}",
                    ),
                )[1]
            case IRTypeMatrix(machine_width, lanes, limbs, _):
                return self.custom_types.setdefault(
                    ir_type,
                    (
                        self.get_template(f"bigint_{self.platform}").render(
                            {
                                "machine_width": machine_width,
                                "lanes": lanes,
                                "limbs": limbs,
                            }
                        ),
                        f"bigint_t{len(self.custom_types) + 1}",
                    ),
                )[1]
            case "pod":
                return "uint8_t*"

    def get_template(self, template: str) -> Template:
        return self._templates.setdefault(
            template, self._templates_env.get_template(f"{template}.j2")
        )
