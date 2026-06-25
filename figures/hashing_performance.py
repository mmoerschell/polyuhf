# pyright: basic
import sys

import matplotlib as mpl
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MODULES = [
    "mmh",
    "nmh",
    "sqh",
    "hkm_iter",
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
                "legend.fontsize": 10,
                "xtick.labelsize": 10,
                "ytick.labelsize": 10,
            }
        )


    df = pd.read_csv(f"data/hashing_performance/{platform}_data.csv")

    for pi, theta in FIELDS:
        for karatsuba, mul_algo_label in enumerate(["schoolbook", "Karatsuba"]):
            plt.figure(figsize=(8, 6))
            for module in MODULES:
                filtered_lines = df[
                    (df["pi"] == pi)
                    & (df["karatsuba"] == karatsuba)
                    & (df["module"] == module)
                ]
                bytes_ = np.array(filtered_lines["length"])
                kilobytes = bytes_ / 1000.0
                cycles = np.array(filtered_lines["cycles"])
                cycles_per_byte = cycles / bytes_
                filtered_label = module.replace("_", " ")
                plt.scatter(kilobytes, cycles_per_byte, label=f"{filtered_label}")

            plt.xlabel("Message length [KB]")
            plt.ylabel("Cycles per Byte")
            plt.legend()
            title = (
                f"Hashing performance on {platform.upper()} "
                f"in GF(2^{pi}-{theta}), using "
                f"{mul_algo_label} multiplication"
            )
            plt.title(title)
            plt.grid(True, which="both", alpha=0.3)
            plt.tight_layout()
            filename = (
                f"hashing_performance_gf_{platform}_{pi}-{theta}_{mul_algo_label}"
            )
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
