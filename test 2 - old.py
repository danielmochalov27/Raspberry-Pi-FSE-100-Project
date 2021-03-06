import RPi.GPIO as GPIO  #Raspberry Pi GPIO library
import time


BtnPin = 38
PIRPin = 32
PBuzzPin = 22
PBuzzPin2 = 23
UltraTrig = 16
UltraEcho = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PBuzzPin, GPIO.OUT)
#Buzzer is connected to Pin 22

GPIO.setup(PBuzzPin2, GPIO.OUT)
#Buzzer is connected to Pin 23

GPIO.setup(BtnPin, GPIO.INPUT, pull_up_down = GPIO.PUD_DOWN)
#PushButton is connected to Pin 38
GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)

GPIO.setup(PIRPin, GPIO.INPUT)
#PIR sensor conected to Pin 32

GPIO.setup(UltraEcho, GPIO.INPUT)
#Ultra Sonic Sensor input is connected to Pin 18

GPIO.setup(UltraTrig, GPIO.OUTPUT)
#Ultra Sonic Sensor output is connected to Pin 16

#Turning everything on

#End of turning everything on
def detect(channel)
  


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

# Main function
def main():
  try:
    # Repeat till the program is ended by the user
    while True:
      # Get the beeping frequency
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
  # If the program is ended, stop beeping and cleanup GPIOs
  except KeyboardInterrupt:
    GPIO.output(PBuzzPin, False)
    GPIO.cleanup()

while True:
  if GPIO.input(PIRPin): #If there is a movement, PIR sensor gives input to GPIO 32
     GPIO.output(PBuzzPin2, True) #Output given to Buzzer through GPIO 23  
     time.sleep(1) #Buzzer turns on for 1 second
     GPIO.output(PBuzzPin2, False)
     time.sleep(5) 
  time.sleep(0.1) 
  
# Run the main function when the script is executed
if __name__ == "__main__":
    main()