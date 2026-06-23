# pyright: standard
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_graph(module: str, platform: str):
    df = pd.read_csv(f"data/fieldsweep/{module}_{platform}_data.csv")
    scalar_sb = df[df["mode"] == "scalar_schoolbook"]
    scalar_ka = df[df["mode"] == "scalar_karatsuba"]
    vec_schoolbook = df[df["mode"] == "vector_schoolbook"]
    vec_karatsuba = df[df["mode"] == "vector_karatsuba"]

    fastest = df.groupby("pi")["cycles"].min().to_numpy()

    performance = fastest / 16000  # cycles per byte

    plt.figure(figsize=(8, 6))
    plt.scatter(
        np.array(scalar_sb["pi"]),
        np.array(performance),
        label=module,
    )
    plt.xlabel("Pi")
    plt.ylabel("Cycles / byte")
    plt.title(f"Hashing performance across fields for {module}")
    plt.tight_layout()
    plt.legend()
    plt.show()
    plt.close()


def main(argv: list[str]) -> int:
    assert len(argv) == 3, f"usage: {argv[0]} <module> <platform>"
    module = argv[1]
    platform = argv[2]
    generate_graph(module, platform)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
