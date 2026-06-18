#!/usr/bin/env bash
set -euo pipefail

MODULE="mmh"
PLATFORM="neon"
UNROLLING_FACTOR="2"
CPP_BUILD_DIR="src/cpp/build"
GENERATED_DIR="$CPP_BUILD_DIR/generated"
MESSAGE_LENGTH=24000
OUTPUT_FILE=data/fieldsweep/"$MODULE"_"$PLATFORM"_data.csv

mkdir -p fieldsweep

fields=(
  "100 15"
  "104 17"
  "105 13"
  "107 1"
  "114 11"
  "116 3"
  "118 5"
  "122 3"
  "125 9"
  "127 1"
  "130 5"
  "137 13"
  "141 9"
  "150 3"
  "152 17"
  "157 19"
  "158 15"
  "166 5"
  "171 19"
  "174 3"
  "190 11"
  "191 19"
  "196 15"
  "198 17"
  "206 5"
  "213 3"
  "221 3"
  "226 5"
  "233 3"
  "235 15"
  "243 9"
  "251 9"
  "255 19"
  "266 3"
  "285 9"
  "291 19"
  "321 9"
  "322 11"
  "336 3"
  "338 15"
  "379 19"
)

modes_flags=(
  "scalar_schoolbook"
  "scalar_karatsuba -k"
  "vector_schoolbook -v"
  "vector_karatsuba -v -k"
)

printf "pi,theta,mode,cycles\n" > $OUTPUT_FILE

for field in "${fields[@]}"; do
  read -r pi theta <<< "$field"
  echo "FIELD $pi $theta"
  for m_f in "${modes_flags[@]}"; do
    mode=""
    flags=""
    read -r mode flags <<< "$m_f"
    compiler_flags=("${(@z)flags}")

    cmake -E rm -rf "$CPP_BUILD_DIR"
    mkdir -p "$GENERATED_DIR"
    
    # DSL compiler
    venv/bin/python src/compiler.py "${compiler_flags[@]}" -qa modules/$MODULE.txt $pi $theta $PLATFORM $UNROLLING_FACTOR

    # CMake generate
    cmake --log-level=ERROR \
      -S src/cpp/performance \
      -B "$CPP_BUILD_DIR" \
      -G Ninja \
      -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
      -DGENERATED_DIR="$GENERATED_DIR" \
      -DPERF_MODULE="$MODULE" \
      -DCMAKE_BUILD_TYPE=Release \
      -Wno-dev >/dev/null

    # CMake build
    cmake --build "$CPP_BUILD_DIR"

    # Run/perf
    cycles="$("$CPP_BUILD_DIR/${MODULE}_perf" $MESSAGE_LENGTH $MESSAGE_LENGTH 1)"
    cycles=$((cycles))

    printf "%d,%d,%s,%d\n" $pi $theta $mode $cycles >> $OUTPUT_FILE
  done
done

echo "Wrote output to $OUTPUT_FILE"
