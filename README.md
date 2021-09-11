# kea_g9_sensehat_twitterbot

1 - clone this repository.

2 - install dependencies on local env:

If on local computer, run:

pip install -r scripts/requirements.txt

If on local raspberry pi, run:

pip install -r scripts/requirements-pi.txt


3 - go to main folder and create a virtual environment in the folder:

python3 -m venv venv
source venv/bin/activate (to activate venv)


4 - install dependencies on virtual env:

pip3 install -r requirementsweb.txt


5 - start django server:

python3 manage.py runserver


6 - go to 127.0.0.1:8000 and see live website