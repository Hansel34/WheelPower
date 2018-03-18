#import thread
import signal
import sys
import numpy

from CompFilter import *
from driverClass import *

# Initialize driver/sensor classes
drive = driver()
compFilter = CompFilter()

# Set up variables
flat_thresh = -15
down_thresh = -13
up_thresh = -17
debounce = 50
angle = 0

# Signal handler (Ctrl+C)
def signal_handler(signal, frame):
    drive.stop()
    sys.exit()

# Retrieve previous x angles and average them
def get_angle():
   # angle = numpy.mean( [compFilter() for i in range(debounce)] )
    angle = 0
    for x in range(50):
        compFilter()
        angle += compFilter.angle
    angle = angle/50
    print (angle)
    
# Move chair based on angle
def move_chair():
    if abs(angle) > abs(up_thresh):
        drive.forward()
        print("Moving forward")

    elif abs(angle) < abs(down_thresh):
        drive.backward()
        print("Moving backwards")

    else:
        drive.stop()
        print("Not assisting");

# Main
signal.signal(signal.SIGINT, signal_handler)
while True:
    get_angle()
    move_chair()
