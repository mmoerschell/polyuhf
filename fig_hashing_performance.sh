#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 7 ]; then
    echo "Usage: $0 <platform> <module> <delay:partial|full> <pi> <theta> <karatsuba> <unroll>" >&2
    exit 1
fi

PLATFORM="$1"
MODULE="$2"
DELAY="$3"
PI="$4"
THETA="$5"
KARATSUBA="$6"
UNROLLING_FACTOR="$7"

BLOCK_RESOLUTION=16

STEP=$((PI / 8 * BLOCK_RESOLUTION)) # 2 lanes
START=$STEP
STOP=$((16000 + STEP))
OUTPUT_FILE=data/hashing_performance/"$PLATFORM"_"$MODULE"_"$PI"_"$THETA"_"kara$KARATSUBA"_"ur$UNROLLING_FACTOR"_data.csv

mkdir -p data

printf "bytes,cycles\n" > $OUTPUT_FILE

# Build
./runner.sh 1 $KARATSUBA $DELAY 0 1 1 1 $MODULE $PI $THETA $PLATFORM $UNROLLING_FACTOR 

# Run
date
n_bytes=$START
while IFS= read -r line; do
    # Write data
    echo "$n_bytes,$line" >> $OUTPUT_FILE
    # Report progress
    percent=$((100 * n_bytes / $STOP))
    printf "\r[%3d%% done]" "$percent"
    # Loop step
    n_bytes=$((n_bytes + STEP))
done < <(./src/cpp/build/performance_"$MODULE" $START $STOP $STEP median)
echo ""
date

echo "Wrote output to '$OUTPUT_FILE'"
