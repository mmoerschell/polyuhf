#!/usr/bin/env bash
set -euo pipefail

MESSAGE_LENGTH=16000

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <platform>" >&2
    exit 1
fi

PLATFORM="$1"

OUTPUT_FILE=data/fieldsweep/"$PLATFORM"_data.csv
mkdir -p data/fieldsweep


FIELDS=(
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

MODULES=(
  "mmh"
  "nmh"
  "sqh"
)

printf "module,pi,theta,vectorize,karatsuba,cycles\n" > $OUTPUT_FILE

for field in "${FIELDS[@]}"; do
  read -r pi theta <<< "$field"
  echo "FIELD $pi $theta"
  for module in "${MODULES[@]}"; do
    for vectorize in $(seq 0 1); do
      for karatsuba in $(seq 0 1); do
        if [[ "$module" == "sqh" && "$karatsuba" == "1" ]]; then
          # SQH uses squaring, Karatsuba-multiplication has no effect there.
          echo "Skipping Karatsuba for sqh"
          continue
        fi

        # Build
        ./runner.sh $vectorize $karatsuba "full" 0 1 1 1 $module $pi $theta $PLATFORM 1

        # Run/perf
        cycles="$(src/cpp/build/performance_$module $MESSAGE_LENGTH $MESSAGE_LENGTH 1 median)"
        cycles=$((cycles)) # trim whitespace

        printf "%s,%d,%d,%d,%d,%d\n" $module $pi $theta $vectorize $karatsuba $cycles >> $OUTPUT_FILE
      done
    done
  done
done

echo "Wrote output to '$OUTPUT_FILE'"
