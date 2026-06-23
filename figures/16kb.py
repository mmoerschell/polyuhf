# pyright: basic
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.concat(
    [pd.read_csv("data/16kb/neon_data.csv"), pd.read_csv("data/16kb/avx2_data.csv")],
    ignore_index=True,
)

print(df)

neon=df[df["platform"] == "neon"]
avx2=df[df["platform"] == "avx2"]

print(np.array(avx2["cycles"]) / np.array(neon["cycles"]))

"""
plt.figure(figsize=(8, 6))

for module, unroll in MODULES_UNROLL:
    df = pd.read_csv(
        f"data/hashing_performance/neon_{module}_{PI}_{THETA}_kara1_ur{unroll}_data.csv"
    )
    bytes_ = np.array(df["bytes"])
    cycles = np.array(df["cycles"])
    cycles_per_byte = cycles / bytes_
    plt.scatter(bytes_, cycles_per_byte, label=f"{module}")


plt.xlabel("Message length in bytes")
plt.ylabel("Cycles / Byte")
plt.legend()
plt.title(f"Hashing performance in GF(2^{PI}-{THETA})")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.show()
plt.close()
"""
