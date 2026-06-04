import re
import subprocess
import tempfile
from pathlib import Path

CFLAGS = [
    "-Wall",
    "-Wextra",
    "-Wpedantic",
    "-O3",
    "-mcpu=native",
    "-march=armv8.2-a+simd+dotprod",
    "-DNDEBUG",
    "-fno-vectorize",
    "-fno-slp-vectorize",
]

GENERATED_CODE_DIR = "src/cpp/generated"


def compile_and_run(
    module_name: str, start: int, end: int, step: int
) -> tuple[str, str]:
    library = Path(f"{GENERATED_CODE_DIR}/{module_name}.c")
    perf = Path(f"{GENERATED_CODE_DIR}/{module_name}_perf.c")

    with tempfile.TemporaryDirectory() as tmpdir:
        binary = Path(tmpdir) / f"{perf.stem}"

        subprocess.run(
            [
                "clang",
                *CFLAGS,
                str(library),
                str(perf),
                "-o",
                str(binary),
            ],
            check=True,
        )

        result = subprocess.run(
            [str(binary), str(start), str(end), str(step)],
            check=True,
            capture_output=True,
            text=True,
        )

        return result.stdout, result.stderr


def gather_cycles(
    module_name: str, start: int, end: int, step: int
) -> tuple[list[float], list[float]]:
    stdout, _stderr = compile_and_run(module_name, start, end, step)
    pattern = re.compile(r"B = ([0-9]+) -> ([0-9]+(\..*)?) cycles")
    data_B: list[float] = []  # noqa: N806
    data_cycles: list[float] = []
    for match in pattern.finditer(stdout):
        data_B.append(float(match.group(1)))
        data_cycles.append(float(match.group(2)))
    return data_B, data_cycles
