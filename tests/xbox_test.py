import XboxController
import time
import math
import RPi.GPIO as gpio


WHEELS = {"LR": 7, "LF": 11, "RR": 13, "RF": 15}

def init():
    gpio.setmode(gpio.BOARD)
    for WHEEL in WHEELS:
        gpio.setup(WHEELS[WHEEL], gpio.OUT)
        gpio.output(WHEELS[WHEEL], gpio.LOW)

def drive(controlId, value):
    print "Control id = {}, Value = {}".format(controlId, value)
    
def monitor1():
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

def monitor2():
    x_axis = xboxCont.controlValues[0]
    y_axis = -1 * xboxCont.controlValues[1]
    rotation = -math.pi/4
    x_prime = (x_axis * math.cos(rotation)) - (y_axis * math.sin(rotation))
    y_prime = (x_axis * math.sin(rotation)) + (y_axis * math.cos(rotation))
    command = "Y: ", y_prime, " X: ", x_prime
    if xboxCont.controlValues[12] == 1:
        print "STOPPING"
        xboxCont.stop()
        gpio.cleanup
        return False
    
    print command
    return True

def monitor3():
    fb_axis = xboxCont.controlValues[0]
    lr_axis = -1 * xboxCont.controlValues[1]
    angle = math.degrees(math.atan2(fb_axis, lr_axis))
    magnitude = abs(fb_axis) + abs(lr_axis)
    command =  "Angle: " + str(angle) + "Mag: " + str(magnitude)
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
    run = monitor3()
