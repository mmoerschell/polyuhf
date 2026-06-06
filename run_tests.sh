#!/bin/sh
set -eux

# Uncomment whatever applies

# Build all DSL source files
# mkdir -p src/cpp/generated
find programs -iname '*.txt' | parallel --group --halt now,fail=1 ./src/main.py -t {}

# Build & run test harness
mkdir -p src/cpp/build
cmake -S src/cpp -B src/cpp/build -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build src/cpp/build
./src/cpp/build/correctness $@
