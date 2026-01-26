#!/bin/sh

find programs -iname "*.txt" -exec echo "> {}" \; -exec ./src/main.py {} \;
