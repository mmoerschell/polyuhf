#!/usr/bin/env bash

set -euo pipefail

MODULES=(
    "mmh"
    "sqh"
    "nmh"
)

FIELDS=(
    "116 3"
    "226 5"
)

OUTPUT_FILE=data/predicted_cycles.csv
mkdir -p data/

printf "module,pi,theta,predicted_cycles_per_byte\n" > $OUTPUT_FILE

for field in "${FIELDS[@]}"; do
    read -r pi theta <<< "$field"
    for module in "${MODULES[@]}"; do
        predicted_cpb=$(./compiler -v -m --delay-limb-realignment full modules/"$module".txt $pi $theta neon 1)
        predicted_cpb=$(printf '%s\n' "$predicted_cpb" | grep 'Estimated cyles')
        predicted_cpb=$(printf '%s\n' "$predicted_cpb" | grep -Eo '[0-9]+\.[0-9]+')
        printf "%s,%s,%s,%s\n" $module $pi $theta $predicted_cpb >> $OUTPUT_FILE
    done
done

echo "Done."
