#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

##WRIST TEST
for k in range(150,600):
  print k
  pwm.setPWM(2, 0, k)
  time.sleep(.01)
  

