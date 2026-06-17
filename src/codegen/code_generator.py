from __future__ import annotations

from collections.abc import Iterable
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
    IRStore,
    IRTemporary,
)
from settings import Settings
from typesystem import (
    Buffer,
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
        if self.func.is_hash:
            key = self.func.params[0].name
            message = self.func.params[1].name
            return (
                f"void {self.func.name}"
                f"(uint8_t* output, uint8_t* {key}, uint8_t* {message}, "
                "size_t buffer_length)"
            )
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
            f"{self.mcr.compile_ir_type(self.func.ir_return_type)} "
            f"{self.func.name}({args_c})"
        )

    def generate_definition(self, func: IRFunction, c_signature: str) -> str:
        lines: list[str] = []
        if self.mcr.settings.lanes:
            lines += [
                f"const {self.mcr.compile_vector_type()} vlambda_mask = "
                f"{self.mcr.compile_vector_splat(self.mcr.settings.lambda_mask)};",
                f"const {self.mcr.compile_vector_type()} vlambda_prime_mask = "
                f"{self.mcr.compile_vector_splat(self.mcr.settings.lambda_prime_mask)};",
            ]
        if self.func.is_hash:
            len_name = self.func.params[2].name
            lines.append(
                f"const uint64_t {len_name} = "
                "(buffer_length + FIELD_CHUNK_SIZE - 1) / FIELD_CHUNK_SIZE;"
            )
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
            case IRIfElse(condition, then_branch, else_branch, constant_time):
                then_text = "\n".join(self._compile_statement(s) for s in then_branch)
                if constant_time:
                    assert else_branch is not None
                    else_text = "\n".join(
                        self._compile_statement(s) for s in else_branch
                    )
                    cond = self._compile_operand(condition)
                    return (
                        f"/* constant-time if ({cond}) then */\n"
                        f"{then_text}\n"
                        f"/* constant-time if ({cond}) else */\n"
                        f"{else_text}"
                    )
                if else_branch is None:
                    return f"if ({self._compile_operand(condition)}) {{{then_text}}}"
                else_text = "\n".join(self._compile_statement(s) for s in else_branch)
                return (
                    f"if ({self._compile_operand(condition)}) {{{then_text}}} "
                    f"else {{{else_text}}}"
                )
            case IRReturn(value):
                return f"return {self._compile_operand(value)};"
            case IRStore(value):
                return self.mcr.get_template("store").render(
                    {
                        "dst": "output",
                        "src": self._compile_operand(value),
                        "settings": self.mcr.settings,
                        "n_bytes": (self.mcr.settings.field.pi + 7) // 8,
                    }
                )

    def _compile_instruction(self, insn: IRInstruction) -> str:  # noqa: C901
        optional_ctype = f"{self.mcr.compile_ir_type(insn.result.ir_type)} "
        match insn:
            case IRInstruction(declare, result, "select", (condition, then_, else_)):
                return self._compile_select(declare, result, condition, then_, else_)
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
            # Prime field arithmetic
            case IRInstruction(
                declare,
                result,
                "add" | "vadd" | "mul" | "vmul" | "square" | "vsquare",
                operands,
            ) if isinstance(result.dsl_type, PrimeField):
                if declare:
                    return (
                        f"{optional_ctype}{self._compile_operand(result)} = "
                        + "{0};"
                        + "\n"
                        + self._compile_pf_arithmetic(insn)
                    )
                else:
                    return self._compile_pf_arithmetic(insn)
            # Prime field carry
            case IRInstruction(
                declare,
                IRTemporary(
                    PrimeField(),
                    "vector" | "matrix",
                ) as result,
                "carry" | "vcarry",
                operands,
            ):
                assert not declare, "carries should reuse temporaries"
                te_ctx = {  # type: ignore
                    "x": self._compile_operand(result),
                    "settings": self.mcr.settings,
                    "shr": (lambda a, b: a >> b),  # type: ignore
                    "bitand": (lambda a, b: a & b),  # type: ignore
                    "propagate_limbs": self.mcr.settings.carry_propagate_limbs,
                }
                te_name = insn.insn_name
                if insn.insn_name == "vcarry":
                    te_name = f"vcarry_{self.mcr.settings.platform}"
                return self.mcr.get_template(te_name).render(te_ctx)
            # Prime overflow
            case IRInstruction(
                False,
                IRTemporary(
                    PrimeField(),
                    "vector",
                ) as result,
                "full_reduction",
                _,
            ):
                return self.mcr.get_template("full_reduction").render(
                    {
                        "x": self._compile_operand(result),
                        "settings": self.mcr.settings,
                        "shr": (lambda a, b: a >> b),  # type: ignore
                        "shl": (lambda a, b: a << b),  # type: ignore
                        "bitand": (lambda a, b: a & b),  # type: ignore
                    }
                )
            # Scalar load
            case IRInstruction(
                declare,
                IRTemporary(_, "vector") as result,
                "load",
                operands,
            ):
                assert declare, "load temporaries should not be reassigned"
                assert len(operands) >= 2
                assert isinstance(operands[0].dsl_type, Buffer), operands[0]
                assert all(isinstance(o, IRConst) for o in operands[2:])
                lanes = self.mcr.settings.lanes or 1
                assert len(operands[2:]) <= lanes
                dst = self._compile_operand(result)
                src = self._compile_operand(operands[0])
                position = self._compile_operand(operands[1])
                offsets: list[int] = [o.value for o in operands[2:]]  # type: ignore
                chunk_size = self.mcr.settings.field.chunk_size()
                res: list[str] = [
                    self._comment(dst, "load", src, "@", position, "offsets", offsets),
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
                        terms = self._load_terms(
                            src,
                            chunk_size,
                            position,
                            distribution[i][0],
                        )
                        res.append(f"{dst}.limb{i} = ({terms}) & {mask}ull;")
                    elif self.mcr.settings.platform in {"neon", "avx2"}:
                        res.append(
                            f"{dst}.limb{i} = "
                            + self.mcr.compile_vector_literal(
                                "("
                                + self._load_terms(
                                    src,
                                    chunk_size,
                                    position,
                                    distribution[i][j],
                                )
                                + f") & {mask}ull"
                                for j in range(lanes)
                            )
                            + ";"
                        )
                    else:
                        raise NotImplementedError()
                return "\n".join(res)
            # Vectorized load
            case IRInstruction(
                declare,
                IRTemporary(_dsl_type, "matrix") as result,
                "vload",
                operands,
            ):
                assert declare, "vload temporaries should not be reassigned"
                assert len(operands) > 2
                assert isinstance(operands[0].dsl_type, Buffer), operands[0]
                assert all(isinstance(o, IRConst) for o in operands[2:])
                assert self.mcr.settings.lanes
                assert len(operands[2:]) <= self.mcr.settings.lanes
                offsets: list[int] = [o.value for o in operands[2:]]  # type: ignore
                return self.mcr.get_template(
                    f"vload_{self.mcr.settings.platform}"
                ).render(
                    {
                        "var": self._compile_operand(result),
                        "settings": self.mcr.settings,
                        "buffer": self._compile_operand(operands[0]),
                        "position": self._compile_operand(operands[1]),
                        "offsets": offsets,
                        "chunk_size": self.mcr.settings.field.chunk_size(),
                        "min": min,
                        "max": max,
                    }
                )
            # const
            case IRInstruction(declare, result, "splat", (src,)):
                assert declare, "splat should create a new temporary"
                assert result.ir_type == "matrix"
                dst = self._compile_operand(result)
                return (
                    f"{self.mcr.compile_ir_type(result.ir_type)} {dst};\n"
                    + "\n".join(
                        f"{dst}.limb{i} = "
                        f"{self._compile_vector_splat_expr(limb_expr)};"
                        for i in range(self.mcr.settings.limbs)
                        for limb_expr in [self._field_limb_expr(src, i)]
                    )
                )
            case IRInstruction(declare, result, "lane_powers", operands):
                assert declare, "lane_powers should create a new temporary"
                assert result.ir_type == "matrix"
                assert len(operands) == self.mcr.settings.lanes
                dst = self._compile_operand(result)
                return (
                    f"{self.mcr.compile_ir_type(result.ir_type)} {dst};\n"
                    + "\n".join(
                        f"{dst}.limb{i} = "
                        + self.mcr.compile_vector_literal(
                            self._field_limb_expr(operand, i) for operand in operands
                        )
                        + ";"
                        for i in range(self.mcr.settings.limbs)
                    )
                )
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
                def hadd_expr(vector: str) -> str:
                    if self.mcr.settings.platform == "neon":
                        return f"vaddvq_u{self.mcr.settings.vector_lw}({vector})"
                    if self.mcr.settings.platform == "avx2":
                        return self._avx2_horiz_add(vector)
                    raise NotImplementedError(
                        f"horizontal add for {self.mcr.settings.platform}"
                    )

                return (
                    f"{self._comment(cres, 'horiz_add', csrc)}\n"
                    f"{self.mcr.compile_ir_type(result.ir_type)} "
                    f"{(cres)};\n"
                    + "\n".join(
                        f"{cres}.limb{i} = {hadd_expr(f'{csrc}.limb{i}')};"
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

    def _load_terms(
        self,
        src: str,
        chunk_size: int,
        position: str,
        distribution: list[tuple[int, int]],
    ) -> str:
        if not distribution:
            return "0ull"
        return "|".join(
            self._load_shift_expr(src, chunk_size, position, by, shift)
            for by, shift in distribution
        )

    def _compile_select(
        self,
        declare: bool,
        result: IRTemporary,
        condition: IROperand,
        then_: IROperand,
        else_: IROperand,
    ) -> str:
        dst = self._compile_operand(result)
        cond = self._compile_operand(condition)
        then_c = self._compile_operand(then_)
        else_c = self._compile_operand(else_)
        ctype = self.mcr.compile_ir_type(result.ir_type)
        declaration = f"{ctype} {dst};\n" if declare else ""
        mask = f"{dst}_mask"
        lines = [
            declaration,
            "{",
            # Oldest trick in the book
            f"uint64_t {mask} = (uint64_t)0 - (uint64_t)(({cond}) != 0);",
        ]
        if result.ir_type == "scalar":
            lines.append(f"{dst} = (({then_c}) & {mask}) | (({else_c}) & ~{mask});")
        elif result.ir_type == "vector":
            for i in range(self.mcr.settings.limbs):
                lines.append(
                    f"{dst}.limb{i} = ((({then_c}).limb{i}) & {mask}) | "
                    f"((({else_c}).limb{i}) & ~{mask});"
                )
        else:
            raise NotImplementedError("select for matrix temporaries")
        lines.append("}")
        return "\n".join(line for line in lines if line)

    def _comment(self, dst: str, insn_name: str, *operands: object) -> str:
        operand_text = " ".join(
            ", ".join(str(x) for x in operand)
            if isinstance(operand, list)
            else str(operand)
            for operand in operands
        )
        return f"/* {dst} = {insn_name} {operand_text} */".rstrip()

    def _load_shift_expr(
        self, src: str, chunk_size: int, position: str, byte: int, shift: int
    ) -> str:
        direction = "<<" if shift >= 0 else ">>"
        return f"{src}[{chunk_size} * {position} + {byte}] {direction} {abs(shift)}"

    def _avx2_horiz_add(self, src: str) -> str:
        return (
            f"(uint64_t)_mm256_extract_epi64({src}, 0) + "
            f"(uint64_t)_mm256_extract_epi64({src}, 1) + "
            f"(uint64_t)_mm256_extract_epi64({src}, 2) + "
            f"(uint64_t)_mm256_extract_epi64({src}, 3)"
        )

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
                    return (
                        "(vbigint_t) {"
                        + ",".join(
                            self.mcr.compile_vector_splat(lv)
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

    def _field_limb_expr(self, operand: IROperand, limb: int) -> str:
        match operand:
            case IRConst(_, "vector" | "matrix", value):
                mask = (
                    self.mcr.settings.lambda_prime_mask
                    if limb == self.mcr.settings.limbs - 1
                    else self.mcr.settings.lambda_mask
                )
                return str((value >> (limb * self.mcr.settings.lambda_)) & mask)
            case IRConst(_, "scalar", _):
                raise TypeError("scalar constants do not have field limbs")
            case _:
                return f"{self._compile_operand(operand)}.limb{limb}"

    def _compile_vector_splat_expr(self, value: str) -> str:
        match self.mcr.settings.platform:
            case "neon":
                return f"vdupq_n_u{self.mcr.settings.vector_lw}({value})"
            case "avx2":
                return f"_mm256_set1_epi64x((long long)({value}))"
            case _:
                raise NotImplementedError(
                    f"platform {self.mcr.settings.platform!r} has no vector splat"
                )

    def _compile_pf_arithmetic(self, insn: IRInstruction) -> str:
        # TODO is mul aliasing-safe?
        assert len(insn.operands) in {1, 2}
        assert isinstance(insn.result.dsl_type, PrimeField)
        assert insn.result.ir_type, "vector" or insn.result.ir_type == "matrix"
        te_ctx = {
            "dst": self._compile_operand(insn.result),
            "lhs": self._compile_operand(insn.operands[0]),
            "rhs": self._compile_operand(insn.operands[1])
            if len(insn.operands) > 1
            else None,
            "settings": self.mcr.settings,
            "kappa_shifts": [
                shift
                for shift in range(self.mcr.settings.kappa.bit_length())
                if (self.mcr.settings.kappa >> shift) & 1
            ],
        }
        match insn.insn_name, insn.result.ir_type:
            case ("add", "vector"):
                te_name = "add"
            case ("vadd", "matrix"):
                te_name = f"vadd_{self.mcr.settings.platform}"
            case ("mul", "vector"):
                te_name = f"mul_{self.mcr.settings.mul_algo}"
            case ("vmul", "matrix"):
                te_name = (
                    f"vmul_{self.mcr.settings.mul_algo}_{self.mcr.settings.platform}"
                )
            case ("square", "vector"):
                te_name = "square_schoolbook"
            case ("vsquare", "matrix"):
                te_name = f"vsquare_schoolbook_{self.mcr.settings.platform}"
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
            if func.is_hash:
                signature = fgen.generate_signature()
                declarations.append(f"{signature};")
                definitions.append(fgen.generate_definition(func, signature))
                perf_function_names.append(func.name)
            else:
                signature = fgen.generate_signature()
                declarations.append(f"{signature};")
                definitions.append(fgen.generate_definition(func, signature))

        context = {
            "declarations": declarations,
            "settings": self.settings,
            "module_name": self.module.name,
            "intrinsics_header": self.compile_intrinsics_header(),
            "vector_type": self.compile_vector_type() if self.settings.lanes else None,
            "n_bytes": (self.settings.field.pi + 7) // 8,
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
                    "func": perf_function_names[0],
                    "settings": self.settings,
                }
            )
            if self.perf and perf_function_names
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

    def compile_intrinsics_header(self) -> str:
        match self.settings.platform:
            case "neon":
                return "arm_neon.h"
            case "avx2":
                return "immintrin.h"
            case _:
                raise NotImplementedError(
                    f"platform {self.settings.platform!r} has no intrinsics header"
                )

    def compile_vector_type(self) -> str:
        match self.settings.platform:
            case "neon":
                return f"uint{self.settings.vector_lw}x{self.settings.lanes}_t"
            case "avx2":
                return "__m256i"
            case _:
                raise NotImplementedError(
                    f"platform {self.settings.platform!r} has no vector type"
                )

    def compile_vector_splat(self, value: int) -> str:
        match self.settings.platform:
            case "neon":
                return f"vdupq_n_u{self.settings.vector_lw}({value})"
            case "avx2":
                return f"_mm256_set1_epi64x((long long){value}ull)"
            case _:
                raise NotImplementedError(
                    f"platform {self.settings.platform!r} has no vector splat"
                )

    def compile_vector_literal(self, lanes: Iterable[object]) -> str:
        lane_list = list(lanes)
        match self.settings.platform:
            case "neon":
                return (
                    f"({self.compile_vector_type()}){{"
                    + ",".join(str(lane) for lane in lane_list)
                    + "}"
                )
            case "avx2":
                if len(lane_list) != 4:
                    raise NotImplementedError("AVX2 vector literals need four lanes")
                return (
                    "_mm256_set_epi64x("
                    + ",".join(
                        f"(long long)({lane})" for lane in reversed(lane_list)
                    )
                    + ")"
                )
            case _:
                raise NotImplementedError(
                    f"platform {self.settings.platform!r} has no vector literal"
                )

    def get_template(self, template: str) -> Template:
        return self._templates.setdefault(
            template, self._templates_env.get_template(f"{template}.j2")
        )
