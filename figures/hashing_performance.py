# pyright: basic
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


MODULES = [
    "mmh",
    "nmh",
    "sqh",
    "hkm_iter",
    "poly1305",
]

FIELDS = [
    (116, 3),
    (226, 5),
]


def main(argv: list[str]) -> int:
    platform = argv[1]

    df = pd.read_csv(f"data/hashing_performance/{platform}_data.csv")

    for pi, theta in FIELDS:
        for karatsuba in range(2):
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
            plt.title(f"Hashing performance in GF(2^{pi}-{theta})")
            plt.grid(True, which="both", alpha=0.3)
            plt.tight_layout()
            plt.show()
            plt.close()
    return 0


if __name__ == "__main__":
    assert len(sys.argv) == 2, f"Usage: {sys.argv[0]} <platform>"
    raise SystemExit(main(sys.argv))
