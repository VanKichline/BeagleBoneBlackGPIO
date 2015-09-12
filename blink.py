#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

pinOut = "P9_23"
tDelay = 0.1

GPIO.setup(pinOut, GPIO.OUT)
while True:
	GPIO.output(pinOut, GPIO.HIGH)
	time.sleep(tDelay)
	GPIO.output(pinOut, GPIO.LOW)
	time.sleep(tDelay)

