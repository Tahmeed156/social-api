#!/bin/bash
set -xe

set -o nounset

BUCKET_NAME=$1
build_dir=build

latest_build=`aws s3 ls $BUCKET_NAME/$build_dir/ | sort | tail -n 1 | tr -s ' ' | cut -d ' ' -f 4`
app_dir=`echo $latest_build | cut -d '.' -f 1`

echo "Fetching latest build: $latest_build"

aws s3 cp s3://$BUCKET_NAME/$build_dir/$latest_build ./build.zip

rm -r $app_dir || true
mkdir $app_dir
unzip build.zip -d $app_dir
cd $app_dir

echo "Setting up venv:"
python3 -m venv venv
source venv/bin/activate

echo `pwd`

echo "Installing Requirements:"
pip install -r requirements.txt

python manage.py migrate

echo "Starting App:"
# Not ideal at all. But you get the idea !!. Do it properly for the type of application you are deploying.
killall gunicorn || true
gunicorn -b 0.0.0.0:8000 social.wsgi --daemon
sudo systemctl nginx restart

echo "Cleaning up:"
cd ..
rm build.zip