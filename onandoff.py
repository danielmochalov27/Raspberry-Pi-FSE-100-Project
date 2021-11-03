import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

BtnPin = 40
PIRPin = 38
PBuzzPin = 22
PBuzzPin2 = 16
UltraTrig = 35
UltraEcho = 32

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
 ultra_distance = (during * 340)/2
 
 pir_sense = 0

 if GPIO.input(PIRPin):
  pir_sense = 1
 else:
  pir_sense = 0

 ultra_ir_sense = [ultra_distance, pir_sense]
 return ultra_ir_sense

  # Calculates the frequency of beeping depending on the measured distance
def beep_freq():
  # Measure the distance
  ultra_ir_list = ultra_ir_distance()
  # If the distance is bigger than 50cm, we will not beep at all
  if ultra_ir_list[0] > 50:
    return -1
  # If the distance is between 50 and 30 cm, we will beep once a second
  elif ultra_ir_list[0] <= 50 and ultra_ir_list[0] >=30:
    return 1
  # If the distance is between 30 and 20 cm, we will beep every twice a second
  elif ultra_ir_list[0] < 30 and ultra_ir_list[0] >= 20:
    return 0.5
  # If the distance is between 20 and 10 cm, we will beep four times a second
  elif ultra_ir_list[0] < 20 and ultra_ir_list[0] >= 10:
    return 0.25
  # If the distance is smaller than 10 cm, we will beep constantly
  else:
    return 0

def PBuzzBeep2(x):
  GPIO.output(PBuzzPin2, GPIO.LOW)
  time.sleep(x)
  GPIO.output(PBuzzPin2, GPIO.HIGH)

while True:
    # waiting for button press
    while GPIO.input(BtnPin) == 1:
     time.sleep(0.2)

    print ("Sensors ON")
    while GPIO.input(BtnPin) == 1:
    
      ultra_ir_list = ultra_ir_distance()
      pir_sense1 = ultra_ir_list[1]

      if ultra_ir_list[1] == 1:
        PBuzzBeep2(0.5)
        print("pir detected")

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
        print("ultra detected far")
        # Beeping on certain frequency
      else:
        GPIO.output(PBuzzPin, True)
        time.sleep(0.2) # Beep is 0.2 seconds long
        GPIO.output(PBuzzPin, False)
        time.sleep(freq) # Pause between beeps = beeping frequency
        print("ultra detected")
      print("Sensors OFF")