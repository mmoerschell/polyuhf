#!/usr/bin/env zsh
set -euo pipefail

MODULE="mmh"
PLATFORM="neon"
UNROLLING_FACTOR="2"
BUILD_ROOT="build/fieldsweep"
MESSAGE_LENGTH=24000
OUTPUT_FILE=fieldsweep/"$MODULE"_"$PLATFORM"_data.csv

mkdir -p $BUILD_ROOT

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
  "vector_karatsuba -vk"
)

printf "pi,theta,mode,cycles\n" > $OUTPUT_FILE

for field in "${fields[@]}"; do
  read -r pi theta <<< "$field"
  echo "FIELD $pi $theta"
  for m_f in "${modes_flags[@]}"; do
    mode=""
    flags=""
    read -r mode flags <<< "$m_f"
    
    # DSL compiler
    ./compiler $flags -qa -o $BUILD_ROOT/generated modules/$MODULE.txt $pi $theta $PLATFORM $UNROLLING_FACTOR

    # CMake generate
    cmake --log-level=ERROR -S src/cpp/performance -B $BUILD_ROOT/cmake -G Ninja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DGENERATED_DIR=$BUILD_ROOT/generated -DPERF_MODULE=$MODULE -DCMAKE_BUILD_TYPE=Release -Wno-dev >/dev/null

    # CMake build
    cmake --build $BUILD_ROOT/cmake

    # Run/perf
    cycles="$($BUILD_ROOT/cmake/($MODULE)_perf $MESSAGE_LENGTH $MESSAGE_LENGTH 1)"
    cycles=$((cycles))

    printf "%d,%d,%s,%d\n" $pi $theta $mode $cycles >> $OUTPUT_FILE
  done
done

echo "Wrote output to $OUTPUT_FILE"
