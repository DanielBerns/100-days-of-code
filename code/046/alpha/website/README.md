# How to install

## Make virtual environment web

$ mkdir ~/.venvs
$ python -m venv ~/.venvs/web
$ . ~/.venvs/web/bin/activate


## Install python libraries

$ pip install flask flask-login requests pillow
$ pip install flask-wtf flask-sqlalchemy flask-migrate python-dotenv
$ pip install FLASK-Mail email-validator Flask-JWT
$ pip install Flask-HTTPAuth

## Start

### Create database
1. $ cd server
2. $ ./create_db.sh
