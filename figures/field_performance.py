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

    fastest = df.groupby("pi")["cycles"].min().to_numpy()

    performance = fastest / 16000  # cycles per byte

    plt.figure(figsize=(8, 6))
    # plt.scatter(
    #     np.array(scalar_sb["pi"]),
    #     np.array(performance),
    #     label=module,
    # )
    plt.scatter(
        np.array(vec_schoolbook["pi"]),
        np.array(vec_schoolbook["cycles"]) / 16000.0,
        label="schoolbook"
    )
    plt.scatter(
        np.array(vec_karatsuba["pi"]),
        np.array(vec_karatsuba["cycles"]) / 16000.0,
        label="karatsuba"
    )
    plt.xlabel("Pi")
    plt.ylabel("Cycles / byte")
    plt.legend()
    plt.title(f"Performance across fields, 16kb, {module} on {platform.upper()}")
    plt.tight_layout()
    if save:
        path = (
            f"figures/field_performance_16kb_"
            f"{platform}_{module}.png"
        )
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
