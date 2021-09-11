# kea_g9_sensehat_twitterbot

<b>1 - clone this repository.</b> 

<b>2 - install dependencies on local env:</b> 

pip install -r scripts/requirements.txt


<b>3 - go to main folder and create a virtual environment in the folder:</b> 

python -m venv venv

source venv/bin/activate (to activate venv)


<b>4 - install dependencies on virtual env:</b> 

pip install -r requirements-web.txt


<b>5 - Edit the scripts/connection.py with your credentials to your Mariadb server.</b> 


<b>6 - run create_db:</b> 

python scripts/create_db.py


<b>7 - make migrations and migrate them to database:</b> 

python manage.py makemigrations

python manage.py migrate


<b>8 - insert fake data to dabase:</b> 

python scripts/insert_fake_data.py


<b>9 - create super user:</b> 

python manage.py createsuperuser


<b>10 - go to 127.0.0.1:8000/admin and edit the table Team members. After inserting data it will be displayed on the web page.


<b>11 - start django server:</b> 

python3 manage.py runserver


<b>12 - go to 127.0.0.1:8000 and see live website</b> 


