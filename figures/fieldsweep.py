# pyright: standard
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_graph(module: str):
    df = pd.read_csv(f"{module}_data.csv")
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
    plt.title(f"Speedup over scalar implementation for {module}")
    plt.tight_layout()
    # if output_path:
    #     output_path.parent.mkdir(parents=True, exist_ok=True)
    #     plt.savefig(output_path, dpi=600)
    # if show:
    plt.ylim(0, 5)
    plt.legend()
    plt.show()
    # plt.close()


def main(argv: list[str]) -> int:
    assert len(argv) == 2
    module = argv[1]
    generate_graph(module)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
