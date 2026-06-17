import math

from typesystem import PrimeField


class Settings:
    field: PrimeField
    lambda_: int
    lambda_prime: int
    lambda_mask: int
    lambda_prime_mask: int
    limbs: int
    kappa: int | None
    platform: str
    scalar_mw: int
    vector_lw: int | None  # lane bit width
    lanes: int | None
    unrolling_factor: int
    align: int
    mul_algo: str
    carry_propagate_limbs: int
    limb_realignment: str
    full_reduction_passes: int

    def __init__(
        self,
        pi: int,
        theta: int,
        vectorize: bool,
        platform: str,
        karatsuba: bool,
        unrolling_factor: int,
        limb_realignment: str = "partial",
    ) -> None:
        if limb_realignment not in {"partial", "full"}:
            raise ValueError("limb_realignment must be either 'partial' or 'full'")
        match platform:
            case "avx2":
                self.configure(
                    pi,
                    theta,
                    64,
                    64 if vectorize else None,
                    4 if vectorize else None,
                    "avx2",
                    "karatsuba" if karatsuba else "schoolbook",
                    unrolling_factor,
                    2,
                    limb_realignment,
                )
            case "neon":
                self.configure(
                    pi,
                    theta,
                    64,
                    64 if vectorize else None,
                    2 if vectorize else None,
                    "neon",
                    "karatsuba" if karatsuba else "schoolbook",
                    unrolling_factor,
                    2,
                    limb_realignment,
                )
            case _:
                raise NotImplementedError(self.platform)

    def configure(
        self,
        pi: int,
        theta: int,
        scalar_mw: int,
        vector_lw: int | None,
        lanes: int | None,
        platform: str,
        mul_algo: str,
        unrolling_factor: int,
        carry_propagate_limbs: int,
        limb_realignment: str,
    ) -> None:

        self.field = PrimeField(pi, theta)
        self.scalar_mw = scalar_mw
        self.vector_lw = vector_lw
        self.lanes = lanes
        self.platform = platform
        self.mul_algo = mul_algo
        self.unrolling_factor = unrolling_factor
        self.carry_propagate_limbs = carry_propagate_limbs
        self.limb_realignment = limb_realignment
        self.full_reduction_passes = (
            4 if limb_realignment == "full" else 2
        )  # TODO good ol heuristic
        if self.lanes:
            assert self.lanes > 1
        # Autotune lambda
        w = min(self.scalar_mw, self.vector_lw or self.scalar_mw)
        for candidate_lambda in range(8, w):
            self._set_lambda_limbs_kappa(candidate_lambda)
            if not self._constraints(w):
                self._set_lambda_limbs_kappa(candidate_lambda - 1)
                break
        assert self.lambda_ >= 8, "limbs must be at least one byte"
        self.align = (
            self.vector_lw * self.lanes
            if self.vector_lw and self.lanes
            else self.scalar_mw
        )

        # Sanity checks
        if self.mul_algo == "karatsuba":
            assert self.limbs >= 2, "Karatsuba multiplication needs at least 2 limbs"
        assert 0 <= self.carry_propagate_limbs < self.limbs, (
            "carry_propagate_limbs must be in [0, limbs)"
        )
        if self.vector_lw and self.platform == "neon":
            assert self.vector_lw * self.lanes == 128, (  # type: ignore
                "Number or width of lanes misconfigured for NEON"
            )  # type: ignore
        if self.vector_lw and self.platform == "avx2":
            assert self.vector_lw == 64 and self.lanes == 4, (  # type: ignore
                "AVX2 backend expects four 64-bit lanes"
            )  # type: ignore

        w = self.vector_lw or self.scalar_mw

    def _set_lambda_limbs_kappa(self, candidate_lambda: int):
        assert self.field
        self.lambda_ = candidate_lambda
        self.lambda_prime = self.field.pi % self.lambda_ or self.lambda_
        self.lambda_mask = (1 << self.lambda_) - 1
        self.lambda_prime_mask = (1 << self.lambda_prime) - 1
        self.limbs = (self.field.pi + self.lambda_ - 1) // self.lambda_
        self.kappa = self.field.theta * (1 << (self.lambda_ - self.lambda_prime))

    def _constraints(self, w: int) -> bool:
        # Constraints from CHES paper
        return (
            2 * self.lambda_
            + (self.lambda_ - self.lambda_prime)
            + math.ceil(math.log2(self.field.theta))
            + math.ceil(math.log2(self.limbs))
            < w  # NOTE notation differs from paper
            # Inequation (9)
        ) and (
            2 * self.lambda_
            - self.lambda_prime
            + math.ceil(math.log2(self.field.theta))
            < w // 2  # NOTE notation differs from paper
            # Inequation (10)
        )
