#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


vqr = None


#import library
from umqtt.robust import MQTTClient
import time

#callback for listen to topics
def listen(topic,msg):
    global vqr
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))
        vqr = str(msg.decode())
    elif topic == MQTT_Topic_msg.encode():
        ev3.screen.print(str(msg.decode()))
        
        robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
        robot.straight(300)

ev3 = EV3Brick()

ev3.screen.print('test1')
time.sleep(1)

#MQTT setup
MQTT_ClientID = 'ev3dev'
MQTT_Broker = '192.168.137.1'
MQTT_Topic_remote = 'Remote'
MQTT_Topic_distance= 'Distance'

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


client.subscribe(MQTT_Topic_remote)
client.subscribe(MQTT_Topic_distance)
time.sleep(0.5)

client.publish(MQTT_Topic_Status, 'Robot A: Listening')
ev3.screen.print('Listening')
time.sleep(1)

#New topic and publish the hello world
MQTT_Topic_msg = "Lego/msg"
client.subscribe(MQTT_Topic_msg)

client.set_callback(listen)

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
ultrasonic_sensor = UltrasonicSensor(Port.S3)





while True:
        # try:
    #     if(ev3.buttons.pressed()[0] == Button.CENTER):
    #         ev3.screen.print("Center")
    # except:
    client.publish(MQTT_Topic_remote ,ev3.buttons.pressed())
    #global vqr
    client.check_msg()
    time.sleep(0.5)


