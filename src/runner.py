#!/usr/bin/env python3
# pyright: standard

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from argparse import Namespace
from pathlib import Path

from compiler import compile_file
from config import (
    ExperimentConfig,
    load_experiment_config,
    module_name_from_path,
)

AnalysisResult = tuple[object, object, object]
AnalysisByModule = dict[str, AnalysisResult]


def generated_dir(config: ExperimentConfig, build_root: Path) -> Path:
    return build_root / config.build_id / "generated"


def cmake_build_dir(config: ExperimentConfig, build_root: Path) -> Path:
    return build_root / config.build_id / "cmake"


def compile_flags(
    output_dir: Path,
    autotests: bool,
    perf: bool,
    verbose: bool,
    show_ir: bool,
    format_output: bool,
) -> Namespace:
    return Namespace(
        output_dir=output_dir,
        verbose=verbose,
        show_ir=show_ir,
        analysis=perf,
        format=format_output,
        automatic_tests=autotests,
        generate_perf=perf,
    )


def generate(
    config: ExperimentConfig,
    build_root: Path,
    perf: bool = True,
    verbose: bool = False,
    show_ir: bool = False,
    format_output: bool = False,
) -> tuple[Path, AnalysisByModule]:
    out_dir = generated_dir(config, build_root)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    flags = compile_flags(out_dir, True, perf, verbose, show_ir, format_output)
    analyses: AnalysisByModule = {}
    for module in config.modules:
        module_name = module_name_from_path(module)
        analysis = compile_file(
            str(module),
            module_name,
            flags,
            config.settings,
        )
        if analysis is not None:
            analyses[module_name] = analysis
    return out_dir, analyses


def configure(config: ExperimentConfig, build_root: Path) -> Path:
    out_dir = generated_dir(config, build_root)
    build_dir = cmake_build_dir(config, build_root)
    build_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "cmake",
            "-S",
            "src/cpp",
            "-B",
            str(build_dir),
            "-G",
            "Ninja",
            "-DCMAKE_BUILD_TYPE=Release",
            "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
            f"-DGENERATED_DIR={out_dir.resolve()}",
        ],
        check=True,
    )
    return build_dir


def build(
    config: ExperimentConfig,
    build_root: Path,
    verbose: bool = False,
    show_ir: bool = False,
    format_output: bool = False,
) -> tuple[Path, AnalysisByModule]:
    _, analyses = generate(config, build_root, True, verbose, show_ir, format_output)
    build_dir = configure(config, build_root)
    subprocess.run(["cmake", "--build", str(build_dir)], check=True)
    return build_dir, analyses


def run_correctness(build_dir: Path) -> None:
    subprocess.run([str(build_dir / "correctness")], check=True)


def run_bench(
    build_dir: Path,
    start: int,
    stop: int,
    step: int,
    module: str | None,
    logical_bytes: int | None = None,
) -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    perf_bins = sorted(build_dir.glob("*_perf"))
    if module:
        perf_bins = [p for p in perf_bins if p.name == f"{module}_perf"]
    if not perf_bins:
        raise RuntimeError("No perf binaries were generated")

    for binary in perf_bins:
        command = [str(binary), str(start), str(stop), str(step)]
        if logical_bytes is not None:
            command.append(str(logical_bytes))
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
        for line in result.stdout.splitlines():
            if not line.startswith("{"):
                continue
            samples.append(json.loads(line))
    return samples


