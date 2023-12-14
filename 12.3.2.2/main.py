#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


ev3 = EV3Brick()
UltraSensor= UltrasonicSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)


while True :
    left_motor.run(360)
    right_motor.run(360)
    time.sleep(0.5)
    if(UltraSensor.distance()<200):
        right_motor.stop()
        #time.sleep(0.5)
        left_motor.run(-360)
        time.sleep(0.5)
        #left_motor.stop()
    








    







