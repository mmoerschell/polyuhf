#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <platform:neon|avx2>" >&2
    exit 1
fi

PLATFORM="$1"

MODULES_DELAY_UNROLL=(
    "mmh full 8"
    "sqh full 8"
    "nmh full 8"
    "hkm partial 2"
    "hkm_iter partial 2"
    "poly1305 partial 1"
)


FIELDS=(
    "116 3"
    "130 5"
    "226 5"
)

for mdu in "${MODULES_DELAY_UNROLL[@]}"; do
    read -r module delay unroll <<< "$mdu"

    for field in "${FIELDS[@]}"; do
        read -r pi theta <<< "$field"

        # Poly1305 guard
        if [[ "$module" == "poly1305" && ( "$pi" != "130" || "$theta" != "5" ) ]]; then
            continue
        fi

        for karatsuba in $(seq 0 1); do
            echo "Testing module '$module' in GF(2^$pi-$theta) with $delay delay and unrolling $unroll, karatsuba=$karatsuba"
            ./runner.sh 1 "$karatsuba" "$delay" 1 0 1 0 "$module" "$pi" "$theta" "$PLATFORM" "$unroll"
        done

    done
done

echo "ALL TESTS PASSED"
