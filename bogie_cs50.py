#!/usr/bin/python

from lib.Adafruit_PWM_Servo_Driver import PWM
from lib import xbox_read
import time

# Define Constants
MAXPULSE = 4095
MAXJOYSTICK = 32700
MAXTRIGGER = 255
FREQ = 60

# Initialize the PWM Device
pwm = PWM(0x40)
pwm.setPWMFreq(FREQ)

class Robot:
    """
    Class to setup a Robot.  Takes a dictionary of "commands" and
    their associated output pins (BOARD number)
    """
    def __init__(self, drive_map, sensor_map, servo_map, control_map):
        """
        Initialize Output (and Input) pins. Assign objects to groups
        """
        self.drive = drive_map
        self.sensor = sensor_map
        self.servo = servo_map
        self.control = control_map
        # Initialize the PWM Device
        self.pwm = PWM(0x40)
        self.pwm.setPWMFreq(FREQ)
        for key in self.drive:
            self.pwm.setPWM(self.drive[key],0,0)
        for key in self.servo:
            self.servo[key]["POS"] = self.servo[key]["MID"]
            self.servo[key]["WIDTH"] = self.servo[key]["MAX"] - self.servo[key]["MIN"]
            self.pwm.setPWM(self.servo[key]["PIN"],0,self.servo[key]["POS"])

    def __repr__(self):
        """
        String Representation of Robot instance
        """
        rep = "Robot: " + "\n\n"
        rep += "Drive Map:   " + str(self.drive) + "\n\n"
        rep += "Sensor Map:  " + str(self.sensor) + "\n\n"
        rep += "Servo Map:   " + str(self.servo) + "\n\n"
        rep += "Control Map: " + str(self.control) + "\n\n"
        return rep

    def halt(self):
        """
        Function to reset Robot to Initial Values and Stop execution
        """
        print "HALT()"
        for key in self.drive:
            self.pwm.setPWM(self.drive[key],0,0)
        for key in self.servo:
            self.pwm.setPWM(self.servo[key]["PIN"],0,self.servo[key]["MID"])
        
        
    def update(self, event):
        """
        Update Control States and Update PWM for each Motor or Servo when appropriate
        """
        ## update control states
        self.control[event.key] = event.value

        ## Drive Motors
        if event.key in ["X1","Y1"]:
            throttle  = float(self.control["Y1"]) / MAXJOYSTICK
            direction = float(self.control["X1"]) / MAXJOYSTICK
            L = MAXPULSE * (throttle + direction)
            R = MAXPULSE * (throttle - direction)
            if L >= 0:
                self.pwm.setPWM(self.drive["LR"],0,0)
                self.pwm.setPWM(self.drive["LF"],0,int(min(abs(L),MAXPULSE)))
            else:
                self.pwm.setPWM(self.drive["LF"],0,0)
                self.pwm.setPWM(self.drive["LR"],0,int(min(abs(L),MAXPULSE)))
            if R >= 0:
                self.pwm.setPWM(self.drive["RR"],0,0)
                self.pwm.setPWM(self.drive["RF"],0,int(min(abs(R),MAXPULSE)))
            else:
                self.pwm.setPWM(self.drive["RF"],0,0)
                self.pwm.setPWM(self.drive["RR"],0,int(min(abs(R),MAXPULSE)))
                                
        ## Pivot Arm
        if event.key == "X2":
            pivot = float(self.control["X2"]) / MAXJOYSTICK
            pivot = pivot * self.servo["PVT"]["WIDTH"] / 2
            pivot = int(pivot) + self.servo["PVT"]["MID"]
            self.servo["PVT"]["POS"] = pivot
            print "PIVOT: ", self.servo["PVT"]["POS"]
            self.pwm.setPWM(self.servo["PVT"]["PIN"],0,self.servo["PVT"]["POS"])
            
        ## Reach Arm
        if event.key == "Y2":
            reach = float(self.control["Y2"]) / MAXJOYSTICK
            reach = reach * self.servo["RCH"]["WIDTH"] / 2
            reach = int(reach) + self.servo["PVT"]["MID"]
            self.servo["RCH"]["POS"] = reach
            print "REACH: ", self.servo["RCH"]["POS"]
            self.pwm.setPWM(self.servo["RCH"]["PIN"],0,self.servo["RCH"]["POS"])
                          
        ## Lift Arm
        if event.key in ["LT","RT"]:
            lift = float(self.control["RT"] - self.control["LT"]) / MAXTRIGGER
            lift = lift * self.servo["LFT"]["WIDTH"] / 2
            lift = int(lift) + self.servo["LFT"]["MID"]
            self.servo["LFT"]["POS"] = lift
            print "LIFT:  ", self.servo["LFT"]["POS"]
            self.pwm.setPWM(self.servo["LFT"]["PIN"],0,self.servo["LFT"]["POS"])
        
        ## CLOSE GRIP    
        if event.key == "RB" and event.value == 1:
            print "CLOSE GRIP"
            self.servo["GRP"]["POS"] = self.servo["GRP"]["MAX"]
            self.pwm.setPWM(self.servo["GRP"]["PIN"],0,self.servo["GRP"]["POS"])

        ## OPEN GRIP
        if event.key == "LB" and event.value == 1:
            print "OPEN GRIP"
            self.servo["GRP"]["POS"] = self.servo["GRP"]["MIN"]
            self.pwm.setPWM(self.servo["GRP"]["PIN"],0,self.servo["GRP"]["POS"])
            
    def read_sensors(self, command):
        pass
    
## Initiate Bogie Rover
drive_map = {"LR":1, "LF":0, "RR":3, "RF":2}
sensor_map = {}
servo_map = {"PVT":{"PIN":12,"MIN":135,"MID":405,"MAX":675,"MAG":1},              # SERVO MAP
             "RCH":{"PIN":13,"MIN":200,"MID":400,"MAX":600,"MAG":1},
             "LFT":{"PIN":14,"MIN":200,"MID":450,"MAX":700,"MAG":1},
             "GRP":{"PIN":15,"MIN":350,"MID":350,"MAX":410,"MAG":1}}
control_map = {"X1":0,"Y1":0,"X2":0,"Y2":0,"LT":0,"RT":0,"RB":0,"LB":0,"start":0,"guide":0,"back":0,
               "A":0,"B":0,"X":0,"Y":0,"dl":0,"dr":0,"du":0,"dd":0,"TL":0,"TR":0}
Bogie = Robot(drive_map, sensor_map, servo_map, control_map)   
print Bogie

for event in xbox_read.event_stream(deadzone=12000):
    if event.key == "back" and event.value == 1:
        Bogie.halt()
    else: 
        Bogie.update(event)
