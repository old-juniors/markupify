#!/bin/bash

# Check if the 'pre-commit-requirements.txt' file exists
if [ -f pre-commit-requirements.txt ]; then
    # Install packages from 'pre-commit-requirements.txt' using pip
    pip install -r pre-commit-requirements.txt
    echo "Packages installed successfully."

    # Install the 'pre-commit' command
    pre-commit install

    # Run against all the files
    pre-commit run --all-files
else
    echo "Error: 'pre-commit-requirements.txt' file not found."
    exit 1
fi
