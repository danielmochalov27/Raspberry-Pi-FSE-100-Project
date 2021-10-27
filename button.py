#!/usr/bin/env python3
import RPi.GPIO as GPIO #Raspberry Pi GPIO library
from time import sleep, time

#Initialization:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BtnPin = 38
IrPin = 32
PBuzzPin = 22
UltraTrig = 16
UltraEcho = 18

ultrasonic_ir_reader = True

def setup():
  GPIO.setup(BtnPin,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)#(pin number for button, sets to input, initial value (low state) equals off))
  GPIO.setup(IrPin,GPIO.IN)
  GPIO.setup(PBuzzPin,GPIO.OUT)
  GPIO.output(PBuzzPin,GPIO.HIGH)
  GPIO.setup(UltraTrig, GPIO.OUT)
  GPIO.setup(UltraEcho, GPIO.IN)

  GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect, bouncetime = 50)


#Passive Button Methods
def PBuzzOn():
 GPIO.output(PBuzzPin, GPIO.LOW)
 
def PBuzzOff():
 GPIO.output(PBuzzPin, GPIO.HIGH)
 
def PBuzzBeep(x):
 PBuzzOn()
 time.sleep(x)
 PBuzzOff()
 time.sleep(x)

#returns ultra_distance and ir_sense
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
 
 ir_sense = 0

 if GPIO.input(IrPin):
  ir_sense = 1
 else:
  ir_sense = 0

 ultra_ir_sense = [ultra_distance, ir_sense]
 return ultra_ir_sense

#button
def detect(channel):
  #global rgb_reader
  print ("button pressed")
  global ultrasonic_ir_reader

  if GPIO.input(BtnPin) == GPIO.HIGH:
    ultrasonic_ir_reader = True
    print("button on")
    #rgb_reader = True
  else:
    ultrasonic_ir_reader = False
    print("button off")
    #rgb_reader = False

while True:
  while ultrasonic_ir_reader:
    print("ultrasonic_ir_reader")
    ultra_ir_list = ultra_ir_distance()
    if(ultra_ir_list[0] < 1):
      print("ultransonic sensor detected")
      PBuzzBeep(0.5)
    if(ultra_ir_list[1] == 1):
      print("ir sensor detected")
      PBuzzBeep(0.25)

def loop():
	while True:
		pass

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		GPIO.cleanup()
