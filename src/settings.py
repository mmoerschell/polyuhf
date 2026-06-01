import math
from typing import Literal

from typesystem import BinaryField, Field, PrimeField


class Settings:
    field: Field
    lambda_: int
    lambda_prime: int
    lambda_mask: int
    lambda_prime_mask: int
    limbs: int
    kappa: int | None
    platform: Literal["arm", "sse", "avx", "avx512"]
    scalar_mw: int
    vector_lw: int | None  # lane bit width
    lanes: int | None
    unrolling_factor: int
    align: int
    mul_algo: Literal["schoolbook", "karatsuba"]

    def __init__(
        self,
        field: Field,
        lambda_: int,
        platform: Literal["arm", "sse", "avx", "avx512"],
        scalar_mw: int,
        vector_lw: int | None,
        lanes: int | None,
        unrolling_factor: int,
        mul_algo: Literal["schoolbook", "karatsuba"],
    ) -> None:
        assert lambda_ >= 8, "limbs must be at least one byte"
        if lanes:
            assert lanes > 1
        self.field = field
        self.lambda_ = lambda_
        self.lambda_prime = self.field.bit_length() % self.lambda_ or self.lambda_
        self.lambda_mask = (1 << self.lambda_) - 1
        self.lambda_prime_mask = (1 << self.lambda_prime) - 1
        self.limbs = (self.field.bit_length() + self.lambda_ - 1) // self.lambda_
        self.kappa = (
            self.field.theta * (1 << (self.lambda_ - self.lambda_prime))
            if isinstance(self.field, PrimeField)
            else None
        )
        self.platform = platform
        self.scalar_mw = scalar_mw
        self.vector_lw = vector_lw
        self.lanes = lanes
        self.unrolling_factor = unrolling_factor
        self.align = (
            self.vector_lw * self.lanes
            if self.vector_lw and self.lanes
            else self.scalar_mw
        )
        self.mul_algo = mul_algo

        # Constraints from CHES paper
        if isinstance(self.field, PrimeField):
            w = self.vector_lw or self.scalar_mw
            assert (
                2 * self.lambda_
                + (self.lambda_ - self.lambda_prime)
                + math.ceil(math.log2(self.field.theta))
                + math.ceil(math.log2(self.limbs))
                < w  # NOTE notation differs from paper
            ), "Inequation (9) failed"
            assert (
                2 * self.lambda_
                - self.lambda_prime
                + math.ceil(math.log2(self.field.theta))
                < w // 2  # NOTE notation differs from paper
            ), "Inequation (10) failed"
        elif isinstance(self.field, BinaryField):
            raise NotImplementedError("Limb size constraints for binary fields")
