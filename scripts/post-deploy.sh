#!/bin/bash
set -xe

set -o nounset

echo "Setting up venv:"
python3 -m venv venv
source venv/bin/activate

echo `pwd`

echo "Installing Requirements:"
pip install -r requirements.txt

echo "Checking Compile Errors:"
python3 integration_tests/integration_tests.py --host=34.226.214.93 --protocol=http