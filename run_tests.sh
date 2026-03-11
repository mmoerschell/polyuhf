#!/bin/sh
set -ex

# src/main.py -f programs/poly1305.txt prime --crandall 13 5
src/main.py -f programs/exponentiation.txt prime --crandall 13 5
cmake -S src/cpp -B src/cpp/build/Release -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build src/cpp/build/Release
./src/cpp/build/Release/tests
