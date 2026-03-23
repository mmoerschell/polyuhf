#!/bin/sh
set -ex

# Build all DSL source files with appropriate fields
mkdir -p src/cpp/generated
src/main.py -f programs/addition.txt prime --crandall 130 5
src/main.py -f programs/multiplication.txt prime --crandall 130 5
src/main.py -f programs/poly1305.txt prime --crandall 130 5
src/main.py -f programs/exponentiation.txt prime --crandall 130 5
src/main.py -f programs/mmh.txt prime --crandall 130 5
src/main.py -f programs/sqh.txt prime --crandall 130 5
src/main.py -f programs/nmh.txt prime --crandall 130 5

# Build & run test harness
# Uncomment whatever applies

# mkdir -p src/cpp/build/Debug
# mkdir -p src/cpp/build/Release

# cmake -S src/cpp -B src/cpp/build/Debug -G Ninja -DCMAKE_BUILD_TYPE=Debug
cmake -S src/cpp -B src/cpp/build/Release -G Ninja -DCMAKE_BUILD_TYPE=Release

# cmake --build src/cpp/build/Debug
cmake --build src/cpp/build/Release

# ./src/cpp/build/Debug/tests $@
./src/cpp/build/Release/tests $@
