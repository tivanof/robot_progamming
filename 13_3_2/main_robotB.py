#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()


#import library
from umqtt.robust import MQTTClient
import time


#callback for listen to topics
def listen(topic,msg):
    if topic == MQTT_Topic_remote.encode():
        direction =str(msg.decode())
        
        wait(1000)
        robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
        
        if (direction == "UP"):
            robot.straight(300)
        elif (direction == "DOWN"):
            robot.straight(-300)
        elif (direction == "RIGHT"):
            robot.turn(90)
        elif (direction == "LEFT"):
            robot.turn(-90)


ev3 = EV3Brick()

ev3.screen.print('test1')
time.sleep(1)

#MQTT setup
MQTT_ClientID = 'travispastrana'
MQTT_Broker = '192.168.137.1'
MQTT_Topic_remote = 'Remote'
MQTT_Topic_distance = 'Distance'
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
ev3.screen.print('Listening')
time.sleep(1)



client.set_callback(listen)

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
ultrasonic_sensor = UltrasonicSensor(Port.S3)

# Set the target distance from an obstacle (in millimeters)
target_distance = 200  # 20cm = 200mm

# Start the motor to move the robot forward
#left_motor.dc(50)  
#right_motor.dc(50)


#while ultrasonic_sensor.distance() > target_distance:
#    wait(10)  
#motor.stop()


while True:
    
    client.check_msg()
    dist = ultrasonic_sensor.distance()
    
    client.publish(MQTT_Topic_distance,str(dist))
    time.sleep(0.5)
    
    
