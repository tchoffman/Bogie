import time
import RPi.GPIO as gpio
import sys
import Tkinter as tk

WHEELS = {"LR": 7,
        "LF": 11,
        "RR": 13,
        "RF": 15}

def init():
    gpio.setmode(gpio.BOARD)
    for WHEEL in WHEELS:
        gpio.setup(WHEELS[WHEEL], gpio.OUT)
        gpio.output(WHEELS[WHEEL], gpio.LOW)

def forward(t):
    pass
def reverse(t):
    pass
def turn_left(t):
    pass
def turn_right(t):
    pass
def pivot_left(t):
    pass
def pivot_right(t):
    pass

def key_input(event):
    init()
    print "Key: ", event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == "w":
        forward(sleep_time)
    elif key_press.lower() == "s":
        backward(sleep_time)
    elif key_press.lower() == "a":
        turn_left(sleep_time)
    elif key_press.lower() == "d":
        turn_right(sleep_time)
    elif key_press.lower() == "q":
        pivot_left(sleep_time)
    elif key_press.lower() == "e":
        pivot_right(sleep_time)
    else:
        time.sleep(sleep_time)

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()

gpio.cleanup()
