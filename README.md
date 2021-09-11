# kea_g9_sensehat_twitterbot

1 - clone this repository.

2 - install dependencies on local env:

If on local computer, run:

pip install -r scripts/requirements.txt

If on remote raspberry pi, run:

pip install -r scripts/requirements-pi.txt


3 - go to main folder and create a virtual environment in the folder:

If If on local computer, substitute python3 for python:

python3 -m venv venv
source venv/bin/activate (to activate venv)


4 - install dependencies on virtual env:

If If on local computer:

pip install -r requirements-web.txt

If on remote raspberry pi, run:

pip3 install -r requirements-web-pi.txt


5 - If on local computer: run create_db:

python scripts/create_db.py


6 - If on local computer: make migrations and migrate them to database:

python manage.py makemigrations

python manage.py migrate


7 - If on local computer: insert fake data to dabase:

python scripts/insert_fake_data.py


8 - create super user:

python manage.py createsuperuser


9 - go to 127.0.0.1:8000/admin and edit the table Team members. After inserting data it will be displayed on the web page.


10 - start django server:

python3 manage.py runserver


8 - go to 127.0.0.1:8000 and see live website


