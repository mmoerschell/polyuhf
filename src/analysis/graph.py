import numpy as np
from matplotlib import pyplot as plt, ticker

from settings import Settings


def roofline_plot(
    data_B: list[float],  # noqa: N803
    data_ops: list[float],
    data_traffic: list[float],
    data_cycles: list[float],
    settings: Settings,
) -> None:
    """
    Roofline plot
    https://en.wikipedia.org/wiki/Roofline_model
    """
    bytes_ = settings.field.chunk_size() * np.array(data_B)

    # https://en.wikipedia.org/wiki/Apple_M3
    GBsec = 150
    GHz = 4.05
    bandwidth = GBsec / GHz  # bytes per cycle
    peak_perf = 8

    oi = np.logspace(-3, 3, 1000)  # operational intensity
    roof = np.minimum(peak_perf, bandwidth * oi)

    performance = np.array(data_ops) / np.array(data_cycles)
    intensity = np.array(data_ops) / bytes_
    point_indices = np.arange(len(performance))

    plt.figure(figsize=(8, 6))
    plt.loglog(oi, roof, label="Roofline Bound", color="red", linestyle="--")
    plt.scatter(
        intensity,
        performance,
        c=point_indices,
        cmap="plasma",  # Dark purple (old) -> Pink -> Bright Yellow (new)
        edgecolors="none",
        s=35,  # Size of points
        zorder=5,
    )
    # plt.xlim(0, max_oi)
    # plt.ylim(0, peak_perf * 1.1)
    plt.xscale("log", base=10)
    plt.yscale("log", base=2)
    plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter())
    plt.xlabel("Intensity [iops/byte]")
    plt.ylabel("Performance [iops/cycle]")
    plt.title("Roofline plot")
    # plt.grid(True, which="both", alpha=0.3)
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def cycles_per_byte_plot(
    data_B: list[float],  # noqa: N803
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
    roofline_plot(
        data_B,
        data_ops,
        data_traffic,
        data_cycles,
        settings,
    )
