from RPi import GPIO
from time import sleep

dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:
        while True:
                dtState = GPIO.input(dt)
                counter += 1
                print counter
                sleep(0.01)
finally:
        GPIO.cleanup()