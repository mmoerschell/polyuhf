from dataclasses import dataclass

from ir.high_level.nodes import FunctionSignature, IRVar


@dataclass
class Env:
    # Invariant: Env.vars is append-only except when
    # entering a new lexical scope (reduction)
    vars: dict[str, IRVar]
    signatures: dict[str, FunctionSignature]
