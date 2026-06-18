#!/usr/bin/env bash
set -euo pipefail

# TODO adjust input length to be a multiple of the block size in every field

MODULE="mmh"
DELAY="full"
PLATFORM="neon"
UNROLLING_FACTOR="1"
CPP_BUILD_DIR="src/cpp/build"
GENERATED_DIR="$CPP_BUILD_DIR/generated"
MESSAGE_LENGTH=16000
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

modes_vec_kara=(
  "scalar_schoolbook 0 0"
  "scalar_karatsuba 0 1"
  "vector_schoolbook 1 0"
  "vector_karatsuba 1 1"
)

printf "pi,theta,mode,cycles\n" > $OUTPUT_FILE

for field in "${fields[@]}"; do
  read -r pi theta <<< "$field"
  echo "FIELD $pi $theta"
  for m_f in "${modes_vec_kara[@]}"; do
    read -r mode vectorize karatsuba <<< "$m_f"
   
    # Build
    ./runner.sh $vectorize $karatsuba $DELAY 0 1 1 1 $MODULE $pi $theta $PLATFORM $UNROLLING_FACTOR

    # Run/perf
    cycles="$(src/cpp/build/performance_$MODULE $MESSAGE_LENGTH $MESSAGE_LENGTH 1 median)"
    cycles=$((cycles)) # trim whitespace

    printf "%d,%d,%s,%d\n" $pi $theta $mode $cycles >> $OUTPUT_FILE
  done
done

echo "Wrote output to '$OUTPUT_FILE'"
