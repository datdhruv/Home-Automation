import RPi.GPIO as GPIO
from time import sleep 

## set LED default to ,ow in controller program

def LED(a):
    if (a == "on"):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(1, GPIO.OUT, initial=GPIO.HIGH)


    elif (a == "off"):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW)

    return (9)
LED('on')
