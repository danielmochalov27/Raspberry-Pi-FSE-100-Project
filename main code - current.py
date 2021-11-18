import RPi.GPIO as GPIO #makes sure you can interact with the pins on the pi
import time #counts

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#sets up all the pins for the sensors
BtnPin = 40
PIRPin = 38
PBuzzPin = 22
PBuzzPin2 = 16
UltraTrig = 35
UltraEcho = 32

GPIO.setup(BtnPin, GPIO.IN)
#Button is connected to pin 40

GPIO.setup(PBuzzPin, GPIO.OUT)
#Buzzer is connected to Pin 22

GPIO.setup(PBuzzPin2, GPIO.OUT)
#Buzzer 2is connected to Pin 16

GPIO.setup(PIRPin, GPIO.IN)
#PIR sensor conected to Pin 38

GPIO.setup(UltraEcho, GPIO.IN)
#Ultra Sonic Sensor input is connected to Pin 32

GPIO.setup(UltraTrig, GPIO.OUT)
#Ultra Sonic Sensor output is connected to Pin 35

#this code is for the PIR sensors (motion sensor) when it detects motion it beeps with one type of tone
def pir_motion(PIRPin):
  print("pir motion detected")

  Buzz = GPIO.PWM(16, 440)
  Buzz.start(0)
  Buzz.ChangeDutyCycle(50)
  time.sleep(1)
  Buzz.stop()

  GPIO.output(16, 1)
  time.sleep(2.0)
  GPIO.output(16, 0)

GPIO.add_event_detect(PIRPin, GPIO.RISING, callback = pir_motion)
#
#This code is for the ultrasonic sensor (distance sensor) sensor will click faster and faster as you get closer to something
def ultra_ir_distance():
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
 ultra_distance = during*17150
 ultra_distance = round(ultra_distance, 2)

 return ultra_distance

  # Calculates the frequency of beeping depending on the measured distance
def beep_freq():
  # Measure the distance
  ultra_distance = ultra_ir_distance()
  # If the distance is bigger than 200cm, we will not beep at all
  if ultra_distance > 200:
    return -1
  # If the distance is between 200 and 120 cm, we will beep once a second
  elif ultra_distance <= 200 and ultra_distance >= 120:
    return 1
  # If the distance is between 120 and 80 cm, we will beep every twice a second
  elif ultra_distance < 120 and ultra_distance >= 80:
    return 0.5
  # If the distance is between 80 and 40 cm, we will beep four times a second
  elif ultra_distance < 80 and ultra_distance >= 40:
    return 0.25
  # If the distance is smaller than 40 cm, we will beep constantly
  else:
    return 0

while True:
    # waiting for button press
    print("Sensors OFF")
    while GPIO.input(BtnPin) == 1:
     time.sleep(0.2)

    time.sleep(0.2)
    
    print ("Sensors ON")
    while GPIO.input(BtnPin) == 1:

      freq = beep_freq()
      # No beeping
      if freq == -1:
        GPIO.output(PBuzzPin, False)
        time.sleep(0.25)
        print("ultra not detected")

        # Constant beeping
      elif freq == 0:
        GPIO.output(PBuzzPin, True)
        time.sleep(0.25)
        print("ultra detected close")
        # Beeping on certain frequency
      else:
        GPIO.output(PBuzzPin, True)
        time.sleep(0.2) # Beep is 0.2 seconds long
        GPIO.output(PBuzzPin, False)
        time.sleep(freq) # Pause between beeps = beeping frequency
        print("ultra detected")  