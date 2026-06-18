#!/usr/bin/env zsh

set -euo pipefail

BUILD_DIR=src/cpp/build
GENERATED_DIR=src/cpp/generated

if [ "$#" -ne 12 ]; then
    echo "Usage: $0 <vectorize:0|1> <karatsuba:0|1> <delay:partial|full> <correctness:0|1> <performance:0|1> <quiet:0|1> <build-only:0|1> <module> <pi> <theta> <platform> <unrolling factor>" >&2
    exit 1
fi

# Gather parameters
VECTORIZE=$1
KARATSUBA=$2
DELAY=$3
CORRECTNESS=$4
PERFORMANCE=$5
QUIET=$6
BUILD_ONLY=$7
MODULE_NAME=$8
PI=$9
THETA=${10}
PLATFORM=${11}
UNROLL=${12}

# Check parameters
if [[ "$VECTORIZE" != "0" && "$VECTORIZE" != "1" ]]; then
    echo "vectorize must be 0 or 1" >&2
    exit 2
fi
if [[ "$KARATSUBA" != "0" && "$KARATSUBA" != "1" ]]; then
    echo "karatsuba must be 0 or 1" >&2
    exit 2
fi
if [[ "$DELAY" != "partial" && "$DELAY" != "full" ]]; then
    echo "delay must be partial or full" >&2
    exit 2
fi
if [[ "$CORRECTNESS" != "0" && "$CORRECTNESS" != "1" ]]; then
    echo "correctness must be 0 or 1" >&2
    exit 2
fi
if [[ "$PERFORMANCE" != "0" && "$PERFORMANCE" != "1" ]]; then
    echo "performance must be 0 or 1" >&2
    exit 2
fi
if [[ "$QUIET" != "0" && "$QUIET" != "1" ]]; then
    echo "quiet must be 0 or 1" >&2
    exit 2
fi
if [[ "$BUILD_ONLY" != "0" && "$BUILD_ONLY" != "1" ]]; then
    echo "build-only must be 0 or 1" >&2
    exit 2
fi
if [[ "$CORRECTNESS" == "0" && "$PERFORMANCE" == "0" ]]; then
    echo "at least one of correctness or performance must be enabled" >&2
    exit 2
fi
if [[ ! -f "modules/$MODULE_NAME.txt" ]]; then
    echo "No module found at modules/$MODULE_NAME.txt" >&2
    exit 1
fi

compiler_args=()
if [[ "$VECTORIZE" == "1" ]]; then
    compiler_args+=(--vectorize)
fi
if [[ "$KARATSUBA" == "1" ]]; then
    compiler_args+=(--karatsuba)
fi
if [[ "$CORRECTNESS" == "1" ]]; then
    compiler_args+=(--automatic_tests)
fi
if [[ "$PERFORMANCE" == "1" ]]; then
    compiler_args+=(--analysis)
fi
if [[ "$QUIET" == "1" ]]; then
    compiler_args+=(--quiet)
fi
compiler_args+=(--delay-limb-realignment "$DELAY")

cmake_correctness=OFF
cmake_performance=OFF
if [[ "$CORRECTNESS" == "1" ]]; then
    cmake_correctness=ON
fi
if [[ "$PERFORMANCE" == "1" ]]; then
    cmake_performance=ON
fi

echo "Erasing $BUILD_DIR and $GENERATED_DIR"
rm -rf "$BUILD_DIR" "$GENERATED_DIR"

# DSL Compiler
python3 ./compiler "${compiler_args[@]}" "modules/$MODULE_NAME.txt" "$PI" "$THETA" "$PLATFORM" "$UNROLL"

# Generate
if [[ "$QUIET" == "1" ]]; then
    exec 3>/dev/null
else
    exec 3>&1
fi
cmake -S src/cpp -B "$BUILD_DIR" -G Ninja \
    -DMODULE_NAME="$MODULE_NAME" \
    -DCORRECTNESS="$cmake_correctness" \
    -DPERFORMANCE="$cmake_performance" \
    -DPLATFORM="$PLATFORM" >&3

# Build
if [[ "$CORRECTNESS" == "1" ]]; then
    cmake --build "$BUILD_DIR" --target "correctness_$MODULE_NAME"
fi
if [[ "$PERFORMANCE" == "1" ]]; then
    cmake --build "$BUILD_DIR" --target "performance_$MODULE_NAME"
fi

# Run/correctness
if [[ "$BUILD_ONLY" == "0" && "$CORRECTNESS" == "1" ]]; then
    "$BUILD_DIR/correctness_$MODULE_NAME"
fi

# Run/performance
if [[ "$BUILD_ONLY" == "0" && "$PERFORMANCE" == "1" ]]; then
    "$BUILD_DIR/performance_$MODULE_NAME" 100 100 1
fi
