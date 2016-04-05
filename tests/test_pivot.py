#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
## PIVOT TEST
for i in range(0,800,25):
  # Change speed of continuous servo on channel O
  print i
  pwm.setPWM(12, 0, i)
  time.sleep(.5)
