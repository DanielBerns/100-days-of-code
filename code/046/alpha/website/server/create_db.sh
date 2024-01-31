#!/usr/bin/env bash

rm -rf ~/data/athena/website/logs/
rm -rf ~/data/athena/website/store/
rm -rf ./migrations    

mkdir -p ~/data/athena/website/logs/
mkdir -p ~/data/athena/website/store/

source ~/.venvs/web/bin/activate
export FLASK_APP=./website.py
flask db init
flask db migrate -m "start"
flask db upgrade
deactivate
