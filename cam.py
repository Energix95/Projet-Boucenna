import cv2
import serial
import time
from Maestro import maestro

from cv2 import VideoCapture

servo = maestro.Controller()
servo.setAccel(0,50)      #set servo 0 acceleration to 4
servo.setTarget(0,6000)  #set servo to move to center position
time.sleep(1)
servo.setAccel(0,50)
servo.setTarget(0,1000)
#servo.setSpeed(0,50)     #set speed of servo 1
#x = servo.getPosition(1) #get the current position of servo 1
servo.close()
#ça va?
