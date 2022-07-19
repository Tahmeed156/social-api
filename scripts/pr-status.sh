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
python manage.py check

echo "Running Tests:"
pytest -v -s

echo "Checking Deployment Checklist:"
python manage.py check --deploy