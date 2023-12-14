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

TSensor = TouchSensor(Port.S1)

timeout = time.time() +5   # 5 sec from now
count =0
while True:
    if TSensor.pressed():
        count += 1
        time.sleep(0.1)
    if time.time() > timeout:
        break
    time.sleep(0.1)
ev3.screen.print(count)

for i in range(count):
    ev3.speaker.beep(frequency=100+(100*i), duration=300)
    time.sleep(0.2)
