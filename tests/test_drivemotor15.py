#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)

pwm.setPWMFreq(60)                        # Set frequency to 60 
##Drive TEST
for pulse_width in range(4096):
  print pulse_width
  pwm.setPWM(0, 0, pulse_width)
  pwm.setPWM(2, 0, pulse_width)
  time.sleep(.001)
  
time.sleep(1)
pwm.setPWM(0,0,0) 
pwm.setPWM(2,0,0)

for pulse_width in range(4096):
  print pulse_width
  pwm.setPWM(1, 0, pulse_width)
  pwm.setPWM(3, 0, pulse_width)
  time.sleep(.001)

time.sleep(1)
pwm.setPWM(1,0,0)
pwm.setPWM(3,0,0)
