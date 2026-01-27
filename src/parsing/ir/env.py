from dataclasses import dataclass

from .nodes import IRNode


@dataclass
class Env:
    vars: dict[str, IRNode]
