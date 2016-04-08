#!/bin/bash

modprobe i2c-dev
modprobe i2c-bcm2708

# Get my directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python $DIR/bogie_legopi.py

# attempt to clean up
killall xboxdrv

