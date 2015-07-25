import bogie
import time
import RPi.GPIO as GPIO

##wobble(.75)
##time.sleep(1)
bogie.forward(1.25)
time.sleep(.5)
bogie.backward(1.25)
time.sleep(.5)
##circle_cw(3)
##time.sleep(.5)
##circle_ccw(3)
##time.sleep(.5)
##wobble(.75)
##turn_r(3)
##time.sleep(1)
##turn_l(3)

GPIO.cleanup()
