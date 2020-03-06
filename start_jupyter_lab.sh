#!/bin/bash -e

function cleanup {
  echo "Deactivating virtual environment"
  deactivate
}

trap cleanup EXIT

echo "Changing to $(dirname $0)"
cd $(dirname $0)

echo "Activating virtual environment"
source venv/bin/activate
PYTHONPATH=$(pwd) jupyter lab

