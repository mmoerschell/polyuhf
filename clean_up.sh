#!/bin/sh
set -eu

find . -name __pycache__ -type d -prune -exec rm -rf {} +
find . \( -name '*.pyc' -o -name '*.pyo' \) -type f -delete
rm -rf .pytest_cache .ruff_cache build
