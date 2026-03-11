#!/bin/sh
set -ex

# Build all DSL source files with appropriate fields
src/main.py -f programs/addition.txt prime --crandall 130 5
# src/main.py -f programs/poly1305.txt prime --crandall 130 5
# src/main.py -f programs/exponentiation.txt prime --crandall 130 5

# Build test harness
# Uncomment on first run
# mkdir -p src/cpp/build/Release
# cmake -S src/cpp -B src/cpp/build/Release -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build src/cpp/build/Release

# Run tests
./src/cpp/build/Release/tests $@
