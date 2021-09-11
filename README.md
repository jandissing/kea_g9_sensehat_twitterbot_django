# kea_g9_sensehat_twitterbot

1 - clone this repository.

2 - install dependencies on local env:

pip install -r scripts/requirements.txt


3 - go to main folder and create a virtual environment in the folder:

python -m venv venv
source venv/bin/activate (to activate venv)


4 - install dependencies on virtual env:

pip install -r requirements-web.txt


5 - Edit the scripts/connection.py with your credentials to your Mariadb server.


6 - run create_db:

python scripts/create_db.py


7 - make migrations and migrate them to database:

python manage.py makemigrations

python manage.py migrate


8 - insert fake data to dabase:

python scripts/insert_fake_data.py


9 - create super user:

python manage.py createsuperuser


10 - go to 127.0.0.1:8000/admin and edit the table Team members. After inserting data it will be displayed on the web page.


11 - start django server:

python3 manage.py runserver


12 - go to 127.0.0.1:8000 and see live website


