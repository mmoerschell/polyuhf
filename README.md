# Domain-Specific Language for Polynomial Universal Hash Functions

This repository contains an experimental DSL compiler for polynomial universal hash
functions over Crandall prime fields of the form `GF(2^pi - theta)`. A DSL module
is parsed, type-checked, lowered to an intermediate representation, and emitted
as scalar C or SIMD C for NEON/AVX2, together with optional correctness tests and
performance harnesses.

## Dependencies

The DSL compiler depends on Python 3 and the packages in `requirements.txt`. It is best used in a virtual environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The C/C++ side uses CMake, Ninja, Boost.Test/Boost.JSON, and OpenSSL. The figure
scripts use pandas, NumPy, and matplotlib. The repository also assumes common
developer tools. Below is an example of how to install those on Ubuntu.

```sh
sudo apt install -y gcc g++ libboost-all-dev libssl-dev cmake ninja-build
```

For optional formatting of generated code, you may  also want to install `clang-tidy` and `clang-format`.

```sh
sudo apt install -y clang-tidy clang-format
```

## Layout

Some important paths in this repository:

```text
modules/                 DSL input modules
src/compiler.py          DSL compiler entry point
compiler                 symlink to src/compiler.py
src/parsing/             ANTLR parser and AST builder
src/ir/                  IR nodes, IR builder, pretty-printer
src/codegen/             C code generator and operation templates
src/automatic_tests/     Boost correctness-test emitter
src/cpp/                 CMake project, generated C, manual C++ tests
src/cpp/generated/       generated headers, sources, tests, perf harnesses
src/cpp/build/           CMake build directory
data/                    measured CSV data
figures/                 plotting scripts and generated PNGs
report/                  thesis report sources
```

## Compiler

The compiler takes one DSL module, a prime field, a target platform, and a small
set of code-generation flags, for example:

```sh
./compiler [flags] modules/mmh.txt 116 3 neon 1
```

This compiles `modules/mmh.txt` for `GF(2^116 - 3)`, targeting NEON, with
unrolling factor `1`.

Useful flags:

```text
--vectorize, -v                 emit SIMD field operations
--karatsuba, -k                 use one-level Karatsuba multiplication
--delay-limb-realignment MODE   MODE is partial or full
--automatic_tests, -t           generate Boost correctness tests
--analysis, -a                  generate performance harness when possible
--show-ir, -i                   print the compiler IR
--format, -f                    run optional C formatting
--quiet, -q                     only report errors
--test-size N                   number of generated Boost test cases
```

The compiler writes generated code to `src/cpp/generated/`. A typical generated
module consists of:

```text
<module>.h
<module>.c
datastructures.h
datastructures.c
<module>_autotests.cpp      if --automatic_tests is enabled
<module>_perf.c             if --analysis can emit a perf harness
```

Hash functions are emitted with the stable C API:

```c
void hashname(uint8_t *output, uint8_t *key, uint8_t *message, size_t len);
```

Here `len` is the byte length of `key` and `message` at the C boundary. The IR
uses field-element block counts internally. The generated hash functions may read a few more bytes from the source buffers than the specificed length, if the field-element chunk size $\lfloor \pi / 8 \rfloor$ does not divide `len` in the chosen field configuration!

## CMake

`src/cpp/CMakeLists.txt` builds exactly one generated module at a time. It uses
the generated files in `src/cpp/generated/` and emits targets into
`src/cpp/build/`.

Manual invocation:

```sh
cmake -S src/cpp -B src/cpp/build -G Ninja \
  -DMODULE_NAME=mmh \
  -DCORRECTNESS=ON \
  -DPERFORMANCE=ON \
  -DPLATFORM=neon

cmake --build src/cpp/build
```

The target names are derived from the module:

```text
correctness_<module>
performance_<module>
```

`CORRECTNESS=ON` builds the Boost correctness executable. `PERFORMANCE=ON` builds
the generated measurement executable if the compiler emitted `<module>_perf.c`.
The CMake project exports `compile_commands.json`; `src/cpp/compile_commands.json`
points at the current build directory.

## Runner

`runner.sh` is the usual one-module workflow. It erases `src/cpp/build/` and
`src/cpp/generated/`, runs the DSL compiler, configures CMake, builds the selected
targets, and optionally runs them.

```sh
./runner.sh \
  <vectorize:0|1> \
  <karatsuba:0|1> \
  <delay:partial|full> \
  <correctness:0|1> \
  <performance:0|1> \
  <quiet:0|1> \
  <build-only:0|1> \
  <module> \
  <pi> \
  <theta> \
  <platform> \
  <unrolling factor>
```

Example:

```sh
./runner.sh 1 1 full 1 1 1 0 mmh 116 3 neon 2
```

This builds vectorized Karatsuba MMH in `GF(2^116 - 3)` for NEON, with fully
delayed limb realignment and unrolling factor `2`, then runs both correctness and
performance targets.

Set `build-only` to `1` to compile without executing binaries:

```sh
./runner.sh 1 0 partial 1 0 1 1 poly1305 130 5 neon 1
```

The performance binary accepts a byte range:

```sh
./src/cpp/build/performance_mmh <start-bytes> <stop-bytes> <step-bytes> [median|min]
```

For example:

```sh
./src/cpp/build/performance_mmh 140 16000 140 median
```

## Correctness Sweep

`correctness_tests.sh` runs a small correctness sweep across modules and fields:

```sh
./correctness_tests.sh neon
./correctness_tests.sh avx2
```

The script calls `runner.sh` repeatedly. Poly1305 is only tested in
`GF(2^130 - 5)`, where its usual byte/block interpretation makes sense.

## Figures and Measurements

The measurement scripts generate CSV files under `data/`. The plotting scripts
read those CSV files and write figures under `figures/` or PGF files under
`report/import_figures/`.

## Notes

Generated files are disposable. Re-running `runner.sh` removes the current
`src/cpp/generated/` and `src/cpp/build/` directories, so do not keep manual edits
there.

The parser sources in `src/parsing/antlr/` are generated from the grammar. If the
grammar changes, regenerate the parser using the provided script before using the compiler again. This additionally requires a Java installation.
