# pyright: basic
import sys

import matplotlib as mpl
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MODULES = [
    "nmh",
    "sqh",
    "mmh",
]

FIELDS = [
    (116, 3),
    (226, 5),
]


def main(argv: list[str]) -> int:
    assert (
        len(argv) == 3
        and argv[1] in {"neon", "avx2"}
        and argv[2] in {"show", "png", "latex"}
    ), f"Usage: {argv[0]} <platform> <show|png|latex>"
    platform = argv[1]
    output = argv[2]
    if output == "latex":
        mpl.rcParams.update(
            {
                "font.size": 11,
                "axes.labelsize": 11,
                "legend.fontsize": 11,
                "xtick.labelsize": 11,
                "ytick.labelsize": 11,
                "font.family": "sans-serif",
                "pgf.rcfonts": False,
                "pgf.texsystem": "pdflatex",
            }
        )

    df = pd.read_csv(f"data/hashing_performance/{platform}_data.csv")

    for pi, theta in FIELDS:
        plt.figure(figsize=(8, 5))

        # Style setup
        ax = plt.gca()
        for spine in ["top", "right", "left"]:
            ax.spines[spine].set_visible(False)  # hide lines
        ax.yaxis.set_ticks_position("left")  # keep ticks on the left
        ax.tick_params(axis="y", length=0)
        ax.set_facecolor("#eeeeee")  # plot/graph area background
        ax.grid(axis="y", color="white")  # white horizontal grid
        ax.set_axisbelow(True)  # grid behind bars

        for karatsuba, mul_algo_label in enumerate(["schoolbook", "Karatsuba"]):
            for module in MODULES:
                if module == "sqh":
                    if karatsuba == 0:
                        mul_algo_label = "schoolbook-squaring"
                    else:
                        # SQH uses squaring, Karatsuba-multiplication has no effect there.
                        continue

                filtered_lines = df[
                    (df["pi"] == pi)
                    & (df["karatsuba"] == karatsuba)
                    & (df["module"] == module)
                ]
                bytes_ = np.array(filtered_lines["length"])
                kilobytes = bytes_ / 1000.0
                cycles = np.array(filtered_lines["cycles"])
                cycles_per_byte = cycles / bytes_
                label = f"{module} ({mul_algo_label})".replace("_", " ")
                is_highlight = (module, karatsuba) == ("nmh", 0)
                plt.plot(
                    kilobytes,
                    cycles_per_byte,
                    label=f"{label}",
                    lw=3.0 if is_highlight else 1.5,
                    alpha=1.0 if is_highlight else 0.7,
                    zorder=10 if is_highlight else 1,
                )

        plt.legend()
        plt.xlabel("Message length [KB]")
        plt.title(
            "Cycles per byte", loc="left"
        )  # Prof. Püschel style. This is actually the y label
        plt.tight_layout()
        filename = f"hashing_performance_gf_{platform}_{pi}-{theta}"
        if output == "show":
            plt.show()
        elif output == "png":
            path = f"figures/{filename}.png"
            plt.savefig(path, dpi=300)
            print(f"Wrote figure to '{path}")
        elif output == "latex":
            path = f"report/import_figures/{filename}.pgf"
            plt.savefig(path)
            print(f"Wrote figure to '{path}")
        plt.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
