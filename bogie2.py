import XboxController
import time
import math
import RPi.GPIO as gpio

class Robot:
    """
    Class to setup a Robot.  Takes a dictionary of "commands" and
    their associated output pins (BOARD number)
    """
    def __init__(self, outputs):
        """
        Initialize Output (and Input) pins. Assign objects to groups
        """
        gpio.setmode(gpio.BOARD)
        self.outputs = outputs
        self.drive = {}
        self.sensor = {}
        self.servo = {}
        for output in self.outputs:
            gpio.setup(self.outputs[output], gpio.OUT)     
        for output in self.outputs.keys():
            self.drive[output] = gpio.PWM(self.outputs[output],100)
            self.drive[output].start(0)

    def __repr__(self):
        rep = "Robot("
        rep += "Output Map: " + str(self.outputs) + ","
        rep += "Drive: " + str(self.drive.keys()) + ","
        rep += "Sensor: " + str(self.sensor.keys()) + ","
        rep += "Servos: " + str(self.servo.keys()) + ")"
        return rep

    def halt(self):
        for item in self.drive:
            self.drive[item].stop()
        gpio.cleanup()

    
        
Bogie = Robot({"LR":7, "LF":11, "RR":13, "RF":15})
        
print Bogie

try:
    while True:
        for i in range(0,101):
            Bogie.drive["LF"].ChangeDutyCycle(i)
            Bogie.drive["RR"].ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(0,101):
            Bogie.drive["LF"].ChangeDutyCycle(100 - i)
            Bogie.drive["RR"].ChangeDutyCycle(100 - i)
            time.sleep(0.02)
            
except KeyboardInterrupt:
    for item in Bogie.drive:
        Bogie.drive[item].stop()
    gpio.cleanup()
