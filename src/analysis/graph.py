import numpy as np
from matplotlib import pyplot as plt

from settings import Settings


def cycles_per_byte_plot(
    data_B,
    data_ops: list[float],
    data_traffic: list[float],
    data_cycles: list[float],
    settings: Settings,
) -> None:
    """
    CHES Figure 7-style plot
    """
    bytes_ = settings.field.chunk_size() * np.array(data_B)
    cycles_per_byte = np.array(data_cycles) / bytes_

    plt.figure(figsize=(8, 6))
    plt.scatter(bytes_, cycles_per_byte)
    # plt.xscale("log")
    # plt.yscale("log")
    plt.xlabel("Bytes")
    plt.ylabel("Cycles / Byte")
    plt.title("Memory Cost")
    plt.grid(True, which="both", alpha=0.3)
    plt.tight_layout()
    plt.show()


def graphs(
    data_B: list[float],  # noqa: N803
    data_ops: list[float],
    data_traffic: list[float],
    data_cycles: list[float],
    settings: Settings,
) -> None:
    cycles_per_byte_plot(
        data_B,
        data_ops,
        data_traffic,
        data_cycles,
        settings,
    )
