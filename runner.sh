#!/usr/bin/env zsh

set -euo pipefail

BUILD_DIR=src/cpp/build
MODULE_NAME=nmh

rm -rf $BUILD_DIR
./compiler -vat modules/$MODULE_NAME.txt 130 5 neon 1
cmake -S src/cpp -B $BUILD_DIR -G Ninja -DMODULE_NAME="$MODULE_NAME" -DCORRECTNESS=ON -DPERFORMANCE=ON
cmake --build $BUILD_DIR
ls $BUILD_DIR

$BUILD_DIR/correctness_$MODULE_NAME
$BUILD_DIR/performance_$MODULE_NAME 100 100 1
