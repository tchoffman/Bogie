import time
import RPi.GPIO as gpio

WHEELS = {"LR": 7,
        "LF": 11,
        "RR": 13,
        "RF": 15}

gpio.setmode(gpio.BOARD)

for WHEEL in WHEELS:
    gpio.setup(WHEELS[WHEEL], gpio.OUT)
    gpio.output(WHEELS[WHEEL], gpio.LOW)

def forward(t):
    gpio.output(WHEELS["LF"],gpio.HIGH)
    gpio.output(WHEELS["RF"],gpio.HIGH)
    time.sleep(t)
    gpio.output(WHEELS["LF"],gpio.LOW)
    gpio.output(WHEELS["RF"],gpio.LOW)
    pass

def backward(t):
    gpio.output(WHEELS["LR"],gpio.HIGH)
    gpio.output(WHEELS["RR"],gpio.HIGH)
    time.sleep(t)
    gpio.output(WHEELS["LR"],gpio.LOW)
    gpio.output(WHEELS["RR"],gpio.LOW)
    pass

def wobble(t):
    for WHEEL in WHEELS:
        gpio.output(WHEELS[WHEEL], gpio.HIGH)
        time.sleep(t)
        gpio.output(WHEELS[WHEEL], gpio.LOW)
        time.sleep(t)
    pass

def circle_cw(t):
    gpio.output(WHEELS["LF"],gpio.HIGH)
    gpio.output(WHEELS["RR"],gpio.HIGH)
    time.sleep(t)
    gpio.output(WHEELS["LF"],gpio.LOW)
    gpio.output(WHEELS["RR"],gpio.LOW)
    pass

def circle_ccw(t):
    gpio.output(WHEELS["RF"],gpio.HIGH)
    gpio.output(WHEELS["LR"],gpio.HIGH)
    time.sleep(t)
    gpio.output(WHEELS["RF"],gpio.LOW)
    gpio.output(WHEELS["LR"],gpio.LOW)
    pass

def turn_r(t):
    gpio.output(WHEELS["LF"],gpio.HIGH)
    time.sleep(t)
    gpio.output(WHEELS["LF"],gpio.LOW)
    pass

def turn_l(t):
    gpio.output(WHEELS["RF"],gpio.HIGH)
    time.sleep(t)
    gpio.output(WHEELS["RF"],gpio.LOW)
    pass

wobble(.15)
time.sleep(1)
forward(.5)
time.sleep(.5)
backward(.5)
time.sleep(.5)
circle_cw(1)
time.sleep(.5)
circle_ccw(1)
time.sleep(.5)
wobble(.15)
turn_r(.5)
time.sleep(.5)
turn_l(.5)

gpio.cleanup()
