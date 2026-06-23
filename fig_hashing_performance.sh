#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <platform>" >&2
    exit 1
fi

PLATFORM="$1"

MODULES_SETTINGS=(
    "mmh 1 full"
    "nmh 1 full"
    "sqh 1 full"
)

FIELDS=(
    "116 3"
    "226 5"
)


STEP=112
START=140
STOP=16000
OUTPUT_FILE=data/hashing_performance/"$PLATFORM"_data.csv
mkdir -p data/hashing_performance


printf "module,pi,theta,karatsuba,length,cycles\n" > $OUTPUT_FILE


date
for mod_settings in "${MODULES_SETTINGS[@]}"; do
    read -r module vectorize delay <<< "$mod_settings"


    for field in "${FIELDS[@]}"; do
        read -r pi theta <<< "$field"

        for karatsuba in $(seq 0 1); do
            # Build
            ./runner.sh 1 $karatsuba $delay 0 1 1 1 $module $pi $theta $PLATFORM 1 

            # Run
            n_bytes=$START
            while IFS= read -r cycles; do
                # Write data
                echo "$module,$pi,$theta,$karatsuba,$n_bytes,$cycles" >> $OUTPUT_FILE
                # Report progress
                percent=$((100 * n_bytes / $STOP))
                printf "\r[%3d%% done]" "$percent"
                # Loop step
                n_bytes=$((n_bytes + STEP))
            done < <(./src/cpp/build/performance_"$module" $START $STOP $STEP median)
            echo ""

            # Cool down
            echo "Cooling down"

            sleep 120

        done
    done
done
date

echo "Wrote output to '$OUTPUT_FILE'"
