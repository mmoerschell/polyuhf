#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <platform>" >&2
    exit 1
fi

PLATFORM="$1"

FIELDS=(
  "116 3"
  "130 5"
  "226 5"
)

MODULES_SETTINGS=(
    "mmh 1 full 1"
    "nmh 1 full 1"
    "sqh 1 full 1"
    "hkm_iter 0 partial 1"
    "poly1305 1 partial 1"
)

mkdir -p data/16kb
OUTPUT_FILE=data/16kb/"$PLATFORM"_data.csv

echo "platform,module,pi,theta,unroll,karatsuba,cycles" > $OUTPUT_FILE

for mod_settings in "${MODULES_SETTINGS[@]}"; do
    read -r module vectorize delay unroll <<< "$mod_settings"
    for field in "${FIELDS[@]}"; do
        read -r pi theta <<< "$field"
        for karatsuba in $(seq 0 1); do
            if [[ "$module" == "poly1305" && "$pi" -ne 130 ]]; then
                echo "Skipping poly1305 in $pi"
                continue
            fi
            # Build
            ./runner.sh $vectorize $karatsuba $delay 0 1 1 1 $module $pi $theta $PLATFORM $unroll
            # Run
            cycles=$(./src/cpp/build/performance_"$module" 16000 16000 1 median)
            cycles=$((cycles))
            # Write
            printf "%s,%s,%s,%s,%s,%s,%d\n" $PLATFORM $module $pi $theta $unroll $karatsuba $cycles >> $OUTPUT_FILE
        done
    done
done

echo "Wrote output to '$OUTPUT_FILE'"
