#!/bin/bash

export $(cat .env | grep -v ^# | xargs)
rm -rf db.sqlite3
rm -rf pages/migrations
python3 manage.py makemigrations
python3 manage.py makemigrations pages
python3 manage.py migrate
python3 manage.py migrate pages
python3 manage.py populate_locations
python3 manage.py runserver