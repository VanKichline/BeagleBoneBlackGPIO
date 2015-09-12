#!/bin/bash

# Make sure only root can run this script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

echo 49 > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio49/direction
COUNTER=0
while [ $COUNTER -lt 10000 ]; do
	echo 0 > /sys/class/gpio/gpio49/value
	echo 1 > /sys/class/gpio/gpio49/value
	let COUNTER=COUNTER+1
done
echo 49 > /sys/class/gpio/unexport

