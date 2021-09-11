import tweepy
import time
import mysql.connector as mariadb
from sense_hat import SenseHat
from connection import user, password

sense = SenseHat()

conn = mariadb.connect(user=user, password=password,
                       database='DB', host='localhost', port='3306')

mycursor = conn.cursor()

print("Twitter bot running...")

CONSUMER_KEY = 'gV6LIFTB905o0xpZ550zEFzH2'
CONSUMER_SECRET = 'Tq7b7EJLbytN5u8T57jzeVtuwdITMMaKVr08GoC1eyZGdPfvMS'
ACCESS_KEY = '1433822353860055041-9GcjlHJ035AjB8XCqCRfI1lrF6enib'
ACCESS_SECRET = 'mgrD2OEG05hZ2ETITUcitr1hvJHkBs0xOLl2rqDLAhcLS'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def retrieve_last_seen_id():
    conn = mariadb.connect(user=user, password=password,
                           database='DB', host='localhost', port='3306')

    mycursor = conn.cursor()
    mycursor.execute(
        "SELECT * FROM LastSeenId ORDER BY (Id) DESC LIMIT 1;")
    a = mycursor.fetchall()
    print(a)
    if not a:
        print("The HatData table is empty!")
        print("Not responding old tweets...")
        mentions = api.mentions_timeline(tweet_mode='extended')
        print(mentions[0].id)
        last_seen_id = mentions[0].id
        store_last_seen_id(
            last_seen_id, mentions[0].user.screen_name, mentions[0].created_at, mentions[0].user.profile_image_url_https, mentions[0].full_text)

    else:
        for x in a:
            print(x)
            last_seen_id = x[1]
            print(last_seen_id)
    return last_seen_id


def store_last_seen_id(last_seen_id, user, created_at, profile_image_url_https, full_text):
    conn = mariadb.connect(user=user, password=password,
                           database='DB', host='localhost', port='3306')
    mycursor = conn.cursor()
    mycursor.execute(
        f"INSERT INTO LastSeenId (LastSeenId, User, created_at, img_link, Tweet) values ('{(last_seen_id)}', '{user}', '{created_at}', '{profile_image_url_https}', '{full_text}')")
    conn.commit()
    return


def reply():
    print('retrieving and responding to tweets...')
    last_seen_id = retrieve_last_seen_id()

    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    print(mentions)

    for m in reversed(mentions):
        print(str(m.id) + ' - ' + m.full_text)
        last_seen_id = m.id
        store_last_seen_id(last_seen_id, m.user.screen_name,
                           m.created_at, m.user.profile_image_url_https, m.full_text)
        if 'pressure' in m.full_text.lower() and 'temperature' in m.full_text.lower() and 'humidity' in m.full_text.lower():
            print('found keyphrase')
            print('responding back...')

            api.update_status(
                f"@{m.user.screen_name} Temperature:{round(sense.get_temperature(), 1)}C, Pressure:{round(sense.get_pressure(), 1)}hPa, Humidity:{round(sense.get_humidity())}%", m.id)

        elif 'pressure' in m.full_text.lower() and 'humidity' in m.full_text.lower():
            print('found keyphrase')
            print('responding back...')

            api.update_status(
                f"@{m.user.screen_name} Pressure:{round(sense.get_pressure(), 1)}hPa, Humidity:{round(sense.get_humidity())}%", m.id)

        elif 'pressure' in m.full_text.lower() and 'temperature' in m.full_text.lower():
            print('found keyphrase')
            print('responding back...')

            api.update_status(
                f"@{m.user.screen_name} Temperature:{round(sense.get_temperature(), 1)}C, Pressure:{round(sense.get_pressure(), 1)}hPa", m.id)

        elif 'temperature' in m.full_text.lower() and 'humidity' in m.full_text.lower():
            print('found keyphrase')
            print('responding back...')

            api.update_status(
                f"@{m.user.screen_name} Temperature:{round(sense.get_temperature(), 1)}C, Humidity:{round(sense.get_humidity())}%", m.id)

        elif 'pressure' in m.full_text.lower():
            print('found keyphrase')
            print('responding back...')

            api.update_status(
                f"@{m.user.screen_name} Pressure:{round(sense.get_pressure(), 1)}hPa", m.id)

        elif 'temperature' in m.full_text.lower():
            print('found keyphrase')
            print('responding back...')

            api.update_status(
                f"@{m.user.screen_name} Temperature:{round(sense.get_temperature(), 1)}C", m.id)

        elif 'humidity' in m.full_text.lower():
            print('found keyphrase')
            print('responding back...')

            api.update_status(
                f"@{m.user.screen_name} Humidity:{round(sense.get_humidity())}%", m.id)


while True:
    reply()
    time.sleep(15)
