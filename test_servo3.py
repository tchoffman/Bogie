#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)

pwm.setPWMFreq(60)                        # Set frequency to 60 
##GRIP TEST
for l in range(5):
  print l
  pwm.setPWM(3, 0, 150)
  time.sleep(1)
  pwm.setPWM(3, 0, 800)
  time.sleep(1)
  

