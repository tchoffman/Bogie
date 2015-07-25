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

xboxCont = XboxController.XboxController(
    controllerCallBack = drive,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)

init()
xboxCont.start()
time.sleep(15)
gpio.cleanup()
xboxCont.stop()
