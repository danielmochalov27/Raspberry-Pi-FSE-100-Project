#!/usr/bin/env python3
import RPi.GPIO as GPIO #Raspberry Pi GPIO library
import ir, rgb, ultrasonic

#Initialization:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BtnPin = 21

def setup():
  GPIO.setup(BtnPin,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)#(pin number for button, sets to input, initial value (low state) equals off))
  GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect, bouncetime = 50)

def detect(channel):
  global ultrasonic_ir_reader
  global rgb_reader

  if GPIO.input(BtnPin) == GPIO.HIGH:
      ultrasonic_ir_reader = True
      rgb_reader = True
  else:
      ultrasonic_ir_reader = False
      rgb_reader = False

while True:
  while ultrasonic_ir_reader:
    print("ultrasonic_ir_reader")
    #ultrasonic.ultra_react()
