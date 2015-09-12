#!/bin/bash

# Make sure only root can run this script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

echo 0 > /sys/class/gpio/gpio44/value
echo 49 > /sys/class/gpio/unexport

