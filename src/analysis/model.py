from ir.ir_nodes import (
    IRFunction,
    IRInstruction,
    IRLoop,
    IRModule,
    IROperand,
    IRStatement,
)
from settings import Settings
from typesystem import PrimeField

MESSAGE_LENGTH = 16000

"""
Reciprocal throughput estimates, in cycles per instruction, for Apple M-series NEON/SIMD

Sources:
- https://dougallj.github.io/applecpu/firestorm-simd.html (primary)
- https://acl.inf.ethz.ch/teaching/fastcode/2025/benchmarking_m_series_apple_cpus.pdf

NOTE: we don't differentiate between cheaper operations (those that are not loads, not
multiplications), and just call them "simple". That includes:
vaddq_u64
vandq_u64
vshrq_n_u64
vshlq_n_u64
vdupq_n_u64
"""

NEON_SIMPLE_TP = 0.25  # from add
NEON_LOAD128_TP = 1.0 / 3.0
NEON_TABLE_TP = 0.25
NEON_WIDEN_MUL_TP = 0.25


def active_vload_limbs(settings: Settings) -> list[tuple[bool, bool]]:
    # Return (active, needs_shift) for each vector-load limb
    chunk_size = settings.field.chunk_size()
    limbs: list[tuple[bool, bool]] = []
    assert settings.vector_lw is not None
    for limb in range(settings.limbs):
        ls_bit_idx = limb * settings.lambda_
        first_byte = ls_bit_idx // 8
        shift_right = ls_bit_idx % 8
        limb_bytes = min(
            (settings.lambda_ + shift_right + 7) // 8,
            settings.vector_lw // 8,
        )
        num_bytes = max(0, min(limb_bytes, chunk_size - first_byte))
        limbs.append((num_bytes > 0, shift_right > 0))
    return limbs


def schoolbook_counts(settings: Settings) -> tuple[int, int]:
    # Return (widening_madds, extra_kappa_muls) for generated schoolbook mul
    limbs = settings.limbs
    madds = limbs * limbs
    folded_terms = limbs * (limbs - 1) // 2
    return madds, folded_terms


