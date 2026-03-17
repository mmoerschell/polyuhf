import subprocess

CLANG_TIDY = "clang-tidy-mp-21"
CLANG_FORMAT = "clang-format-mp-21"


def tidy_and_format_c(path: str) -> None:
    try:
        # clang-tidy: semantic cleanup
        subprocess.run(
            [
                CLANG_TIDY,
                path,
                "-checks=readability-redundant-parentheses",
                "-fix",
                "-format-style=none",
                "--",
                "-std=c++23",
                "-x",
                "c++",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        # clang-format: layout cleanup
        subprocess.run(
            [
                CLANG_FORMAT,
                "-i",
                path
            ],
            check=True,
            capture_output=True,
            text=True,
        )

    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"[clang pipeline failed]\n{e.stdout}\n{e.stderr}",  # type: ignore
        ) from e
