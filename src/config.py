# pyright: basic
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import tomllib

from settings import (
    BenchSettings,
    RepresentationSettings,
    Settings,
    TargetCPU,
    TestSettings,
)
from typesystem import PrimeField


@dataclass(frozen=True)
class ExperimentConfig:
    settings: Settings
    modules: tuple[Path, ...]
    name: str
    module_dir: Path = Path("modules")
    module_extension: str = ".txt"

    @property
    def build_id(self) -> str:
        field = self.settings.field
        vector = (
            f"v{self.settings.vector_lw}x{self.settings.lanes}"
            if self.settings.vector_lw and self.settings.lanes
            else "scalar"
        )
        stable_payload = {
            "name": self.name,
            "field": str(field),
            "representation": asdict(self.settings.representation),
            "target": asdict(self.settings.target),
            "tests": asdict(self.settings.tests),
            "bench": asdict(self.settings.bench),
            "modules": [
                {
                    "path": str(path),
                    "sha1": hashlib.sha1(
                        path.read_bytes(),
                    ).hexdigest(),
                }
                for path in self.modules
            ],
        }
        digest = hashlib.sha1(
            json.dumps(stable_payload, sort_keys=True).encode()
        ).hexdigest()[:8]
        target_name = self.settings.target.name.replace("-", "_")
        return (
            f"{self.name}_p{field.pi}_t"
            f"{getattr(field, 'theta', 'na')}_l{self.settings.lambda_}_"
            f"{target_name}_{vector}_{digest}"
        )


def module_name_from_path(path: str | Path) -> str:
    module_name = Path(path).stem
    if not module_name:
        raise ValueError(f"Can't find module name in path '{path}'")
    if module_name in ["configuration", "helpers"]:
        raise ValueError(f"Illegal module name '{module_name}'")
    return module_name


def discover_modules(directory: str | Path, extension: str) -> tuple[Path, ...]:
    module_dir = Path(directory)
    suffix = extension if extension.startswith(".") else f".{extension}"
    return tuple(sorted(module_dir.glob(f"*{suffix}")))


def load_toml(path: Path) -> dict[str, object]:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def load_experiment_config(path: str | Path) -> ExperimentConfig:
    config_path = Path(path)
    data = load_toml(config_path)
    for section in ["field", "representation", "target", "tests", "bench"]:
        if section not in data:
            raise ValueError(f"Config '{config_path}' must define [{section}]")
    field = data["field"]
    representation = data["representation"]
    target = data["target"]
    tests = data["tests"]
    bench = data["bench"]
    module_config = data.get("modules", {})
    vector_lw = representation.get("vector_lw")
    lanes = representation.get("lanes")

    settings = Settings(
        PrimeField(int(field["pi"]), int(field["theta"])),
        RepresentationSettings(
            lambda_=int(representation["lambda"]),
            scalar_mw=int(representation.get("scalar_mw", 64)),
            vector_lw=int(vector_lw) if vector_lw is not None else None,
            lanes=int(lanes) if lanes is not None else None,
            unrolling_factor=int(representation.get("unrolling_factor", 2)),
            mul_algo=representation.get("mul_algo", "schoolbook"),
            carry_propagate_limbs=int(representation.get("carry_propagate_limbs", 2)),
        ),
        TargetCPU(
            name=target["name"],
            platform=target["platform"],
            frequency_ghz=float(target["frequency_ghz"]),
            memory_bandwidth_gbs=float(target["memory_bandwidth_gbs"]),
            peak_iops_per_cycle=float(target["peak_iops_per_cycle"]),
            perf_seed=int(target["perf_seed"]),
            perf_warmup_rounds=int(target["perf_warmup_rounds"]),
            perf_measure_rounds=int(target["perf_measure_rounds"]),
            roofline_points=int(target["roofline_points"]),
        ),
        TestSettings(max_B=int(tests["max_B"])),
        BenchSettings(
            start=int(bench["start"]),
            stop=int(bench["stop"]),
            step=int(bench["step"]),
        ),
    )

    module_dir = Path(module_config.get("directory", "modules"))
    extension = module_config.get("extension", ".txt")
    selected_modules = discover_modules(module_dir, extension)
    if not selected_modules:
        raise ValueError(
            f"No module files matching '*{extension}' found in '{module_dir}'"
        )
    return ExperimentConfig(
        settings,
        selected_modules,
        config_path.stem,
        module_dir,
        extension,
    )


def render_field_config_header(settings: Settings) -> str:
    export_bytes = (settings.field.pi + 7) // 8
    prime_hex = settings.field.prime_as_hex()
    return f"""#pragma once

#include <stddef.h>
#include <stdint.h>

#include "datastructures.h"

#define FIELD_PI {settings.field.pi}ull
#define FIELD_THETA {settings.field.theta}ull
#define FIELD_LAMBDA {settings.lambda_}ull
#define FIELD_LAMBDA_PRIME {settings.lambda_prime}ull
#define FIELD_LIMBS {settings.limbs}ull
#define FIELD_CHUNK_SIZE {settings.field.chunk_size()}ull
#define FIELD_EXPORT_BYTES {export_bytes}ull
#define FIELD_PRIME_HEX "{prime_hex}"

static inline void export_field_bytes(uint8_t *dst, const bigint_t *src) {{
    export_{export_bytes}_bytes(dst, src);
}}
"""


def write_field_config_header(output_dir: str | Path, settings: Settings) -> Path:
    output_path = Path(output_dir) / "field_config.h"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_field_config_header(settings), encoding="utf-8")
    return output_path
