import RPi.GPIO as GPIO
from time import sleep 

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(1,gpio.OUT)


## set LED default to ,ow in controller program

def LED_control(msg):
    if (msg == "LED ON"):
        gpio.output(1, gpio.HIGH)
        
        # Debug message
        print("LED turned on")

    elif (msg == "LED OFF"):
        gpio.output(1, gpio.LOW)
        
        # Debug message
        print("Led turned off")
    
