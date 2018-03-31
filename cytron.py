import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 13				# set pwm2 pin on MD10-Hat
DIG2 = 24				# set dir2 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
sleep(1)				# delay for 1 seconds
p2 = GPIO.PWM(DIG2, 100)		# set pwm for M2

speed = int(input())

if (speed > 50) :

  try:					
    while True:

     print "STOP"			# display "Forward" when programe run
     GPIO.output(AN2, GPIO.LOW)		# set AN2 as HIGH, M2B will turn ON
     p2.start(0)				# set Direction for M2  
     sleep(1)				#delay for 2 second
                           

     print "GO"
     GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP                       
     p2.start(speed)                         
     sleep(1)                             #delay for 3 second

     GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP                        
     p2.start(speed)                         
     sleep(1)

     print "at full speed"
     GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP                         
     p2.start(speed)                         
     sleep(100)    

  except:					# exit programe when keyboard interupt
     p2.start(50)				# set speed to 0
     GPIO.output(AN2, GPIO.LOW)  
                                          # Control+X to save and exit
else:

  try:					
    while True:

     print "STOP"			# display "Forward" when programe run
     GPIO.output(AN2, GPIO.LOW)		# set AN2 as HIGH, M2B will turn ON
     p2.start(0)				# set Direction for M2  
     sleep(1)				#delay for 2 second
                           

     print "GO"
     GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP                          
     p2.start(speed)                         
     sleep(1)                             #delay for 3 second

     GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP                       
     p2.start(speed)                         
     sleep(1)

     GPIO.output(AN2, GPIO.HIGH)           # set AN2 as HIGH, M2B will STOP                         
     p2.start(speed)                         
     sleep(100)    

  except:					# exit programe when keyboard interupt
     p2.start(50)				# set speed to 0
     GPIO.output(AN2, GPIO.LOW)  
                                          # Control+X to save and exit
