# pyright: basic
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MODULES = [
    "mmh",
    "nmh",
    "sqh",
    # "hkm_iter",
]

FIELDS = [
    (116, 3),
    (226, 5),
]


def main(argv: list[str]) -> int:
    assert len(argv) in {2, 3}, f"Usage: {argv[0]} <platform> [save]"
    platform = argv[1]
    save = len(argv) == 3 and argv[2] == "save"

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
                cycles = np.array(filtered_lines["cycles"])
                cycles_per_byte = cycles / bytes_
                plt.scatter(bytes_, cycles_per_byte, label=f"{module}")

            plt.xlabel("Message length in bytes")
            plt.ylabel("Cycles / Byte")
            plt.legend()
            title = (
                f"Hashing performance on {platform.upper()} "
                f"in GF(2^{pi}-{theta}), using "
                f"{mul_algo_label} multiplication"
            )
            plt.title(title)
            plt.grid(True, which="both", alpha=0.3)
            plt.tight_layout()
            if save:
                path = (
                    f"figures/hashing_performance_gf_"
                    f"{platform}_{pi}-{theta}_{mul_algo_label}.png"
                )
                plt.savefig(path, dpi=300)
                print(f"Wrote figure to '{path}")
            else:
                plt.show()
            plt.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
