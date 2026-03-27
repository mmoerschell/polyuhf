#!/bin/sh

# Clear pycache

# Source - https://stackoverflow.com/a/30659970
# Posted by V. Gamula, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-03, License - CC BY-SA 4.0

find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

# rm generated files
rm src/cpp/generated/*
