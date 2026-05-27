from typing import Literal

from typesystem import Field, PrimeField


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
    align: int
    mul_algo: Literal["schoolbook", "karatsuba"]
    carry_every_n: int | None

    def __init__(
        self,
        field: Field,
        lambda_: int,
        platform: Literal["arm", "sse", "avx", "avx512"],
        scalar_mw: int,
        vector_lw: int | None,
        lanes: int | None,
        mul_algo: Literal["schoolbook", "karatsuba"],
        carry_every_n: int,
    ) -> None:
        assert lambda_ >= 8, "limbs must be at least one byte"
        assert lambda_ <= scalar_mw // 2
        if vector_lw:
            assert lambda_ <= vector_lw // 2
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
        self.align = (
            self.vector_lw * self.lanes
            if self.vector_lw and self.lanes
            else self.scalar_mw
        )
        self.mul_algo = mul_algo
        self.carry_every_n = carry_every_n

        # check kappa overflow
        if self.kappa:
            # TODO derive a bound
            mw = self.vector_lw or self.scalar_mw
            assert 2 * self.lambda_ + self.kappa.bit_length() < mw - 2
