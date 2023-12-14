#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# Create your objects here.
ev3 = EV3Brick()



# Initialize a motor at port B.
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)




robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# drive a square

for i in range(4) :
    robot.straight(360)
    robot.turn(90)
    

# drive an 8

robot.drive(250,80)
time.sleep(4.6)
robot.drive(250,-80)
time.sleep(4.6)
    

# Change of direction
robot.drive(1000,0)
time.sleep(3)
robot.drive(0,0)
time.sleep(2)
ev3.speaker.beep()
robot.drive(-200,0)
time.sleep(5)


# gradual acceleration
speed = 100

for i in range(10):
    robot.drive(speed,0)
    speed += 50
    time.sleep(1)



