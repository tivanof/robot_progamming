#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

CSensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
dist = 1


ev3.speaker.beep()

# while True:

#     if CSensor.color() == Color.RED:
#         break

#     elif CSensor.color() == Color.BLACK:
#         robot.drive(100, 0)

#     elif CSensor.color() == Color.BLUE:
#         robot.drive(60, 0)

#     else:
#         robot.turn(10)
#         if CSensor.color() != Color.BLACK:
#             robot.turn(-10)

BLACK = Color.BLACK
RED = Color.RED
LINE_FOLLOW_SPEED = 100
LINE_TURN_SPEED = 60
LINE_TURN_ANGLE = 15

def follow_line(speed=LINE_FOLLOW_SPEED):
    robot.drive(speed, 0)
    ev3.screen.print(CSensor.color())

def turn_left():
    robot.turn(LINE_TURN_ANGLE)
    ev3.screen.print(CSensor.color())


def turn_right():
    robot.turn(-LINE_TURN_ANGLE)
    ev3.screen.print(CSensor.color())


while CSensor.color() != RED:
    if CSensor.color() == BLACK:
        follow_line()

    else:
        # Adjust the turn speed and direction as needed
        if CSensor.color() == Color.BLUE:
            robot.drive(LINE_TURN_SPEED, 0)
        else:
            turn_left()
            if CSensor.color() != BLACK:
                turn_right()
        


