import RPi.GPIO as GPIO			
from time import sleep	

class driver:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)			# GPIO numbering
		GPIO.setwarnings(False)			# enable warning from GPIO
		self.AN2 = 13				# set pwm2 pin on MD10-Hat
		self.AN1 = 12				# set pwm1 pin on MD10-hat
		self.DIG2 = 24				# set dir2 pin on MD10-Hat
		self.DIG1 = 26				# set dir1 pin on MD10-Hat
		GPIO.setup(AN2, GPIO.OUT)		# set pin as output
		GPIO.setup(AN1, GPIO.OUT)		# set pin as output
		GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
		GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
		sleep(1)				# delay for 1 seconds
		self.p1 = GPIO.PWM(DIG1, 100)		# set pwm for M1
		self.p2 = GPIO.PWM(DIG2, 100)		# set pwm for M2
	
	def forward(self):
	   GPIO.output(AN1, GPIO.HIGH)           # set AN1 as LOW, M1B will STOP
	   GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP
	   p1.start(60)                          
	   p2.start(60)                         
	   sleep(1)    

	def backward(self):
	   GPIO.output(AN1, GPIO.HIGH)           # set AN1 as LOW, M1B will STOP
	   GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP
	   p1.start(40)                          
	   p2.start(40)                         
	   sleep(1)    


	def stop(self):
		GPIO.output(AN1, GPIO.LOW)           # set AN1 as LOW, M1B will STOP
		GPIO.output(AN2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
		p1.start(0)                          
		p2.start(0)                         
		sleep(1)  