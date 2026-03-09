#!/bin/sh
set -ex

src/main.py -f programs/poly1305.txt prime --crandall 13 5
cd src/cpp
make clean run-test
cd ../..
