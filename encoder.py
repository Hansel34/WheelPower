from RPi import GPIO
from time import time

ßdt = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(dt, GPIO.IN, pull_up_down= GPIO.PUD_UP)

counter = 0


while True:
        t_end = time() + 1
        counter =0
        while time() <t_end:
                GPIO.wait_for_edge(dt,GPIO.RISING)
                counter += 1
                print ("There are" +str(counter/10) +"Rotations per second")


