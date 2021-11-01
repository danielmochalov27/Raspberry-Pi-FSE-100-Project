import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

BtnPin = 40
PIRPin = 36
PBuzzPin = 22
PBuzzPin2 = 35
UltraTrig = 16
UltraEcho = 12

BtnOn = False

GPIO.setup(BtnPin, GPIO.IN)  #button

GPIO.setup(PBuzzPin, GPIO.OUT)
#Buzzer is connected to Pin 22

GPIO.setup(PBuzzPin2, GPIO.OUT)
#Buzzer is connected to Pin 23

GPIO.setup(PIRPin, GPIO.IN)
#PIR sensor conected to Pin 32

GPIO.setup(UltraEcho, GPIO.IN)
#Ultra Sonic Sensor input is connected to Pin 18

GPIO.setup(UltraTrig, GPIO.OUT)
#Ultra Sonic Sensor output is connected to Pin 16


def distance():
  # Send 10 microsecond pulse to TRIGGER
  GPIO.output(UltraTrig, True) # set TRIGGER to HIGH
  time.sleep(0.00001) # wait 10 microseconds
  GPIO.output(UltraTrig, False) # set TRIGGER back to LOW
 
  # Create variable start and assign it current time
  start = time.time()
  # Create variable stop and assign it current time
  stop = time.time()
  # Refresh start value until the ECHO goes HIGH = until the wave is send
  while GPIO.input(UltraEcho) == 0:
    start = time.time()
 
  # Assign the actual time to stop variable until the ECHO goes back from HIGH to LOW = the wave came back
  while GPIO.input(UltraEcho) == 1:
    stop = time.time()
 
  # Calculate the time it took the wave to travel there and back
  measuredTime = stop - start
  # Calculate the travel distance by multiplying the measured time by speed of sound
  distanceBothWays = measuredTime * 33112 # cm/s in 20 degrees Celsius
  # Divide the distance by 2 to get the actual distance from sensor to obstacle
  distance = distanceBothWays / 2

  # Print the distance to see if everything works correctly
  print("Distance : {0:5.1f}cm".format(distance))
  # Return the actual measured distance
  return distance

  # Calculates the frequency of beeping depending on the measured distance
def beep_freq():
  # Measure the distance
  dist = distance()
  # If the distance is bigger than 50cm, we will not beep at all
  if dist > 50:
    return -1
  # If the distance is between 50 and 30 cm, we will beep once a second
  elif dist <= 50 and dist >=30:
    return 1
  # If the distance is between 30 and 20 cm, we will beep every twice a second
  elif dist < 30 and dist >= 20:
    return 0.5
  # If the distance is between 20 and 10 cm, we will beep four times a second
  elif dist < 20 and dist >= 10:
    return 0.25
  # If the distance is smaller than 10 cm, we will beep constantly
  else:
    return 0

while True:
    # waiting for button press
    while GPIO.input(BtnPin) == 1:
        time.sleep(0.2)

    print ("plz")
    while GPIO.input(BtnPin == 1):

      freq = beep_freq()
      # No beeping
      if freq == -1:
        GPIO.output(PBuzzPin, False)
        time.sleep(0.25)
        # Constant beeping
      elif freq == 0:
        GPIO.output(PBuzzPin, True)
        time.sleep(0.25)
        # Beeping on certain frequency
      else:
        GPIO.output(PBuzzPin, True)
        time.sleep(0.2) # Beep is 0.2 seconds long
        GPIO.output(PBuzzPin, False)
        time.sleep(freq) # Pause between beeps = beeping frequency

    
        

