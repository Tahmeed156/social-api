#!/bin/bash
set -xe

set -o nounset

BUCKET_NAME=$1

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

echo "Generating Build Artifact(s):"
# Not a practical build artifact. Practical build artifacts might be a .deb, .rpm, .jar or a container image. You get the idea !!
HASH=`git ls-tree HEAD | git hash-object --stdin | cut -c 1-7`
zip -r build-$HASH . -x ./venv/\* ./.git/\* 
aws s3 cp ./build-$HASH.zip s3://$BUCKET_NAME/build/