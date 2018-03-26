# Import modules
import time
import math

# Import the LSM303 accelerometer.
import Adafruit_LSM303

# Import the L3GD20 gyroscope
import L3GD20

class CompFilter():
        
    def __init__(self):
        # Create an LSM303 instance.
        self.lsm303 = Adafruit_LSM303.LSM303()

        # Create and configure an L3GD20 instance.
        self.l3gd20 = L3GD20.L3GD20(busId = 1, slaveAddr = 0x6b,
                            ifLog = False, ifWriteBlock = False)

        self.use_gyro = True
        self.l3gd20.Set_PowerMode("Normal")
        self.l3gd20.Set_FullScale_Value("250dps")
        self.l3gd20.Set_AxisY_Enabled(True)

        # Initialize and Calibrate gyroscope
        self.l3gd20.Init()

        self.gyro_dt = 0.004

        # Initialize Complimentary Filter variables
        self.comp_alpha = 0.98
        self.angle = 0

    def __call__(self):
        # Read the X, Y, Z axis acceleration values
        accel, mag = self.lsm303.read()
                    
        # Grab the X, Y, Z components from the reading and print them out.
        accel_x, accel_y, accel_z = accel

        # Calculate pitch from accelerometer
        self.pitch = (math.atan2(accel_x, math.sqrt(accel_y*accel_y +
                accel_z*accel_z)) * 180.0/math.pi)

        # Sleep to maintain constant gyro rate of change
        time.sleep(self.gyro_dt)

        # Read gyro values
        dy = self.l3gd20.Get_CalOut_Value()

        # Calculate final angle using complimentary filter
        self.angle = (self.comp_alpha * (self.angle + dy[1] * self.gyro_dt)
                      + ((1-self.comp_alpha) * self.pitch))

        # Print for debugging
        #print('Pitch = {0}, Gyro = {1} Angle = {2}'.format(self.pitch, dy[1] * self.gyro_dt, self.angle))
