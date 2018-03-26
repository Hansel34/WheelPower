#import thread
import signal
import sys
import numpy

<<<<<<< HEAD
from compFilterv2 import *
=======
from CompFilter import *
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26
from driverClass import *

# Initialize driver/sensor classes
drive = driver()
compFilter = CompFilter()

<<<<<<< HEAD
# Set up variables
flat_thresh = input("PLEASE ENTER ANGLE: ")
down_thresh = flat_thresh - 2
up_thresh = flat_thresh + 2
debounce = 50
ignoreAngles = 500
=======


# Set up variables
flat_thresh = input("pLEASE ENTER ANGLE: ")
down_thresh = flat_thresh + 2
up_thresh = flat_thresh - 2
debounce = 50
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26

# Signal handler (Ctrl+C)
def signal_handler(signal, frame):
	drive.stop()
	sys.exit()
<<<<<<< HEAD
# ignore first 10 angles
def ignore_angle():
        print("Please wait for initialization")
        for x in range(ignoreAngles):
                compFilter()
# Retrieve previous x angles and average them
def get_angle():
   # angle = numpy.mean( [compFilter() for i in range(debounce)] )
    tempAngle = 0
    for x in range(20):
        compFilter()
        tempAngle += compFilter.angle
    angle = tempAngle/20
    return angle
    
# Move chair based on angle
def move_chair(angle):
    print(angle)
    if angle > up_thresh:
        drive.forward()


    elif angle < down_thresh:
        #drive.backward()


    else:
        drive.stop()
 

# Main
signal.signal(signal.SIGINT, signal_handler)
ignore_angle()
=======

# Retrieve previous x angles and average them
def get_angle():
   # angle = numpy.mean( [compFilter() for i in range(debounce)] )
	tempAngle = 0
	for x in range(50):
		compFilter()
		tempAngle += compFilter.angle
	angle = tempAngle/50
	return angle
	
# Move chair based on angle
def move_chair(angle):
	print(angle)
	if abs(angle) > abs(up_thresh):
		drive.forward()
		print("Moving forward")

	elif abs(angle) < abs(down_thresh):
		#drive.backward()
		print("Moving backwards")

	else:
		drive.stop()
		print("Not assisting");

# Main
signal.signal(signal.SIGINT, signal_handler)
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26
while True:
	angle = get_angle()
	move_chair(angle)
