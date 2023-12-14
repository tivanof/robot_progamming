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

# Write your program here.
ev3.speaker.beep()
# ev3.screen.print(CSensor.color())
CSensor = ColorSensor(Port.S4)
ev3.screen.print(CSensor.color())

array= []

while True:
    robot.drive(100,0)
    if (CSensor.color() == Color.BLACK):
        count_black +=1
        ev3.screen.print("Black = ",count_black)
        ev3.screen.print("Red = ",count_red)
        ev3.screen.print("Blue = ",count_blue)
        time.sleep(0.2)

    if (CSensor.color() == Color.BLUE):
        count_blue +=1
        ev3.screen.print("Black = ",count_black)
        ev3.screen.print("Red = ",count_red)
        ev3.screen.print("Blue = ",count_blue)
        time.sleep(0.2)

    if (CSensor.color() == Color.RED):
        count_red +=1
        ev3.screen.print("Black = ",count_black)
        ev3.screen.print("Red = ",count_red)
        ev3.screen.print("Blue = ",count_blue)
        time.sleep(0.2)