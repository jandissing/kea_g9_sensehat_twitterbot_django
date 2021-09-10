from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()
# Set colorblue = (0,0,255)
while True:
    temp = sense.get_temperature()
    sense.show_message(str(round(temp, 1)), scroll_speed=0.09)
    time.sleep(5)
