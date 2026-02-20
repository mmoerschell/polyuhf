from dataclasses import dataclass

from ir.typed.typed_nodes import TFunctionSignature, TVar


@dataclass
class Env:
    # Invariant: Env.vars is append-only except when
    # entering a new lexical scope (reduction)
    vars: dict[str, TVar]
    signatures: dict[str, TFunctionSignature]
