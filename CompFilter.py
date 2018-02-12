# Import modules
import time
import math

# Import the LSM303 accelerometer.
import Adafruit_LSM303

# Import the L3GD20 gyroscope
import L3GD20

class CompFilter():
        
    def __init__(self, use_gyro):
        # Create an LSM303 instance.
        self.lsm303 = Adafruit_LSM303.LSM303()

        # Initialize values to hold low pass filter
        # values for accelerometer
        self.f_accel_x = 0.0
        self.f_accel_y = 0.0
        self.f_accel_z = 0.0
        self.alpha = 0.5

        # Create and configure an L3GD20 instance.
        if use_gyro:
            self.l3gd20 = L3GD20.L3GD20(busId = 1, slaveAddr = 0x6b,
                            ifLog = false, ifWriteBlock = False)

            self.use_gyro = True
            self.l3gd20.Set_PoweR_Mode("Normal")
            self.l3gd20.Set_FullScale_Value("250dps")
            self.l3gd20.Set_AxisX_Enabled(True)
            self.l3gd20.Set_AxisY_Enabled(True)
            self.l3gd20.Set_AxisZ_Enabled(True)

            # Initialize and Calibrate gyroscope
            self.l3gd20.Init()
            self.l3gd20.Calibrate()
            self.gyro_dt = 0.02
            self.gyro_x = 0
            self.gyro_y = 0
            self.gyro_z = 0

    def __call__(self):
        # Read the X, Y, Z axis acceleration values
        accel, mag = self.lsm303.read()
                    
        # Grab the X, Y, Z components from the reading and print them out.
        accel_x, accel_y, accel_z = accel
                 
        # Run values through a low pass filter
        self.f_accel_x = accel_x + (self.f_accel_x * (1.0 - self.alpha))
        self.f_accel_y = accel_y + (self.f_accel_y * (1.0 - self.alpha))
        self.f_accel_z = accel_z + (self.f_accel_z * (1.0 - self.alpha))

        pitch = (math.atan2(self.f_accel_x, math.sqrt(self.f_accel_y*self.f_accel_y +
                self.f_accel_z*self.f_accel_z)) * 180.0/math.pi)
        print('Pitch = {0}'.format(pitch))

c = CompFilter(False)
while True:
    c()