def square_counts(settings: Settings) -> tuple[int, int, int]:
    """
    Return (widening_madds, extra_kappa_muls, simple_ops) for square.

    TODO FIXME The source template emits cross terms twice. For now,
    the model assumes LLVM turns a_j*a_k + a_j*a_k into one multiply
    and one simple doubling/shift.
    """
    madds = 0
    folded_madds = 0
    simple_ops = 0
    limbs = settings.limbs

    def count_coeff(h: int) -> tuple[int, int]:
        mul_count = 0
        simple_count = 0
        if h >= 2 * limbs - 1:
            return 0, 0
        for j in range((h // 2) + 1):
            k = h - j
            if j < limbs and k < limbs:
                mul_count += 1
                if j < k:
                    simple_count += 1
        return mul_count, simple_count

    for i in range(limbs):
        regular, regular_simple = count_coeff(i)
        folded, folded_simple = count_coeff(limbs + i)
        madds += regular
        madds += folded
        folded_madds += folded
        simple_ops += regular_simple + folded_simple

    return madds, folded_madds, simple_ops


def mul_pressure(settings: Settings) -> float:
    madds, extra_muls = schoolbook_counts(settings)
    return (madds + extra_muls) * NEON_WIDEN_MUL_TP


def square_pressure(settings: Settings) -> float:
    madds, extra_muls, _ = square_counts(settings)
    return (madds + extra_muls) * NEON_WIDEN_MUL_TP


def square_simple_pressure(settings: Settings) -> float:
    _, _, simple_ops = square_counts(settings)
    return simple_ops * NEON_SIMPLE_TP


def vload_pressures(settings: Settings) -> tuple[float, float, float, float]:
    # Return load/table/simple/mul pressure for one generated vector load
    assert settings.lanes is not None
    load_p = 0.0
    table_p = 0.0
    simple_p = 0.0
    mul_p = 0.0
    for active, needs_shift in active_vload_limbs(settings):
        if not active:
            simple_p += NEON_SIMPLE_TP
            continue
        load_p += settings.lanes * NEON_LOAD128_TP
        table_p += NEON_TABLE_TP
        if needs_shift:
            simple_p += NEON_SIMPLE_TP
        simple_p += NEON_SIMPLE_TP
    return load_p, table_p, simple_p, mul_p


def vcarry_simple_pressure(settings: Settings, field: PrimeField) -> float:
    first_pass = 2 * (settings.limbs - 1) * NEON_SIMPLE_TP
    wrap = NEON_SIMPLE_TP + field.theta.bit_count() * NEON_SIMPLE_TP + NEON_SIMPLE_TP
    second_pass = 2 * settings.carry_propagate_limbs * NEON_SIMPLE_TP
    return first_pass + wrap + second_pass


def performance_model_loop_body(stmts: list[IRStatement], settings: Settings) -> float:  # noqa: C901
    # Pressures
    load_p = 0.0
    table_p = 0.0
    simple_p = 0.0
    mul_p = 0.0
    for stmt in stmts:
        match stmt:
            case IRInstruction(_, IROperand(_, "matrix"), "vload", _):
                load, table, simple, mul = vload_pressures(settings)
                load_p += load
                table_p += table
                simple_p += simple
                mul_p += mul
            case IRInstruction(_, IROperand(_, "matrix"), "vadd", _):
                simple_p += settings.limbs * NEON_SIMPLE_TP
            case IRInstruction(_, IROperand(_, "matrix"), "vmul", _):
                if settings.mul_algo != "schoolbook":
                    raise ValueError("performance model currently assumes schoolbook")
                mul_p += mul_pressure(settings)
            case IRInstruction(_, IROperand(_, "matrix"), "vsquare", _):
                mul_p += square_pressure(settings)
                simple_p += square_simple_pressure(settings)
            case IRInstruction(
                _, IROperand(PrimeField() as field, "matrix"), "vcarry", _
            ):
                simple_p += vcarry_simple_pressure(settings, field)
            case IRInstruction(_, IROperand(_, "matrix"), "copy", _):
                pass
            case IRInstruction(_, IROperand(_, "matrix"), "const", _):
                pass
            # TODO carries
            case IRInstruction(_, _, _, _):
                # Ignore other instructions, negligible impact
                pass
            case _:
                raise ValueError("Can only model pure instruction loops")
    pressures = (load_p, table_p, simple_p, mul_p)
    additive = sum(pressures)
    perfect_pipeline = max(pressures)
    return 0.5 * additive + 0.5 * perfect_pipeline


def performance_model_function(f: IRFunction, settings: Settings) -> float:
    """
    Runtime is dominated by main loop
    We only capture these vectorized operations:
    - load
    - field add
    - field mul/square
    """

    total = 0

    # Find main loop (should be first loop)
    for stmt in f.body:
        if isinstance(stmt, IRLoop):
            cs = settings.field.chunk_size()
            n_blocks = (MESSAGE_LENGTH + cs - 1) / cs  # from codegen
            block_count_param = f.params[2].name
            num_loop_iterations = float(
                stmt.bound.subs(block_count_param, n_blocks).evalf()  # type: ignore
            )
            total += num_loop_iterations * performance_model_loop_body(
                stmt.body, settings
            )
            break
    else:
        raise ValueError("Ir has no loop")

    # Currently omitting scalar tail, store etc.
    # Hopefully negligible at 16KB message length

    return total / MESSAGE_LENGTH


def performance_model(module: IRModule, settings: Settings) -> float | None:
    """
    Estimated cycles per byte on ARM NEON for 16kb messages,
    if and only if the module has exactly one hash function.
    Assumes vectorization and schoolbook multiplication/squaring
    """
    candidate_functions = list(
        filter(
            lambda f: (
                f.is_hash
                and len(f.params) == 3
                and f.params[0].ir_type == "pod"  # key
                and f.params[1].ir_type == "pod"  # message
                and f.params[2].ir_type == "scalar"  # n. of blocks
            ),
            module.funcs,
        )
    )
    if len(candidate_functions) == 1:
        try:
            estimation = performance_model_function(candidate_functions[0], settings)
        except ValueError as _:
            return None
        return estimation
