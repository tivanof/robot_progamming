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

array = [" "," "]
index = 0
reverse_index=1

#callback for listen to topics
def listen(topic,msg):
    global index, array,reverse_index, ev3

    if topic == MQTT_Topic_border.encode():
        if str(msg.decode()) == 'right':
            if array[reverse_index]!= 'right':
                array[index] = "right"
                if index ==1:
                    index = 0
                    reverse_index = 1
                    ev3.screen.print("Intruder detected, \n moving from\n",array[0],"to",array[1])
                else: 
                    index = 1
                    reverse_index = 0


        elif str(msg.decode()) == 'left':
            if array[reverse_index]!= 'left' :
                array[index] = "left"
                if index ==1:
                    index = 0
                    reverse_index = 1
                    ev3.screen.print("Intruder detected, \n moving from\n",array[0],"to",array[1])
                else: 
                    index = 1
                    reverse_index = 0


ev3 = EV3Brick()

ev3.screen.print('test1')
time.sleep(1)

#MQTT setup
MQTT_ClientID = 'ev3dev'
MQTT_Broker = '192.168.137.1'
MQTT_Topic_border = 'border'

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
time.sleep(1)


client.subscribe(MQTT_Topic_border)
time.sleep(0.5)

ev3.screen.print('Listening')
time.sleep(1)


while True:
    client.check_msg()
    time.sleep(0.5)