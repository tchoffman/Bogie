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
            self.drive[pin].start(self.motor[pin])

    def __repr__(self):
        rep = "Robot: " + "\n"
        rep += "Drive Map: " + str(self.drive_map) + "\n"
        rep += "Sensor Map: " + str(self.sensor_map) + "\n"
        rep += "Servo Map: " + str(self.servo_map) + "\n"
        return rep

    def halt(self):
        for item in self.drive:
            self.drive[item].stop()
        gpio.cleanup()

    def update_drives(self, throttle, direction):
        throttle = -(throttle)
        left_drive = throttle + direction
        right_drive = throttle - direction
        if left_drive >= 0:
            self.motor["LF"] = min(left_drive,1)*100
            self.motor["LR"] = 0
        else:
            self.motor["LF"] = 0
            self.motor["LR"] = min(abs(left_drive), 1)*100
        if right_drive >= 0:
            self.motor["RF"] = min(right_drive,1)*100
            self.motor["RR"] = 0
        else:
            self.motor["RF"] = 0
            self.motor["RR"] = min(abs(right_drive),1)*100

        for item in self.drive:
            self.drive[item].ChangeDutyCycle(self.motor[item])
            
    def update_servos(self, command):
        pass

    def read_sensors(self, command):
        pass
    
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
        Bogie.update_drives(control.controlValues[1],control.controlValues[0])
        
except control.controlValues[12] == 1:
    Bogie.halt()
    
except KeyboardInterrupt:
    Bogie.halt()
