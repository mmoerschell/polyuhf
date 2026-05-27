import subprocess

CLANG_TIDY = "/opt/homebrew/opt/llvm/bin/clang-tidy"
CLANG_FORMAT = "/opt/homebrew/opt/llvm/bin/clang-format"


def tidy_and_format_c(path: str) -> None:
    try:
        # clang-tidy: semantic cleanup
        subprocess.run(
            [
                CLANG_TIDY,
                path,
                "-checks=readability-redundant-parentheses",
                "-fix",
                "-fix-errors",
                "-format-style=none",
                "--",
                "-std=c23",
                "-x",
                "c",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        # clang-format: layout cleanup
        subprocess.run(
            [CLANG_FORMAT, "-i", path],
            check=True,
            capture_output=True,
            text=True,
        )

    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"[clang pipeline failed]\n{e.stdout}\n{e.stderr}",  # type: ignore
        ) from e
