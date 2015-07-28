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
    
def monitor():
    command = ""
    if xboxCont.controlValues[1] < -0.1:
        command += "FORWARD, "
    if xboxCont.controlValues[1] > 0.1:
        command += "BACKWARD, "
    if xboxCont.controlValues[0] < -0.1:
        command += "LEFT, "
    if xboxCont.controlValues[0] > 0.1:
        command += "RIGHT, "
    if xboxCont.controlValues[12] == 1:
        print "STOPPING"
        xboxCont.stop()
        gpio.cleanup
        return False
    print command
    return True
    
xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)

init()
xboxCont.start()
run = True
while run == True:
    run = monitor()
