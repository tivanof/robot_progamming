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


# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)


robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)



TSensor = TouchSensor(Port.S1)


# start driving when pressing the button
speed = 100

while(1):
    if TSensor.pressed():
        ev3.speaker.beep()
        speed = 100
        for i in range(10):
            robot.drive(speed,0)
            speed += 50
            time.sleep(1)
        break
        

