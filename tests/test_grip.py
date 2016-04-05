#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)

pwm.setPWMFreq(60)                        # Set frequency to 60 
##GRIP TEST
##for k in range(-1000,1000,25):
##  print k
##  pwm.setPWM(15, 0, abs(k))
##  time.sleep(0.5)


for i in range(10):
  pwm.setPWM(15, 0, 350)
  time.sleep(0.5)
  pwm.setPWM(15, 0, 450)
  time.sleep(0.5)
