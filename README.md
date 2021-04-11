# mpu6050-mpy
A light micropython library for the MPU6050 6-DOF IMU, based off https://github.com/larsks/py-mpu6050. Superflous code has been removed, and accelerometer and gyroscope range setting functions have been rewritten to make them easier to use. Some of the functions have also been made private.

## Compiling
This library can be compiled using mpy-cross. Flags -O[4] and -march=armv7m have worked well for me when used with a Pi Pico. Compiling decreases the size of the library significantly, from about 14 KB to about 8 KB. 

Tested and works on a Pi Pico. Have a look at the sample code to see the implementation. 
