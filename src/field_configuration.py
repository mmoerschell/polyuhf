import math
from dataclasses import dataclass
from typing import Union

from jinja2 import Environment, FileSystemLoader

BUILTIN_BIGINT_FUNCTIONS = {
    "+": "_bigint_add",
    "*": "_bigint_mul",
    "^": "_bigint_exp",
    "carry_round": "_bigint_carry_round",
    "print": "_bigint_print",
}


@dataclass(frozen=True)
class PrimeField:
    pi: int
    theta: int
    # GF(2^pi-theta)


@dataclass(frozen=True)
class BinaryField:
    n: int
    # GF(2^n)


Field = Union[PrimeField, BinaryField]


@dataclass(frozen=True)
class FieldConfiguration:
    field: Field
    bitwidth: int
    limbs: int
    lambda_: int
    lambda_prime: int
    lambda_mask: int
    lambda_prime_mask: int
    kappa: int | None

    @classmethod
    def from_field(cls, field: Field, lambda_: int):
        match field:
            case PrimeField(pi, _):
                bitwidth = pi
            case BinaryField(n):
                bitwidth = n
        limbs = math.ceil(bitwidth / lambda_)
        lambda_prime = (
            (bitwidth - 1) % lambda_ + 1
        )  # sets lambda = lambda_prime if remainderless division is possible
        lambda_mask = (1 << lambda_) - 1
        lambda_prime_mask = (1 << lambda_prime) - 1
        kappa = (
            field.theta * (1 << (lambda_ - lambda_prime))
            if isinstance(field, PrimeField)
            else None
        )
        return cls(
            field=field,
            bitwidth=bitwidth,
            limbs=limbs,
            lambda_=lambda_,
            lambda_prime=lambda_prime,
            lambda_mask=lambda_mask,
            lambda_prime_mask=lambda_prime_mask,
            kappa=kappa,
        )

    def as_code(self) -> str:
        match self.field:
            case PrimeField():
                template = "src/templates/scalar_prime_field_ops.j2"
            case BinaryField():
                template = None
                raise NotImplementedError()
        data = {"config": self, "builtins": BUILTIN_BIGINT_FUNCTIONS}
        env = Environment(
            loader=FileSystemLoader("."),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        env.globals["hex"] = hex  # type: ignore
        output = env.get_template(template).render(data)
        assert isinstance(output, str)
        return output
