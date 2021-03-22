import RPi.GPIO as gpio
from time import sleep 

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(21,gpio.OUT)
gpio.setup(14,gpio.OUT)

def SERVO_control():
    gpio.output(14,gpio.HIGH)
    p = gpio.PWM(14, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    p.ChangeDutyCycle(10)
    #time.sleep(5)
    sleep(5)
    p.ChangeDutyCycle(5)
    sleep(5)
    p.stop()
    sleep(5)
    gpio.output(21,gpio.LOW)
    
    # Debug msg
    print("--- Servo cycle compelted succelfully ---")

def handle(msg):
    if msg == "SERVO":
        SERVO_control()
    
    if (msg == "LED ON"):
        gpio.output(21, gpio.HIGH)
        
        # Debug message
        print("LED turned on")

    elif (msg == "LED OFF"):
        gpio.output(21, gpio.LOW)
        
        # Debug message
        print("Led turned off")

    else:
        print("Error command not found")
