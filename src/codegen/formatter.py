import os
import subprocess
import sys
import tempfile

import colorama

CLANG_TIDY = "clang-tidy-mp-21"
CLANG_FORMAT = "clang-format-mp-21"


def tidy_and_format_c(code: str) -> str:
    fd, path = tempfile.mkstemp(suffix=".c")
    try:
        # write generated code
        with os.fdopen(fd, "w") as f:
            f.write(code)

        # clang-tidy: semantic cleanup
        subprocess.run(
            [
                CLANG_TIDY,
                path,
                "-checks=readability-redundant-parentheses",
                "-fix",
                "-format-style=none",
                "--",
                "-x",
                "c",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        # # clang-format: layout cleanup
        subprocess.run(
            [CLANG_FORMAT, "-i", path],
            check=True,
            capture_output=True,
            text=True,
        )

        # read back result
        with open(path) as f:
            return f.read()

    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        print(
            f"[{colorama.Fore.RED}-{colorama.Style.RESET_ALL}] "
            f"[clang pipeline failed] {e}",
            file=sys.stderr,
        )
        return code

    finally:
        os.unlink(path)
