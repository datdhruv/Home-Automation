import RPi.GPIO as GPIO
from time import sleep 

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(1,gpio.OUT)


## set LED default to ,ow in controller program

def SERVO_control():
    gpio.output(21,gpio.HIGH)
    p = gpio.PWM(14, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    p.ChangeDutyCycle(10)
    time.sleep(5)
    p.ChangeDutyCycle(5)
    time.sleep(5)
    p.stop()
    sleep(5)
    gpio.output(21,gpio.LOW)

