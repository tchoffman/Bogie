#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

##ELBOW TEST
for j in range(150,600):
  print j
  pwm.setPWM(1, 0, j)
  time.sleep(.01)


