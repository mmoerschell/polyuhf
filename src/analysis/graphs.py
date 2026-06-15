from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from settings import Settings


def cycles_per_byte_plot(
    name: str,
    data_bytes: list[float],
    data_ops: list[float],
    data_traffic: list[float],
    data_cycles: list[float],
    settings: Settings,
    output_path: Path | None = None,
    show: bool = False,
) -> None:
    """
    CHES Figure 7-style plot
    """
    bytes_ = np.array(data_bytes)
    cycles_per_byte = np.array(data_cycles) / bytes_

    plt.figure(figsize=(8, 6))
    plt.scatter(bytes_, cycles_per_byte)
    # plt.xscale("log")
    # plt.yscale("log")
    plt.xlabel("Message length in bytes")
    plt.ylabel("Cycles / Byte")
    plt.title(f"Hashing performance for {name}")
    plt.grid(True, which="both", alpha=0.3)
    plt.tight_layout()
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=600)
    if show:
        plt.show()
    plt.close()


def field_sweep_cycles_per_byte_plot(
    module: str,
    samples: list[dict[str, object]],
    output_path: Path | None = None,
    show: bool = False,
) -> None:
    samples = sorted(
        samples,
        key=lambda sample: (
            int(sample["field_pi"]),
            int(sample["field_theta"]),
            str(sample["config"]),
        ),
    )
    labels = [
        f"p{sample['field_pi']}-t{sample['field_theta']}" for sample in samples
    ]
    x = np.arange(len(samples))
    cycles_per_byte = np.array(
        [float(sample["cycles"]) / float(sample["bytes"]) for sample in samples]
    )

    plt.figure(figsize=(8, 6))
    plt.plot(x, cycles_per_byte, marker="o")
    plt.xticks(x, labels, rotation=30, ha="right")
    plt.xlabel("Field")
    plt.ylabel("Cycles / Byte")
    plt.title(f"Field sweep for {module}")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=600)
    if show:
        plt.show()
    plt.close()


def graphs(
    name: str,
    data_bytes: list[float],
    data_ops: list[float],
    data_traffic: list[float],
    data_cycles: list[float],
    settings: Settings,
    output_dir: str | Path | None = None,
    show: bool = False,
) -> None:
    output_dir = Path(output_dir) if output_dir else None
    cycles_per_byte_plot(
        name,
        data_bytes,
        data_ops,
        data_traffic,
        data_cycles,
        settings,
        output_dir / f"{name}_cycles_per_byte.png" if output_dir else None,
        show,
    )
