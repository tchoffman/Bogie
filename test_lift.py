#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

##LIFT TEST
for k in range(0,1000,25):
  print k
  pwm.setPWM(14, 0, k)
  time.sleep(.5)

pwm.setPWM(14, 0, 500)  

