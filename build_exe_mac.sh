#!/bin/bash

# Ensure PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller is not installed. Install it with 'pip install pyinstaller'."
    exit 1
fi

# Build the executable for macOS
pyinstaller --onefile --name py_executable src/py_executable/main.py

# Clean up unnecessary build files
rm -rf build
rm py_executable.spec

echo "macOS executable built successfully. Find it in the 'dist/' directory."