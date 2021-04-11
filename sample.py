import utime
from machine import I2C, Pin
import MPU6050

# start timer
start = utime.ticks_ms()

def get(mpu):
    global start
    data = []

    try:
        motion = mpu.read()
        # IMPORTANT - this readout is a value in m/s^2
        # use mpu.read_g() if the acceleration in terms of g is desired
        # this would be slightly faster     
        
        dt = utime.ticks_diff(utime.ticks_ms(), start)

        # preallocating speeds up code if data is used as a global
        data[0] = dt
        data[1] = motion.Temperature
        data[2] = motion.Gx
        data[3] = motion.Gy
        data[4] = motion.Gz
        data[5] = motion.Gyrox
        data[6] = motion.Gyroy
        data[7] = motion.Gyroz
               
    except:
        data = [float('nan')]*9
        print("Failed to get data")
    
    #print("Data updated")
    return data


# initialise MPU6050 and LED
# these pins work on a Pi Pico - check the pinout for the board you use
mpu = MPU6050.MPU6050(bus = 0, scl = Pin(17), sda = Pin(16))
led = Pin(25, Pin.OUT)

# set the range of the accelerometer
# options are 2, 4, 8, 16 (+/-)
mpu.set_accel_range(16)

# set the range of the gyroscope
# options are 250, 500, 1000, 2000
mpu.set_gyro_range(500)

while True:
    data = get(mpu)
    print(data)
    utime.sleep(2)
    led.toggle()
