drive = driver()
angle = angleDetection()

while True:
	currentAngle = angle.GetAngle()
	if currentAngle > 5:
		drive.backward()

	elif currentAngle < -5:
		drive.forward()

	else:
		drive.stop()

except:
	drive.stop()