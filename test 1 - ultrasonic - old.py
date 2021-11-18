import RPi.GPIO as GPIO #Raspberry Pi GPIO library
from time import sleep, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

UltraTrig = 12
UltraEcho = 13
PBuzzPin = 17

def setup():
  GPIO.setup(UltraTrig, GPIO.OUT)
  GPIO.setup(UltraEcho, GPIO.IN)
  
  GPIO.setup(PBuzzPin,GPIO.OUT)
  GPIO.output(PBuzzPin,GPIO.HIGH)

ultrasonic_reader = False

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

def ultra_distance():
  GPIO.output(UltraTrig, True)
  time.sleep(0.00001)

  GPIO.output(UltraTrig, False)

  startTime = time.time()
  endTime = time.time()

  while GPIO.input(UltraEcho) == 0:
    startTime = time.time()
  while GPIO.input(UltraEcho) == 1:
    endTime = time.time()

  during = endTime - startTime
  distance = (during * 340)/2

  return distance

def ultra_react():
  while ultrasonic_reader:
    if ultra_distance() <= 1:
     ABuzzBeep(0.5)