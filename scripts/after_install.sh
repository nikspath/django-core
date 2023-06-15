#!/usr/bin/env bash

# kill any servers that may be running in the background 
sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd /home/ubuntu/django-core/

# activate virtual environment
python3 -m venv venv
source venv/bin/activate

install requirements.txt
pip install -r /home/ubuntu/django-core/requirements.txt

# run server
#screen -d -m python3 manage.py makemigrations
#screen -d -m python3 manage.py migrate
screen -d -m python3 manage.py runserver 0.0.0.0:8000

# django-core-cicd = awsservice and ec2 role
#$ django-core-cicd-codedeploy = awservice and codedeploy