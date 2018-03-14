import thread
import signal
import sys

import CompFilter.py as cf
import driverClass.py as d

# Initialize driver/sensor classes
drive = driver()
compFilter = CompFilter()

# Set up variables
down_thresh = -8
up_thresh = 8
debounce = 50
angle = 0

# Signal handler (Ctrl+C)
def signal_handler(signal, frame):
    drive.stop()
    sys.exit()

# Retrieve previous x angles and average them
def get_angle():
    angle = mean( [compFilter() for i in range(debounce)] )

# Move chair based on angle
def move_chair():
    if angle > up_thresh:
        drive.forward()

    elif angle < down_thresh:
        drive.backward()

    else:
        drive.stop()

# Main
signal.signal(signal.SIGINT, signal_handler)
while True:
    print(get_angle())
    #move_chair()
