#!/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

pinIn  = "P9_33"
last   = -1
tDelay = 0.5

ADC.setup()

while True:
	# Conver 0.0 - 1.0 input to voltage
	curr = round(ADC.read(pinIn) * 1.8, 2)
	if curr <> last:
		last = curr
		print "Pin",pinIn,"=",curr,"volts"
	time.sleep(tDelay)
