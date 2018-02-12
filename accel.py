# Import modules
import time
import math

### Import data gathering modules
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.ion()

# Import the LSM303 module.
import Adafruit_LSM303

class Accelerometer():
    
    def create_plot(h1):
        # Set up plot
        h1.figure, h1.ax = plt.subplots()
        h1.lines, = h1.ax.plot([], [], 'o')

        # Configure plot
##        h1.ax.set_autoscalex_on(True)
        h1.ax.set_ylim(0, 180)
        h1.ax.set_xlim(0, 120)

        h1.ax.grid()

    def update_line(h1, x_data, y_data):
        # Update Data
        h1.lines.set_xdata(x_data)
        h1.lines.set_ydata(y_data)

        # Rescale, draw and flush
        h1.figure.canvas.draw()
        h1.figure.canvas.flush_events()

    def __call__(h1):
        # Create an LSM303 instance.
        lsm303 = Adafruit_LSM303.LSM303()

        # Initialize values to hold previous low pass filter values
        f_accel_x = 0.0
        f_accel_y = 0.0
        f_accel_z = 0.0

        alpha = 0.5
        start_time = time.time()

        # Create plot
        h1.create_plot()

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
            elapsed_time = time.time() - start_time
            Accelerometer.update_line(h1, elapsed_time, pitch)
        ##    print('Pitch = {0}'.format(pitch))

a = Accelerometer()
a()
            
