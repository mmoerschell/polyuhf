from dataclasses import dataclass
from typing import List

# ---------- Base nodes ----------

class ASTNode:
    pass

class Expr(ASTNode):
    pass

# ---------- Program structure ----------

@dataclass
class Program(ASTNode):
    functions: List["Function"]

@dataclass
class Function(ASTNode):
    name: str
    params: List[str]
    body: Expr
