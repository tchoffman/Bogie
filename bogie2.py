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

    def update_motors(self, command):
        for item in command:
            self.motor[item[0]] = item[1]
            self.drive[item[0]].ChangeDutyCycle(item[1])

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
        for i in range(0,101):
            Bogie.update_motors([["LF",i],["RR",i]])
            print Bogie.motor
            time.sleep(0.005)
        for i in range(0,101):
            Bogie.update_motors([["LF",100 - i],["RR",100 - i]])
            print Bogie.motor
            time.sleep(0.005)
            
except KeyboardInterrupt:
    for item in Bogie.drive:
        Bogie.drive[item].stop()
    gpio.cleanup()
