#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
servoPos = 0
##SHOULDER TEST
for i in range(150,600):
  # Change speed of continuous servo on channel O
  print i
  pwm.setPWM(0, 0, i)
  time.sleep(.01)
##ELBOW TEST
for j in range(150,600):
  print j
  pwm.setPWM(1, 0, j)
  time.sleep(.01)
##WRIST TEST
for k in range(150,600):
  print k
  pwm.setPWM(2, 0, k)
  time.sleep(.01)
##GRIP TEST
for l in range(5):
  pwm.setPWM(3, 0, 150)
  time.sleep(1)
  pwm.setPWM(3, 0, 800)
  time.sleep(1)
  

