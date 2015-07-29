import XboxController
import time
import math
import RPi.GPIO as gpio
pwm_freq = 100

class Robot:
    """
    Class to setup a Robot.  Takes a dictionary of "commands" and
    their associated output pins (BOARD number)
    """
    def __init__(self, drive_map, sensor_map, servo_map):
        """
        Initialize Output (and Input) pins. Assign objects to groups
        """
        gpio.setmode(gpio.BOARD)
        self.drive_map = drive_map
        self.drive = {}
        self.motor = {}
        self.sensor_map = sensor_map
        self.sensor = {}
        self.servo_map = servo_map
        self.servo = {}
        for pin in self.drive_map:
            gpio.setup(self.drive_map[pin], gpio.OUT)
            self.motor[pin] = 0
            self.drive[pin] = gpio.PWM(self.drive_map[pin],pwm_freq)
            self.drive[pin].start(motor[pin])

    def __repr__(self):
        rep = "Robot("
        rep += "Drive Map: " + str(self.drive_map) + ","
        rep += "Sensor Map: " + str(self.sensor_map) + ","
        rep += "Servo Map: " + str(self.servo_map) + ")"
        return rep

    def halt(self):
        for item in self.drive:
            self.drive[item].stop()
        gpio.cleanup()

    
## Initiate Bogie Rover        
Bogie = Robot({"LR":7, "LF":11, "RR":13, "RF":15}, {}, {})   
print Bogie


## initiate Xbox Controller
control = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)
control.start()

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