def graph_samples(
    samples: list[dict[str, object]],
    analyses: AnalysisByModule,
    config: ExperimentConfig,
    output_dir: Path,
    show: bool,
) -> list[Path]:
    os.environ.setdefault(
        "MPLCONFIGDIR",
        str(Path(tempfile.gettempdir()) / "polyuhf-matplotlib"),
    )
    os.environ.setdefault("MPLBACKEND", "Agg")
    from analysis.graphs import cycles_per_byte_plot, graphs

    grouped: dict[str, list[dict[str, object]]] = {}
    for sample in samples:
        module = str(sample["module"])
        grouped.setdefault(module, []).append(sample)

    written: list[Path] = []
    for module, module_samples in grouped.items():
        module_samples.sort(key=lambda sample: int(sample["B"]))
        data_b = [float(sample["B"]) for sample in module_samples]
        data_cycles = [float(sample["cycles"]) for sample in module_samples]
        data_traffic = [float(sample["bytes"]) for sample in module_samples]
        cycles_path = output_dir / f"{module}_cycles_per_byte.png"

        if module in analyses:
            ops_expr, traffic_expr, b_symbol = analyses[module]
            data_ops = [
                float(ops_expr.evalf(subs={b_symbol: sample["B"]}))
                for sample in module_samples
            ]
            data_traffic = [
                float(traffic_expr.evalf(subs={b_symbol: sample["B"]}))
                for sample in module_samples
            ]
            graphs(
                module,
                data_b,
                data_ops,
                data_traffic,
                data_cycles,
                config.settings,
                output_dir,
                show,
            )
            written.extend(
                [
                    cycles_path,
                    output_dir / f"{module}_roofline.png",
                ]
            )
        else:
            cycles_per_byte_plot(
                module,
                data_b,
                [],
                data_traffic,
                data_cycles,
                config.settings,
                cycles_path,
                show,
            )
            written.append(cycles_path)
    return written


def graph_field_sweep_samples(
    samples: list[dict[str, object]],
    output_dir: Path,
    show: bool,
) -> list[Path]:
    os.environ.setdefault(
        "MPLCONFIGDIR",
        str(Path(tempfile.gettempdir()) / "polyuhf-matplotlib"),
    )
    os.environ.setdefault("MPLBACKEND", "Agg")
    from analysis.graphs import field_sweep_cycles_per_byte_plot

    grouped: dict[str, list[dict[str, object]]] = {}
    for sample in samples:
        module = str(sample["module"])
        grouped.setdefault(module, []).append(sample)

    written: list[Path] = []
    for module, module_samples in grouped.items():
        path = output_dir / f"{module}_field_sweep_cycles_per_byte.png"
        field_sweep_cycles_per_byte_plot(module, module_samples, path, show)
        written.append(path)
    return written


def bench_range(
    args: argparse.Namespace, config: ExperimentConfig
) -> tuple[int, int, int]:
    return (
        args.start if args.start is not None else config.settings.bench.start,
        args.stop if args.stop is not None else config.settings.bench.stop,
        args.step if args.step is not None else config.settings.bench.step,
    )


def require_config(args: argparse.Namespace) -> ExperimentConfig:
    if not args.config:
        raise SystemExit("--config is required for this command")
    return load_experiment_config(args.config)


def build_from_args(
    config: ExperimentConfig, build_root: Path, args: argparse.Namespace
) -> tuple[Path, AnalysisByModule]:
    return build(config, build_root, args.verbose, args.show_ir, args.format)


def run_field_sweep(
    config_paths: list[str],
    build_root: Path,
    logical_bytes: int,
    module: str | None,
    verbose: bool,
    show_ir: bool,
    format_output: bool,
) -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    for config_path in config_paths:
        config = load_experiment_config(config_path)
        build_dir, _ = build(config, build_root, verbose, show_ir, format_output)
        chunk_size = config.settings.field.chunk_size()
        blocks = (logical_bytes + chunk_size - 1) // chunk_size
        padded_bytes = blocks * chunk_size
        for sample in run_bench(build_dir, blocks, blocks, 1, module, logical_bytes):
            sample.update(
                {
                    "config": str(config_path),
                    "field_pi": config.settings.field.pi,
                    "field_theta": config.settings.field.theta,
                    "chunk_size": chunk_size,
                    "B": blocks,
                    "bytes": logical_bytes,
                    "padded_bytes": padded_bytes,
                }
            )
            samples.append(sample)
    return samples


