import RPi.GPIO as GPIO #Raspberry Pi GPIO library
from time import sleep, time

#Initialization:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

RgbPin = 13

def setup():
  GPIO.setup(RgbPin,GPIO.IN)

  