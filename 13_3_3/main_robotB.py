#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#import library
from umqtt.robust import MQTTClient
import time

#callback for listen to topics
def listen(topic,msg):
    global vqr
    if topic == MQTT_Topic_tune.encode():
        if((str(msg.decode())) == 'A'):
            ev3.speaker.play_notes(['A4/4'])
        elif((str(msg.decode())) == 'B'):
            ev3.speaker.play_notes(['B4/4'])

ev3 = EV3Brick()

ev3.screen.print('test1')
time.sleep(1)

#MQTT setup
MQTT_ClientID = 'travispastrana'
MQTT_Broker = '192.168.137.1'
MQTT_Topic_tune = 'Tune'

client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

ev3.screen.print('test2')
time.sleep(1)


# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print('test3')
time.sleep(1)
ev3.screen.print('Started')
time.sleep(1)
client.set_callback(listen)


client.subscribe(MQTT_Topic_tune)
time.sleep(0.5)

ev3.screen.print('Listening')
time.sleep(1)

while True:
    client.check_msg()
    time.sleep(0.5)