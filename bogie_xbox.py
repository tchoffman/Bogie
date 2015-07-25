import XboxController
import time
import RPi.GPIO as gpio

WHEELS = {"LR": 7,
        "LF": 11,
        "RR": 13,
        "RF": 15}

def init():
    gpio.setmode(gpio.BOARD)
    for WHEEL in WHEELS:
        gpio.setup(WHEELS[WHEEL], gpio.OUT)
        gpio.output(WHEELS[WHEEL], gpio.LOW)

def drive(controlId, value):
    print "Control id = {}, Value = {}".format(controlId, value)
    if controlId == 1:
        if value >= 0.1:
            gpio.output(WHEELS["LR"],gpio.HIGH)
        if value <= -0.1:
            gpio.output(WHEELS["LF"],gpio.HIGH)
        if abs(value) < 0.1:
            gpio.output(WHEELS["LR"],gpio.LOW)
            gpio.output(WHEELS["LF"],gpio.LOW)
    if controlId == 4:
        value = 2 * (value - 0.5)
        if value >= 0.1:
            gpio.output(WHEELS["RR"],gpio.HIGH)
        if value <= -0.1:
            gpio.output(WHEELS["RF"],gpio.HIGH)
        if abs(value) < 0.1:
            gpio.output(WHEELS["RR"],gpio.LOW)
            gpio.output(WHEELS["RF"],gpio.LOW)
            
    if controlId == 12 and value == 1:
        xboxCont.stop()
        gpio.cleanup()
        
xboxCont = XboxController.XboxController(
    controllerCallBack = drive,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)

init()
xboxCont.start()
