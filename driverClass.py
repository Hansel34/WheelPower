import RPi.GPIO as GPIO			
from time import sleep	
AN2 = 13				# set pwm2 pin on MD10-Hat
AN1 = 12				# set pwm1 pin on MD10-hat
DIG2 = 24				# set dir2 pin on MD10-Hat
DIG1 = 26	
sleepTime = 1

class driver:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)			# GPIO numbering
		GPIO.setwarnings(False)			# enable warning from GPIO			# set dir1 pin on MD10-Hat
		GPIO.setup(AN2, GPIO.OUT)		# set pin as output
		GPIO.setup(AN1, GPIO.OUT)		# set pin as output
		GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
		GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
		self.p1 = GPIO.PWM(DIG1, 50)		# set pwm for M1
		self.p2 = GPIO.PWM(DIG2, 50)		# set pwm for M2
		GPIO.output(AN1,GPIO.LOW)
		GPIO.output(AN2,GPIO.LOW)
	
	def forward(self):
                
                GPIO.output(AN1, GPIO.HIGH)           # set AN1 as LOW, M1B will STOP
                GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP
                self.p1.start(60)                          
                self.p2.start(60)                         
                sleep(sleepTime)
	def backward(self):

                GPIO.output(AN1, GPIO.HIGH)           # set AN1 as LOW, M1B will STOP
                GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP
                self.p1.start(40)                          
                self.p2.start(40)                         
                sleep(sleepTime)


	def stop(self):
		GPIO.output(AN1, GPIO.LOW)           # set AN1 as LOW, M1B will STOP
		GPIO.output(AN2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
		self.p1.start(50)                          
		self.p2.start(50)                         
		sleep(sleepTime)
wheelchair = driver()
wheelchair.forward()
wheelchair.stop()
