from RPi import GPIO
from time import time

dt = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(dt, GPIO.IN, pull_up_down= GPIO.PUD_UP)

counter = 0
t_end = time() + 1
counter =0
while True:
	GPIO.wait_for_edge(dt,GPIO.RISING)
	counter+=1
	if (counter % 100 == 0):
                print ("The wheelchair has travelled " +str(counter/200*21) +" CM so far")


