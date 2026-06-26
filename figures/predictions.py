# pyright: standard
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df_predicted = pd.read_csv("data/predicted_cycles.csv")
df_actual = pd.read_csv("data/hashing_performance/neon_data.csv")


MODULES_FIELDS = [
    ("nmh", (116, 3)),
    ("sqh", (116, 3)),
    ("mmh", (116, 3)),
    ("nmh", (226, 5)),
    ("sqh", (226, 5)),
    ("mmh", (226, 5)),
]

labels = []
actual_values = []
predicted_values = []

for module, (pi, theta) in MODULES_FIELDS:
    last_sample = df_actual[
        (df_actual["module"] == module)
        & (df_actual["pi"] == pi)
        & (df_actual["karatsuba"] == 0)
    ].iloc[-1]
    sample_length = last_sample["length"]
    sample_cycles = last_sample["cycles"]
    actual_cpb = float(sample_cycles / sample_length)
    predicted_cpb = float(
        df_predicted.loc[
            (df_predicted["module"] == module) & (df_predicted["pi"] == pi),
            "predicted_cycles_per_byte",
        ].iloc[0]
    )
    labels.append(f"{module}\nπ={pi}")
    actual_values.append(actual_cpb)
    predicted_values.append(predicted_cpb)

    ratio = (predicted_cpb / actual_cpb - 1) * 100
    print(f"{module} {actual_cpb} {predicted_cpb} {ratio:02}%")

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 4))

bars_predicted = ax.bar(
    x + width / 2,
    predicted_values,
    width,
    label="Predicted",
)

bars_actual = ax.bar(
    x - width / 2,
    actual_values,
    width,
    label="Actual",
)

ax.set_title("Cycles per byte", loc="left")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(bars_predicted, fmt="%.2f", padding=3)
ax.bar_label(bars_actual, fmt="%.2f", padding=3)

fig.tight_layout()
plt.show()
