# szkola-w-chmurze
An application that allows users to send a long url and receive url's short version.

## Development setup
- OS Linux ubuntu
- Install Python 3.10
- Create Virtual Environment
`python3 -m venv venv`
- Activate venv
`source venv/bin/activate`
- Install dependencies
`pip install -r requirements.txt`

## Migrate db:
`python3 manage.py makemigrations` <br/>
`python3 manage.py migrate`

## Create an admin account:
`python manage.py createsuperuser`

## Runserver

`cd main` <br/>
`python manage.py runserver`

## How to test via Postman
Attached `szkola-w-chmurze.postman_collection.json` file.
