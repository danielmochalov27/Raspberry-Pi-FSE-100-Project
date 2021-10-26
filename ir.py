import RPi.GPIO as GPIO #Raspberry Pi GPIO library
from time import sleep, time

#Initialization:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

IrPin = 11
PBuzzPin = 17

def setup():
  GPIO.setup(IrPin,GPIO.IN)
  
  GPIO.setup(PBuzzPin,GPIO.OUT)
  GPIO.output(PBuzzPin,GPIO.HIGH)

  #Passive Button Methods
def ABuzzOn():
  GPIO.output(PBuzzPin, GPIO.LOW)

def ABuzzOff():
  GPIO.output(PBuzzPin, GPIO.HIGH)

def ABuzzBeep(x):
  ABuzzOn()
  time.sleep(x)
  ABuzzOff()
  time.sleep(x)