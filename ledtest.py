import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.output(8,1)
sleep(5)
GPIO.output(8,0)
GPIO.output(7,1)
sleep(3)
GPIO.output(7,0)
GPIO.output(4,1)
sleep(3)
GPIO.output(4,0)
GPIO.output(3,1)
sleep(3)
GPIO.output(3,0)
GPIO.output(2,1)
sleep(3)
GPIO.output(2,0)
GPIO.output(11,1)
sleep(3)
GPIO.output(11,0)

GPIO.cleanup()
