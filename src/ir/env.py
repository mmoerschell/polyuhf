from dataclasses import dataclass

from .nodes import FunctionSignature, IRVar


@dataclass
class Env:
    # Invariant: Env.vars is append-only except when
    # entering a new lexical scope (reduction)
    vars: dict[str, IRVar]
    signatures: dict[str, FunctionSignature]
