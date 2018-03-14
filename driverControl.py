forwardAngle = 5 #Angle to start going forward
backwardAngle = -5 #Angle to start going backward




drive = driver()
angle = angleDetection()

while True:
	currentAngle = angle.GetAngle()
	if currentAngle > forwardAngle:
		drive.backward()

	elif currentAngle < backwardAngle:
		drive.forward()

	else:
		drive.stop()

except:
	drive.stop()