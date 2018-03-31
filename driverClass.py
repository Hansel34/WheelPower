import RPi.GPIO as GPIO			
from time import sleep	
AN2 = 13				# set pwm2 pin on MD10-Hat
DIG2 = 24				# set dir2 pin on MD10-Hat	
sleepTime = 1

class driver:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)			# GPIO numbering
		GPIO.setwarnings(False)			# enable warning from GPIO			# set dir1 pin on MD10-Hat
		GPIO.setup(AN2, GPIO.OUT)		# set pin as output
		GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
		self.p2 = GPIO.PWM(DIG2, 50)		# set pwm for M2
		self.speedSetting = 0
		GPIO.output(AN2,GPIO.LOW)
	
	def forward(self):
                GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP
                if self.speedSetting <= 10:
                        self.speedSetting +=1                      
                self.p2.start(60+self.speedSetting)                         
                sleep(sleepTime)
	def backward(self):
                GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP                       
                self.p2.start(40)                         
                sleep(sleepTime)

	def stop(self):
		GPIO.output(AN2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
		self.speedSetting=0                         
		self.p2.start(50)                         
		sleep(sleepTime)

