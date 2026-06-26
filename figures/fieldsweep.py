# pyright: basic
import sys

import matplotlib as mpl
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MESSAGE_LENGTH = 16000

MODULES = [
    # "nmh",
    # "sqh",
    "mmh",
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

    df = pd.read_csv(f"data/fieldsweep/{platform}_data.csv")
    pi = df["pi"].unique()

    for module in MODULES:
        # Performance
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
        for karatsuba, mul_algo_label in enumerate(["Schoolbook", "Karatsuba"]):
            if module == "sqh":
                if karatsuba == 0:
                    mul_algo_label = "Schoolbook-squaring"
                else:
                    # SQH uses squaring, Karatsuba-multiplication has no effect there.
                    continue

            filtered_lines = df[
                (df["module"] == module)
                & (df["vectorize"] == 1)
                & (df["karatsuba"] == karatsuba)
            ]
            cycles = np.array(filtered_lines["cycles"])
            cycles_per_byte = cycles / MESSAGE_LENGTH
            label = f"{mul_algo_label}".replace("_", " ")
            plt.scatter(pi, cycles_per_byte, label=f"{label}")

        plt.legend()
        plt.xlabel("$\\pi$")
        plt.title(
            "Cycles per byte", loc="left"
        )  # Prof. Püschel style. This is actually the y label
        plt.tight_layout()
        filename = f"fieldsweep_performance_{platform}_{module}"
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

        # Speedup
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
        for karatsuba, mul_algo_label in enumerate(["Schoolbook", "Karatsuba"]):
            if module == "sqh":
                if karatsuba == 0:
                    mul_algo_label = "Schoolbook-squaring"
                else:
                    # SQH uses squaring, Karatsuba-multiplication has no effect there.
                    continue

            scalar_cycles, vector_cycles = (
                np.array(
                    df[
                        (df["module"] == module)
                        & (df["vectorize"] == v)
                        & (df["karatsuba"] == karatsuba)
                    ]["cycles"]
                )
                for v in [0, 1]
            )
            speedup = scalar_cycles / vector_cycles
            label = f"{mul_algo_label}".replace("_", " ")
            plt.scatter(pi, speedup, label=f"{label}")

        plt.legend(
            loc="center",
            bbox_to_anchor=(2 / 3, 1 / 3 + 0.01),
        )
        plt.axhline(y=1, color="gray", linestyle="--", zorder=1)
        plt.xlabel("$\\pi$")
        plt.title(
            "Speedup over respective scalar code", loc="left"
        )  # Prof. Püschel style. This is actually the y label
        plt.tight_layout()
        filename = f"fieldsweep_speedup_{platform}_{module}"
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
