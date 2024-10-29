# Bogie Runt Rover with MeArm
The "Bogie" is a robot built on the Bogie Runt Rover chassis from Actorobotics.  In this project I also mounted a small MeArm (laser cut from wood) onto the top of the rover.  The chassis comes with 6 motors and in this case they are controlled as 2 tracks (left and right).  The MeArm has 4 axes of rotation controlled by 4 small servo motors via a RPi "Servo Hat".  The brains of the Robot is a Raspberry Pi 2.  Tracks and servos are controlled via pulse width modulation (PWM) which is converted into constant voltages by the PWM Servo Hat to control velocity of each track. All motors, servos and electronics are powered by a single power source, which requires the use of a "buck controller" to regulate voltage to the RPi and servos. A small Xbox control receiver was modified to mount on the Bogie Rover and drivers were installed on the RPi.  Python scripts control the conversion of signals from the Xbox controller to the motors and servos.  In a simple rover, each joystick would control each track, but the existence of the MeArm required a mapping of the Left Joystick to control both tracks simultaneously with "intuitive" control.  For instance, Leftward pressure will result in ta left turn (L track full reverse, R track full forward).  Meanwhile, the right stick and triggers are used to control the 4 axes of the MeArm.

![Screenshot 2024-10-29 at 1 00 03 PM](https://github.com/user-attachments/assets/f290fe57-34d2-4836-889f-dbb5e5a1a074)


## See it in action here:
https://youtu.be/1KNCQ7p-Euc

## Setup PWM Servo Hat

### Install smbus
sudo apt-get install python-smbus

### Install I2C Tools 
sudo apt-get install i2c-tools

### Enable I2C
sudo raspi-config
Enable I2C support and Reboot

### Detect I2C channels
After connect Servo Hat run:
sudo i2cdetect -y 1

## Setup Xbox Controller

### Install xboxdrv
sudo apt-get install xboxdrv

### Run xboxdrv
from root run:
sudo xboxdrv --detach-kernel-driver
Must run this before running script or script can't claim USB


