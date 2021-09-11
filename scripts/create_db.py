import mysql.connector as mariadb
import time
from connection import user, password

print("Create_db running...")

conn = mariadb.connect(user=user, password=password,
                       host='localhost', port='3306')
mycursor = conn.cursor()

print("Dropping if exists database DB")
mycursor.execute("DROP DATABASE if exists DB")
conn.commit()

print("Creating a database DB")
mycursor.execute("CREATE DATABASE DB")
conn.commit()

time.sleep(2)
print("Creating table LastseenId")
mycursor.execute(
    "CREATE TABLE DB.LastSeenId (Id int auto_increment not null, LastSeenId VARCHAR(19), User VARCHAR(150), created_at DATETIME, Img_link VARCHAR(512), primary key (Id))")
conn.commit()

print("Creating table HatData")
mycursor.execute("CREATE TABLE DB.HatData (Id int auto_increment not null, DateTime DATETIME, Temperature DECIMAL(3,1), Humidity Int, Pressure DECIMAL(5,1), primary key (Id))")
conn.commit()

print("Creating complete")
conn.close()
