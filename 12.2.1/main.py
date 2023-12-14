#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import time
# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()


# print Helloworld
ev3.screen.print("Hello World")