def main(argv: list[str] | None = None) -> int:
    cli = argparse.ArgumentParser(description="PolyUHF unified build/test/bench runner")
    cli.add_argument("--config", "-c", help="TOML experiment config")
    cli.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose compiler output",
    )
    cli.add_argument("--show-ir", action="store_true", help="Print generated IR")
    cli.add_argument("--format", action="store_true", help="Format generated C/C++")
    cli.add_argument(
        "--build-root",
        default="build",
        help="Root for config-specific generated files and CMake builds",
    )
    sub = cli.add_subparsers(dest="command", required=True)
    sub.add_parser("generate")
    sub.add_parser("build")
    sub.add_parser("test")
    bench_parser = sub.add_parser("bench")
    bench_parser.add_argument("--start", type=int)
    bench_parser.add_argument("--stop", type=int)
    bench_parser.add_argument("--step", type=int)
    bench_parser.add_argument("--module", help="Only run one module's perf binary")
    all_parser = sub.add_parser("run-all")
    all_parser.add_argument("--start", type=int)
    all_parser.add_argument("--stop", type=int)
    all_parser.add_argument("--step", type=int)
    all_parser.add_argument("--module", help="Only run one module's perf binary")
    graph_parser = sub.add_parser("graph")
    graph_parser.add_argument("--start", type=int)
    graph_parser.add_argument("--stop", type=int)
    graph_parser.add_argument("--step", type=int)
    graph_parser.add_argument("--module", help="Only graph one module")
    graph_parser.add_argument(
        "--output-dir",
        default="graphs",
        help="Directory for generated graph PNG files",
    )
    graph_parser.add_argument(
        "--show",
        action="store_true",
        help="Show matplotlib windows",
    )
    field_sweep_parser = sub.add_parser(
        "field-sweep",
        help="Benchmark multiple field configs at a fixed logical byte length",
    )
    field_sweep_parser.add_argument(
        "configs",
        nargs="+",
        help="Self-contained TOML configs to build and benchmark",
    )
    field_sweep_parser.add_argument(
        "--bytes",
        type=int,
        default=25_000,
        help="Logical input byte length used for cycles/byte",
    )
    field_sweep_parser.add_argument(
        "--module",
        help="Only run one module's perf binary",
    )
    field_sweep_parser.add_argument(
        "--graph",
        action="store_true",
        help="Write field-sweep cycles/byte graphs",
    )
    field_sweep_parser.add_argument(
        "--output-dir",
        default="graphs",
        help="Directory for generated field-sweep graph PNG files",
    )
    field_sweep_parser.add_argument(
        "--show",
        action="store_true",
        help="Show matplotlib windows",
    )

    args = cli.parse_args(argv)
    build_root = Path(args.build_root)

    if args.command == "generate":
        config = require_config(args)
        out_dir, _ = generate(
            config, build_root, True, args.verbose, args.show_ir, args.format
        )
        print(out_dir)
    elif args.command == "build":
        config = require_config(args)
        build_dir, _ = build_from_args(config, build_root, args)
        print(build_dir)
    elif args.command == "test":
        config = require_config(args)
        build_dir, _ = build_from_args(config, build_root, args)
        run_correctness(build_dir)
    elif args.command == "bench":
        config = require_config(args)
        build_dir, _ = build_from_args(config, build_root, args)
        start, stop, step = bench_range(args, config)
        for sample in run_bench(build_dir, start, stop, step, args.module):
            print(json.dumps(sample, sort_keys=True))
    elif args.command == "run-all":
        config = require_config(args)
        build_dir, _ = build_from_args(config, build_root, args)
        run_correctness(build_dir)
        start, stop, step = bench_range(args, config)
        for sample in run_bench(build_dir, start, stop, step, args.module):
            print(json.dumps(sample, sort_keys=True))
    elif args.command == "graph":
        config = require_config(args)
        build_dir, analyses = build_from_args(config, build_root, args)
        start, stop, step = bench_range(args, config)
        samples = run_bench(build_dir, start, stop, step, args.module)
        for path in graph_samples(
            samples, analyses, config, Path(args.output_dir), args.show
        ):
            print(path)
    elif args.command == "field-sweep":
        samples = run_field_sweep(
            args.configs,
            build_root,
            args.bytes,
            args.module,
            args.verbose,
            args.show_ir,
            args.format,
        )
        for sample in samples:
            print(json.dumps(sample, sort_keys=True))
        if args.graph:
            for path in graph_field_sweep_samples(
                samples, Path(args.output_dir), args.show
            ):
                print(path)
    else:
        raise AssertionError(f"Unknown command {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
