from RPi import GPIO
from time import sleep

dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(dt, GPIO.IN, pull_up_down= GPIO.PUD_UP)

counter = 0

try:
        while True:
                print (GPIO.wait_for_edge(dt,GPIO.RISING))

finally:
        GPIO.cleanup()
