import subprocess
import sys

from colorama import Fore, Style

CLANG_FORMAT_BINARY = "clang-format-mp-21"


def format_c_code(unformatted: str) -> str:
    try:
        # TODO add flags "-style=Google" or "-style=file"
        result = subprocess.run(
            [CLANG_FORMAT_BINARY],
            input=unformatted,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout

    except FileNotFoundError:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] clang-format binary not found",
            file=sys.stderr,
        )
        return unformatted

    except subprocess.CalledProcessError as e:
        print(
            f"[{Fore.RED}-{Style.RESET_ALL}] clang-format "
            f"failed with error:\n{e.stderr}",
            file=sys.stderr,
        )
        return unformatted
