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

        # Initialize values to hold low pass filter
        # values for accelerometer
        self.f_accel_x = 0.0
        self.f_accel_y = 0.0
        self.f_accel_z = 0.0
<<<<<<< HEAD
=======
        self.acc_alpha = 0.02
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26

        # Create and configure an L3GD20 instance.
        self.l3gd20 = L3GD20.L3GD20(busId = 1, slaveAddr = 0x6b,
                            ifLog = False, ifWriteBlock = False)

        self.use_gyro = True
        self.l3gd20.Set_PowerMode("Normal")
        self.l3gd20.Set_FullScale_Value("250dps")
        self.l3gd20.Set_AxisY_Enabled(True)

        # Initialize and Calibrate gyroscope
        self.l3gd20.Init()
<<<<<<< HEAD
        self.gyro_dt = 0.004
=======
        self.gyro_alpha = 0.9
        self.gyro_dt = 0.02
        self.gyro_y = 0
        self.f_gyro_y = 0
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26

        # Initialize Complimentary Filter variables
        self.comp_alpha = 0.98
        self.angle = 0

    def __call__(self):
        # Read the X, Y, Z axis acceleration values
        accel, mag = self.lsm303.read()
                    
        # Grab the X, Y, Z components from the reading and print them out.
        accel_x, accel_y, accel_z = accel
<<<<<<< HEAD

        # Calculate pitch from accelerometer
        self.pitch = (math.atan2(accel_x, math.sqrt(accel_y*accel_y +
                accel_z*accel_z)) * 180.0/math.pi)
=======
                 
        # Run values through a low pass filter
        #self.f_accel_x = self.f_accel_x + self.acc_alpha * (accel_x - self.f_accel_x)
        #self.f_accel_y = self.f_accel_y + self.acc_alpha * (accel_y - self.f_accel_y)
        #self.f_accel_z = self.f_accel_z + self.acc_alpha * (accel_z - self.f_accel_z)

        # Calculate pitch from accelerometer
        self.pitch = (math.atan2(self.accel_x, math.sqrt(self.accel_y*self.accel_y +
                self.accel_z*self.accel_z)) * 180.0/math.pi)
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26

        # Sleep to maintain constant gyro rate of change
        time.sleep(self.gyro_dt)

        # Read gyro values
        dy = self.l3gd20.Get_CalOut_Value()
<<<<<<< HEAD
=======
        #old_gyro_y = self.gyro_y
        #self.gyro_y += dy[1]*self.gyro_dt

        # Run values through a high pass filter
        #self.f_gyro_y = (self.gyro_alpha) * (self.f_gyro_y + self.gyro_y - old_gyro_y)
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26

        # Calculate final angle using complimentary filter
        self.angle = (self.comp_alpha * (self.angle + dy[1] * self.gyro_dt)
                      + ((1-self.comp_alpha) * self.pitch))

        # Print for debugging
<<<<<<< HEAD
        #print('Pitch = {0}, Gyro = {1} Angle = {2}'.format(self.pitch, dy[1] * self.gyro_dt, self.angle))
=======
        print('Pitch = {0}, Gyro = {1} Angle = {2}'.format(self.pitch, self.f_gyro_y, self.angle))
>>>>>>> 7b698ebdd7ab8dbc6bfbdc7d315868df092ccd26
