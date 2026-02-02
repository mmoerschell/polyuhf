from dataclasses import dataclass

from .nodes import FunctionSignature, IRVar


@dataclass
class Env:
    vars: dict[str, IRVar]
    signatures: dict[str, FunctionSignature]
