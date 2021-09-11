import mysql.connector as mariadb
import time
from connection import user, password

print("Insert_fake_data running...")

conn = mariadb.connect(user=user, password=password,
                       host='localhost', port='3306')
mycursor = conn.cursor()

print("Inserting fake data inating table HatData")
mycursor.execute("INSERT INTO DB.HatData (DateTime, Temperature, Humidity, Pressure) values ('2021-09-10 10:00:00', '30', '35', '1001.3'),('2021-09-10 10:01:00', '31', '36', '1001.6'),('2021-09-10 10:02:00', '34', '38', '1001.8'),('2021-09-10 10:03:00', '29', '35', '1001.5'),('2021-09-10 10:04:00', '30', '33', '1001.2');")
conn.commit()

print("Inserting fake data in table LastseenId")
mycursor.execute(
    "INSERT INTO  DB.LastSeenId (LastSeenId, User, created_at, Img_link, Tweet) values ('0001', 'johnny009', '2021-09-09 20:25:00', 'https://pbs.twimg.com/profile_images/1435190386142715908/JzAiW7p__400x400.jpg', 'What is the temperature?'), ('0002', 'mark002', '2021-09-09 20:30:00', 'https://pbs.twimg.com/profile_images/1390573724328513537/N63w2Ffb_400x400.jpg', 'Please tell me the Humidity measurement'), ('0003', 'pietra001', '2021-09-09 20:35:00', 'https://pbs.twimg.com/profile_images/1415153929021624327/lduIZO4i_400x400.jpg', 'Pressure?');")

conn.commit()

print("Inserting fake data complete")
conn.close()
