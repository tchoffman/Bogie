# Bogie
Bogie Rover code for Raspberry Pi

## Setup PWM Servo Hat

### Install smbus
sudo apt-get install python-smbus

### Install I2C Tools 
sudo apt-get install i2c-tools

### Detect I2C channels
After connect Servo Hat run:
sudo i2cdetect -y 1

## Setup Xbox Controller

### Install xboxdrv
sudo apt-get install xboxdrv

### Run xboxdrv
from root run:
sudo xboxdrv --detach-kernel-driver



