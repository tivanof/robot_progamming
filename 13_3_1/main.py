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
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))

ev3 = EV3Brick()

ev3.screen.print('test1')
time.sleep(1)
#MQTT setup
MQTT_ClientID = 'ev3dev'
MQTT_Broker = '192.168.137.1'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

ev3.screen.print('test2')
time.sleep(1)


# Write your program here.
client.connect()
time.sleep(0.5)
ev3.screen.print('test3')
time.sleep(1)
client.publish(MQTT_Topic_Status, 'Started')
ev3.screen.print('Started')
time.sleep(1)
client.set_callback(listen)
time.sleep(1)


client.subscribe(MQTT_Topic_Status)
time.sleep(0.5)
client.publish(MQTT_Topic_Status, 'Listening')
ev3.screen.print('Listening')
while True:
    client.check_msg()
    time.sleep(0.5)




# Write your program here.
ev3.speaker.beep()
