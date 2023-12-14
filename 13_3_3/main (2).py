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
    if topic == MQTT_topic_distance.encode():
        ev3.screen.print(str(msg.decode()))
        vqr = str(msg.decode())
    

ev3 = EV3Brick()

ev3.screen.print('test1')
time.sleep(1)

#MQTT setup
MQTT_ClientID = 'group2'
MQTT_Broker = '192.168.137.1'
MQTT_topic_distance = 'Tune'

client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

ev3.speaker.play_notes(['E4/4'])
    
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


client.subscribe(MQTT_topic_distance)

time.sleep(0.5)

ev3.screen.print('Listening')
time.sleep(1)




while True:
    
    
    client.check_msg()
    ev3.speaker.play_notes(['E4/4'])
    wait(100)
    client.publish(MQTT_topic_distance,"A")
    wait(100)
    client.publish(MQTT_topic_distance,"B")
    wait(100)
    client.publish(MQTT_topic_distance,"C")
    wait(100)
    client.publish(MQTT_topic_distance,"B")
    wait(100)
    client.publish(MQTT_topic_distance,"D")
    wait(100)
    ev3.speaker.play_notes(['E4/4'])
    wait(100)
    client.publish(MQTT_topic_distance,"C")
    wait(100)
    client.publish(MQTT_topic_distance,"A")
    wait(100)
    client.publish(MQTT_topic_distance,"B")
    wait(0.5)
    client.publish(MQTT_topic_distance,"C")
    wait(0.5)
    client.publish(MQTT_topic_distance,"B")
    wait(0.5)
    ev3.speaker.play_notes(['E4/4'])
    time.sleep(0.5)