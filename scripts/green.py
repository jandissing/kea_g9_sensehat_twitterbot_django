import time
import mysql.connector as mariadb
from sense_hat import SenseHat
from datetime import datetime
from connection import user, password

print("Green script running...")
conn = mariadb.connect(user=user, password=password,
                       database='DB', host='localhost', port='3306')
mycursor = conn.cursor()

sense = SenseHat()

while True:
    print("Getting measurements from SenseHat: (Type Ctrl+C to exit)")
    temp = round(sense.get_temperature(), 1)
    pressure = round(sense.get_pressure(), 1)
    humidity = round(sense.get_humidity())
    dateandtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"{dateandtime} - T:{temp}C,  P:{pressure} bars,  H:{humidity}%"
    print(message)
    sense.show_message(message)
    print()
    mycursor = conn.cursor()
    mycursor.execute(
        f"INSERT INTO HatData (DateTime, Temperature, Humidity, Pressure) values ('{dateandtime}', '{temp}', '{humidity}', '{pressure}')")
    conn.commit()
    time.sleep(5)
    mycursor.execute("SELECT * FROM HatData")
    print(mycursor.fetchall())
    print()
    time.sleep(5)
