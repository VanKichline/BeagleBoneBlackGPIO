#!/usr/bin/python

import Adafruit_BBIO.PWM as PWM
import time
import os
import sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

pinOut = "P8_13"
tDelay = 0.1

PWM.start(pinOut, 0)

for i in range(0, 100):
	PWM.set_duty_cycle(pinOut, float(i))
	time.sleep(tDelay)

PWM.stop(pinOut)
PWM.cleanup()

