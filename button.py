#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

pinIn = "P9_27"
tDelay = 0.1
last = -1

GPIO.setup(pinIn, GPIO.IN)
while True:
	current = GPIO.input(pinIn)
	if current <> last:
		last = current
		if 1 == current:
			print "The button is pressed"
		else:
			print "The button is released"
	time.sleep(tDelay)

