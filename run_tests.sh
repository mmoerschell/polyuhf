#!/bin/sh
set -eux

# Uncomment whatever applies

# Build all DSL source files
# mkdir -p src/cpp/generated
find programs -iname '*.txt' -print0 |
  xargs -0 -n1 sh -c './src/main.py -f "$1" || exit 255' sh

# Build & run test harness
# mkdir -p src/cpp/build
# cmake -S src/cpp -B src/cpp/build -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build src/cpp/build
./src/cpp/build/tests $@
