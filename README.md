# KEA Group 9 — Sense HAT Twitter Bot

A KEA (Copenhagen School of Design and Technology) group project (Group 9): a Raspberry
Pi collects live environmental readings from a Sense HAT (temperature, pressure,
humidity), a Twitter bot answers mentions with those readings, and a Django web
dashboard displays the team and a live chart of recent measurements.

## What it does

- **`scripts/green.py`** — polls the Sense HAT continuously, scrolls the current
  reading across its LED matrix, and writes each sample to MariaDB (`HatData` table)
- **`scripts/bot.py`** — a Twitter bot (Tweepy) that polls mentions and replies with
  live temperature/pressure/humidity when a mention contains one of those keywords;
  tracks the last tweet it answered (`LastSeenId` table) so it never replies twice
- **Django web app** (`web/`) — a dashboard showing the team, the last 15 sensor
  readings as a time-series chart, and the tweets the bot has answered
- **`scripts/script1.py`, `script2.py`, `clear_led.py`** — small standalone demos for
  the Sense HAT LED matrix (show a message, scroll the current temperature, clear the
  display)

## Architecture

```
core/            Django project settings, URLs, WSGI/ASGI entrypoints
web/             The dashboard app — models (HatData, LastSeenId, TeamMember),
                 views, admin
scripts/         Standalone scripts that talk to the Sense HAT + MariaDB directly,
                 outside the Django app (bot.py, green.py, script1/2.py, clear_led.py)
templates/       Server-rendered dashboard pages
```

The web dashboard and the sensor/bot scripts share the same MariaDB database but run as
separate processes — the Django app only reads and displays what the scripts write.

## Running it

Requires a Raspberry Pi with a Sense HAT attached (or the
[Sense HAT emulator](https://sense-hat.readthedocs.io/en/latest/simulate.html) for
`scripts/*.py`), and a MariaDB server.

```bash
git clone <this repo>
pip install -r scripts/requirements.txt        # Sense HAT + MariaDB scripts

python -m venv venv && source venv/bin/activate
pip install -r requirements-web.txt             # Django web app

# edit scripts/connection.py with your MariaDB credentials
python scripts/create_db.py
python manage.py makemigrations
python manage.py migrate
python scripts/insert_fake_data.py               # optional: sample data
python manage.py createsuperuser

python manage.py runserver                       # dashboard at 127.0.0.1:8000
python scripts/green.py                           # on the Pi: log sensor readings
python scripts/bot.py                             # on the Pi: run the Twitter bot
```

Visit `127.0.0.1:8000/admin` to add team members so they show up on the dashboard.

## Known limitations (kept for historical accuracy)

This was a graded coursework deliverable (2021), not a maintained project:

- **Twitter API credentials and the Django `SECRET_KEY` were originally hardcoded** in
  source rather than loaded from environment variables. The Twitter credentials have
  since been verified dead — the associated token no longer authenticates.
- **`scripts/bot.py` builds one query with an f-string** rather than a parameterized
  statement — a known anti-pattern, kept as-is here rather than silently patched.
- Requires physical Sense HAT hardware (or its emulator) to run the sensor/bot scripts;
  the Django dashboard itself can run without it, using sample data.
- The frontend theme (`static/scss/now-ui-dashboard/`) is the third-party
  [Now UI Dashboard](https://www.creative-tim.com/product/now-ui-dashboard) template by
  Creative Tim, not original code — marked `linguist-vendored` in `.gitattributes`.

## Stack

Python · Django 3.2 · MariaDB/MySQL · Tweepy · sense-hat · matplotlib · pandas
