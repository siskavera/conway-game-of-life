#!/bin/bash

function cleanup {
  echo "Deactivating virtual environment"
  deactivate
}

trap cleanup EXIT

echo "Changing to $(dirname $0)"
cd $(dirname $0)

echo "Creating virtual environment"
virtualenv -p python3 --clear venv
venv/bin/pip install -r requirements.txt
