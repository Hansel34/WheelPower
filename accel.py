# Import modules
import time
import math

# Import the LSM303 module.
import Adafruit_LSM303


# Create an LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Initialize values to hold previous low pass filter values
f_accel_x = 0.0
f_accel_y = 0.0
f_accel_z = 0.0

alpha = 0.5

while True:
    # Read the X, Y, Z axis acceleration values
    accel, mag_unused = lsm303.read()
    
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    
    # Run values through a low pass filter
    f_accel_x = accel_x + (f_accel_x * (1.0 - alpha))
    f_accel_y = accel_y + (f_accel_y * (1.0 - alpha))
    f_accel_z = accel_z + (f_accel_z * (1.0 - alpha))

    pitch = math.atan2(f_accel_x, math.sqrt(f_accel_y*f_accel_y + f_accel_z*f_accel_z)) * 180.0/math.pi
    print('Pitch = {0}'.format(pitch))
    
    #time.sleep(0.05)
