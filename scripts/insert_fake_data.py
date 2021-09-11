import mysql.connector as mariadb
import time
from connection import user, password

print("Insert_fake_data running...")

conn = mariadb.connect(user=user, password=password,
                       host='localhost', port='3306')
mycursor = conn.cursor()

print("CreInserting fake data inating table HatData")
mycursor.execute("INSERT INTO DB.HatData (DateTime, Temperature, Humidity, Pressure) values ('2021-09-10 10:00:00', '30', '35', '1001.3',),(2021-09-10 10:01:00, '31', '36', '1001.6'),(2021-09-10 10:02:00, '34', '38', '1001.8'),(2021-09-10 10:03:00, '29', '35', '1001.5'),(2021-09-10 10:04:00, '30', '33', '1001.2')")
conn.commit()

print("Inserting fake data in table LastseenId")
mycursor.execute(
    "INSERT INTO  DB.LastSeenId (LastSeenId, User, created_at, Img_link) values ('0001', 'johnny009', '2021-09-09 20:25:00', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fdepositphotos.com%2Fvector-images%2Fprofile-picture.html&psig=AOvVaw3YviQ3BPCQYqeCGDB0v4Aj&ust=1631448844084000&source=images&cd=vfe&ved=2ahUKEwjYiuvX8vbyAhUSgqQKHVrPAXAQjRx6BAgAEAk'), ('0002', 'mark002', '2021-09-09 20:30:00', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fprofile%2520picture%2F&psig=AOvVaw2Nf2bxK7U7FE5WHzt4jEmI&ust=1631448851645000&source=images&cd=vfe&ved=2ahUKEwj1w7jb8vbyAhWyNOwKHSD-DgUQjRx6BAgAEAk'), ('0003', 'pietra001', '2021-09-09 20:35:00', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fprofile-photo&psig=AOvVaw2DHNxjIJ0RR9rynTPDB0g8&ust=1631448848392000&source=images&cd=vfe&ved=2ahUKEwi4_vHZ8vbyAhVTlKQKHV2ZCjUQjRx6BAgAEAk')")

conn.commit()

print("Inserting fake data complete")
conn.close()