# pyright: standard
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_graph(module: str, platform: str, save: bool):
    df = pd.read_csv(f"data/fieldsweep/{module}_{platform}_data.csv")
    scalar_sb = df[df["mode"] == "scalar_schoolbook"]
    scalar_ka = df[df["mode"] == "scalar_karatsuba"]
    vec_schoolbook = df[df["mode"] == "vector_schoolbook"]
    vec_karatsuba = df[df["mode"] == "vector_karatsuba"]

    plt.figure(figsize=(8, 6))
    plt.scatter(
        np.array(scalar_sb["pi"]),
        np.array(scalar_sb["cycles"]) / np.array(vec_schoolbook["cycles"]),
        label="Schoolbook",
    )
    plt.scatter(
        np.array(scalar_ka["pi"]),
        np.array(scalar_ka["cycles"]) / np.array(vec_karatsuba["cycles"]),
        label="Karatsuba",
    )
    plt.xlabel("Pi")
    plt.ylabel("Cycles")
    plt.title(
        f"Speedup over scalar code, 16kb, {module} on {platform.upper()}"
    )
    plt.tight_layout()
    plt.legend()
    if save:
        path = f"figures/field_speedup_16kb_{platform}_{module}.png"
        plt.savefig(path, dpi=300)
        print(f"Wrote figure to '{path}'")
    else:
        plt.show()
    plt.close()


def main(argv: list[str]) -> int:
    assert len(argv) in {3, 4}, f"usage: {argv[0]} <module> <platform> [save]"
    module = argv[1]
    platform = argv[2]
    save = len(argv) == 4 and argv[3] == "save"
    generate_graph(module, platform, save)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
