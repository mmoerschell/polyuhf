from ir.c_like.c_nodes import CProgram
from ir.types import Type

INTEGER_TYPE = "int64_t"
BIGINT_TYPE = "void*"


def codegen(p: CProgram) -> str:
    output = ["#import <stdint.h>", ""]
    for f in p.functions:
        ctype = INTEGER_TYPE if f.return_type == Type.INDEX else "void"
        params = ",".join([
            f"{INTEGER_TYPE if ty == Type.INDEX else BIGINT_TYPE} {nm}"
            for ty, nm in f.parameters
        ])
        output.append(f"{ctype} {f.name}({params})"+"{")
    output.append("}")
    return "\n".join(output)
