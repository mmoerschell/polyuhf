from jinja2 import Environment, FileSystemLoader

from parsing.ast.ast_builder import (
    ASTBinaryOperation,
    ASTBufferViewRead,
    ASTCall,
    ASTComparison,
    ASTFunction,
    ASTIfElse,
    ASTInt,
    ASTLocalIdentifier,
    ASTModule,
    ASTReduction,
    ASTUnaryMinus,
)
from parsing.ast.ast_nodes import ASTNode
from settings import Settings
from typesystem import BufferView, DSLType, Field, Index


class BoostCppTestEmitter:
    def __init__(self, module_name: str, settings: Settings, max_B: int):  # noqa: N803
        self.module_name = module_name
        self.settings = settings
        self.max_B = max_B
        self.indent_level = 0
        self.template = Environment(
            loader=FileSystemLoader("src/automatic_tests")
        ).get_template("autotests.j2")

    def _indent(self):
        return "    " * self.indent_level

    def _to_cpp_type(self, ttype: DSLType) -> str:
        """Maps DSL types to C++ types for the test harness."""
        match ttype:
            case Index():
                return "int64_t"
            case Field():
                return "boost::multiprecision::cpp_int"
            case BufferView():
                return "const uint8_t*"

    def generate(self, module: ASTModule) -> str:
        code = [
            "#include <cstdint>",
            "#include <boost/multiprecision/cpp_int.hpp>",
            "#include <boost/test/data/monomorphic.hpp>",
            "#include <boost/test/data/test_case.hpp>",
            "#include <boost/test/unit_test.hpp>",
            "",
            '#include "datastructures.h"',
            f'#include "{self.module_name}.h"',
            "",
        ]

        for func in module.functions:
            if (
                len(func.params) == 3
                and isinstance(func.params[0][1], BufferView)
                and isinstance(func.params[1][1], BufferView)
                and isinstance(func.params[2][1], Index)
                and isinstance(func.return_type, Field)
            ):
                # only test functions that have signature message, key, B -> FE
                code.append(self.visit(func))

        return "\n".join(code)

    def visit(self, node: ASTNode) -> str:
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: ASTNode) -> str:
        raise NotImplementedError(f"No C++ emission defined for {type(node).__name__}")

    # ---------- Expressions ----------

    def visit_ASTInt(self, node: ASTInt) -> str:
        if isinstance(node.ttype, Index):
            return f"{node.value}"
        return f'boost::multiprecision::cpp_int("{node.value}")'

    def visit_ASTLocalIdentifier(self, node: ASTLocalIdentifier) -> str:
        return node.name

    def visit_ASTUnaryMinus(self, node: ASTUnaryMinus) -> str:
        return f"(-{self.visit(node.operand)})"

    def visit_ASTBinaryOperation(self, node: ASTBinaryOperation) -> str:
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.operator == "^":
            if isinstance(node.ttype, Field):
                return f"boost::multiprecision::powm({left}, {right}, prime)"
            else:
                raise NotImplementedError("C integer pow")

        return f"({left} {node.operator} {right})"

    def visit_ASTComparison(self, node: ASTComparison) -> str:
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"({left} {node.operator} {right})"

    def visit_ASTIfElse(self, node: ASTIfElse) -> str:
        cond = self.visit(node.condition)
        then_b = self.visit(node.then_branch)
        else_b = self.visit(node.else_branch)
        return f"(({cond}) ? ({then_b}) : ({else_b}))"

    def visit_ASTCall(self, node: ASTCall) -> str:
        args = ", ".join([self.visit(arg) for arg in node.args])
        return f"{node.func_name}_reference({args})"

    def visit_ASTBufferViewRead(self, node: ASTBufferViewRead) -> str:
        buffer = self.visit(node.buffer)
        index = self.visit(node.index)
        return f"load_from_buffer({buffer}, {index})"

    def visit_ASTReduction(self, node: ASTReduction) -> str:
        assert node.ttype
        acc_type = self._to_cpp_type(node.ttype)

        if isinstance(node.ttype, Index):
            init_val = "0" if node.op == "+" else "1"
        else:
            init_val = f'{acc_type}("0")' if node.op == "+" else f'{acc_type}("1")'

        start = self.visit(node.start)
        stop = self.visit(node.stop)
        step = self.visit(node.step)

        self.indent_level += 1
        ind1 = self._indent()
        self.indent_level += 1
        ind2 = self._indent()

        body = self.visit(node.body)

        self.indent_level -= 2
        ind_base = self._indent()

        # Execute reduction using an Immediately Invoked Function Expression (IIFE)
        return (
            f"[&]() -> {acc_type} {{\n"
            f"{ind1}{acc_type} _acc = {init_val};\n"
            f"{ind1}for(int64_t {node.var} = {start}; {node.var} < {stop}; "
            f"{node.var} += {step}) {{\n"
            f"{ind2}_acc = (_acc {node.op} {body}) % prime;\n"
            f"{ind1}}}\n"
            f"{ind1}return _acc;\n"
            f"{ind_base}}}()"
        )

    # ---------- Functions ----------

    def visit_ASTFunction(self, node: ASTFunction) -> str:
        params: list[str] = []
        for name, ttype in node.params:
            cpp_type = self._to_cpp_type(ttype)
            params.append(f"{cpp_type} {name}")

        return self.template.render(
            {
                "function_name": node.name,
                "param_str": ", ".join(params),
                "ret_type": self._to_cpp_type(node.return_type),
                "body_str": self.visit(node.body),
                "settings": self.settings,
                "B_max": self.max_B,
            }
        )
