import math
from dataclasses import dataclass
from typing import Literal

from typesystem import PrimeField

Platform = Literal["neon", "avx2"]
MulAlgo = Literal["schoolbook", "karatsuba"]


@dataclass(frozen=True)
class PrimeFieldSettings:
    field: PrimeField


@dataclass(frozen=True)
class RepresentationSettings:
    lambda_: int
    scalar_mw: int
    vector_lw: int | None
    lanes: int | None
    unrolling_factor: int
    mul_algo: MulAlgo
    carry_propagate_limbs: int


@dataclass(frozen=True)
class TargetCPU:
    name: str
    platform: Platform
    frequency_ghz: float
    memory_bandwidth_gbs: float
    peak_iops_per_cycle: float
    perf_seed: int
    perf_warmup_rounds: int
    perf_measure_rounds: int
    roofline_points: int


@dataclass(frozen=True)
class TestSettings:
    max_B: int  # noqa: N815


@dataclass(frozen=True)
class BenchSettings:
    start: int
    stop: int
    step: int


class Settings:
    field_settings: PrimeFieldSettings
    representation: RepresentationSettings
    target: TargetCPU
    tests: TestSettings
    bench: BenchSettings
    field: PrimeField
    lambda_: int
    lambda_prime: int
    lambda_mask: int
    lambda_prime_mask: int
    limbs: int
    kappa: int | None
    platform: Platform
    scalar_mw: int
    vector_lw: int | None  # lane bit width
    lanes: int | None
    unrolling_factor: int
    align: int
    mul_algo: MulAlgo
    carry_propagate_limbs: int

    def __init__(
        self,
        field_settings: PrimeFieldSettings,
        representation: RepresentationSettings,
        target: TargetCPU,
        tests: TestSettings,
        bench: BenchSettings,
    ) -> None:
        assert representation.lambda_ >= 8, "limbs must be at least one byte"
        if representation.lanes:
            assert representation.lanes > 1
        self.field_settings = field_settings
        self.representation = representation
        self.target = target
        self.tests = tests
        self.bench = bench
        self.field = field_settings.field
        self.lambda_ = representation.lambda_
        self.lambda_prime = self.field.pi % self.lambda_ or self.lambda_
        self.lambda_mask = (1 << self.lambda_) - 1
        self.lambda_prime_mask = (1 << self.lambda_prime) - 1
        self.limbs = (self.field.pi + self.lambda_ - 1) // self.lambda_
        self.kappa = self.field.theta * (1 << (self.lambda_ - self.lambda_prime))
        self.platform = target.platform
        self.scalar_mw = representation.scalar_mw
        self.vector_lw = representation.vector_lw
        self.lanes = representation.lanes
        self.unrolling_factor = representation.unrolling_factor
        self.carry_propagate_limbs = representation.carry_propagate_limbs
        self.align = (
            self.vector_lw * self.lanes
            if self.vector_lw and self.lanes
            else self.scalar_mw
        )
        self.mul_algo = representation.mul_algo

        # Sanity checks
        if self.mul_algo == "karatsuba":
            assert self.limbs >= 2, "Karatsuba multiplication needs at least 2 limbs"
        assert 0 <= self.carry_propagate_limbs < self.limbs, (
            "carry_propagate_limbs must be in [0, limbs)"
        )
        if self.vector_lw and self.platform == "neon":
            assert self.vector_lw * self.lanes == 128, (  # type: ignore
                "Number of width of lanes misconfigured for NEON"
            )  # type: ignore
        if self.vector_lw and self.platform == "avx2":
            assert self.vector_lw == 64 and self.lanes == 4, (  # type: ignore
                "AVX2 backend currently expects four 64-bit lanes"
            )  # type: ignore

        # Constraints from CHES paper
        w = self.vector_lw or self.scalar_mw
        assert (
            2 * self.lambda_
            + (self.lambda_ - self.lambda_prime)
            + math.ceil(math.log2(self.field.theta))
            + math.ceil(math.log2(self.limbs))
            < w  # NOTE notation differs from paper
        ), "Inequation (9) failed"
        if self.mul_algo == "schoolbook":
            assert (
                2 * self.lambda_
                - self.lambda_prime
                + math.ceil(math.log2(self.field.theta))
                < w // 2  # NOTE notation differs from paper
            ), "Inequation (10) failed"
