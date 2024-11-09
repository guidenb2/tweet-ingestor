#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
VENV_DIR="$SCRIPT_DIR/../tweet-ingestor-venv"

echo "Checking if venv activated"
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Deactivating venv $VIRTUAL_ENV..."
    deactivate
else
    echo "No venv activated"
fi

echo "Checking if venv directory exists..."
if [[ -d "$VENV_DIR" ]]; then
    echo "Deleting venv directory $VENV_DIR..."
    rm -rf "$VENV_DIR"
else
    echo "$VENV_DIR does not exist"
fi

echo "Creating virtual environment 'tweet-ingestor-env'"
cd "$SCRIPT_DIR/.." || exit
python3 -m venv tweet-ingestor-venv
VENV_ACTIVATE="${VENV_DIR}/bin/activate"
if [[ -f "$VENV_ACTIVATE" ]]; then
    echo "Activating virtual environment..."
    # shellcheck disable=SC1090
    source "$VENV_ACTIVATE"
else
    echo "Error: $VENV_ACTIVATE not found."
fi
pip3 install -r requirements.txt

echo "Virtual Environment configured. Exiting..."
