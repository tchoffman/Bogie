#!/usr/bin/python

import RPi.GPIO as GPIO
from lib.Adafruit_PWM_Servo_Driver import PWM
from lib import xbox_read
import time

# Define Constants
MAXPULSE = 4095
FREQ = 60

# Initialize the PWM Device
pwm = PWM(0x40)
pwm.setPWMFreq(FREQ)

class Robot:
    """
    Class to setup a Robot.  Takes a dictionary of "commands" and
    their associated output pins (BOARD number)
    """
    def __init__(self, drive_map, sensor_map, servo_map):
        """
        Initialize Output (and Input) pins. Assign objects to groups
        """
        self.drive = drive_map
        self.sensor = sensor_map
        self.servo = servo_map
        self.control = control_map
        for key in self.drive:
            self.pwm.setPWM(self.drive[key],0,0)
        for key in self.servo:
            self.servo[key]["POS"] = self.servo[key]["MID"]
            self.pwm.setPWM(self.servo[key]["PIN"],0,self.servo[key]["POS"])

    def __repr__(self):
        rep = "Robot: " + "\n"
        rep += "Drive Map: " + str(self.drive) + "\n"
        rep += "Sensor Map: " + str(self.sensor) + "\n"
        rep += "Servo Map: " + str(self.servo) + "\n"
        return rep

    def halt(self):
        for key in self.drive:
            self.pwm.setPWM(self.drive[key],0,0)
        for key in self.servo:
            self.pwm.setPWM(self.servo[key]["PIN"],0,self.servo[key]["MID"])
        
    def update(self, event):
        ## Drive Motors
        if event.key in self.control["DRV"]:
            
        ## Pivot Arm
        if event.key == "X2"
        ## Reach Arm
        ## Lift Arm
        ## Grip Arm
            
##
##
##
##        
##        throttle = -(throttle)
##        left_drive = throttle + direction
##        right_drive = throttle - direction
##        if left_drive >= 0:
##            self.pwm.setPWM(self.drive["LF"],0,int(min(abs(left_drive),1)*MAXPULSE))
##            self.pwm.setPWM(self.drive["LR"],0,0)
##        else:
##            self.pwm.setPWM(self.drive["LF"],0,0)
##            self.pwm.setPWM(self.drive["LR"],0,int(min(abs(left_drive),1)*MAXPULSE))
##        if right_drive >= 0:
##            self.pwm.setPWM(self.drive["RF"],0,int(min(abs(right_drive),1)*MAXPULSE))
##            self.pwm.setPWM(self.drive["RR"],0,0)
##        else:
##            self.pwm.setPWM(self.drive["RF"],0,0)
##            self.pwm.setPWM(self.drive["RR"],0,int(min(abs(right_drive),1)*MAXPULSE))
##            
##        ## Update Pivot
##        self.servo["PIVOT"]["POS"] -= int(pivot) * self.servo["PIVOT"]["MAG"]
##        if self.servo["PIVOT"]["POS"] > self.servo["PIVOT"]["MAX"]:
##            self.servo["PIVOT"]["POS"] = self.servo["PIVOT"]["MAX"]
##        if self.servo["PIVOT"]["POS"] < self.servo["PIVOT"]["MIN"]:
##            self.servo["PIVOT"]["POS"] = self.servo["PIVOT"]["MIN"]
##        self.pwm.setPWM(self.servo["PIVOT"]["PIN"],0,self.servo["PIVOT"]["POS"])
##
##        ## Update REACH
##        self.servo["REACH"]["POS"] -= int(reach) * self.servo["REACH"]["MAG"]
##        if self.servo["REACH"]["POS"] > self.servo["REACH"]["MAX"]:
##            self.servo["REACH"]["POS"] = self.servo["REACH"]["MAX"]
##        if self.servo["REACH"]["POS"] < self.servo["REACH"]["MIN"]:
##            self.servo["REACH"]["POS"] = self.servo["REACH"]["MIN"]
##        self.pwm.setPWM(self.servo["REACH"]["PIN"],0,self.servo["REACH"]["POS"])
##
##        ## Update LIFT
##        self.servo["LIFT"]["POS"] += int((lift - dip) * 100) 
##        self.pwm.setPWM(self.servo["LIFT"]["PIN"],0,self.servo["LIFT"]["POS"])
##
##        ## Update GRIP
##        if grip == 1:
##            self.pwm.setPWM(self.servo["GRIP"]["PIN"],0,self.servo["GRIP"]["MIN"])
##        if grip == 0:
##            self.pwm.setPWM(self.servo["GRIP"]["PIN"],0,self.servo["GRIP"]["MAX"])

    def read_sensors(self, command):
        pass
    
## Initiate Bogie Rover
drive_map = {"LR":0, "LF":1, "RR":3, "RF":2}
sensor_map = {}
servo_map = {"PVT":{"PIN":12,"MID":400,"W":600},              # SERVO MAP
               "RCH":{"PIN":13,"MID":400,"W":400},
               "LFT":{"PIN":14,"MID":450,"W":500},
               "GRP":{"PIN":15,"MID":400,"W":100}}
control_map = {"DRV":["X1","Y1"],"PVT":["X2"], "RCH":["Y2"],"LFT":["LT", "RT"], "GRP":["RB","LB"]}
Bogie = Robot(drive_map, sensor_map, servo_map, control_map)   
print Bogie

for event in xbox_read.event_stream(deadzone=12000):
    if event.value == "back":
        Bogie.halt()
        print "HALTED"
        break
    else: 
        Bogie.update(event)
        
print "END"
