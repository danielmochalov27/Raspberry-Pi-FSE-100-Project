import RPi.GPIO as GPIO #Raspberry Pi GPIO library
from time import sleep, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BtnPin = 38

buttonOn = False

def setup():
  GPIO.setup(BtnPin,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)#(pin number for button, sets to input, initial value (low state) equals off))
  GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect, bouncetime = 50)
  
#button
def detect(chn):
  print ("button pressed")
  if(buttonOn):
    buttonOn = False
  else:
    buttonOn = True

def loop():
  while True: 
    if(buttonOn):
      print("1")
    else:
      print("0")
    pass

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		pass
