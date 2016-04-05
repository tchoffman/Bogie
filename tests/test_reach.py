#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

##REACH TEST
for j in range(0,1000,25):
  print j
  pwm.setPWM(13, 0, j)
  time.sleep(.5)
