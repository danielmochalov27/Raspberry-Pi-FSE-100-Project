import RPi.GPIO as GPIO #Raspberry Pi GPIO library
from time import sleep, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BtnPin = 38

def setup():
  GPIO.setup(BtnPin,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)#(pin number for button, sets to input, initial value (low state) equals off))
  GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=detect, bouncetime = 50)
  
#button
def detect(x):
    print ("button pressed")

#if x == 1:
 #   print("button on")
#if x == 0:
 #   print("button off")


def loop():
	while True:
		pass

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
