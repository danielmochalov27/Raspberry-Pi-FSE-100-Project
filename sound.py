import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


PBuzzPin2 = 16
GPIO.setup(PBuzzPin2, GPIO.OUT)


while True:
 GPIO.output(PBuzzPin2, 1)
 time.sleep(2.0)
 GPIO.output(PBuzzPin2, 0)
 time.sleep(0.2)