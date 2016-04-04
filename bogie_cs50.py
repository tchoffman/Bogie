import XboxController
import time
import math
from Adafruit_PWM_Servo_Driver import PWM
#pwm = PWM(0x40)
#pwm.setPWMFreq(60)
MAXPULSE = 4095

class Robot:
    """
    Class to setup a Robot.  Takes a dictionary of "commands" and
    their associated output pins (BOARD number)
    """
    def __init__(self, drive_map, sensor_map, servo_map):
        """
        Initialize Output (and Input) pins. Assign objects to groups
        """
        self.pwm = PWM(0x40)
        self.pwm.setPWMFreq(60)
        self.drive = drive_map
        self.sensor = sensor_map
        self.servo = servo_map
        for key in self.drive:
            self.pwm.setPWM(self.drive[key],0,0)
        for key in self.servo:
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
            self.pwm.setPWM(self.servo[key]["PIN"],0,self.servo[key]["POS"])
        
    def update_drives(self, throttle, direction):
        throttle = -(throttle)
        left_drive = throttle + direction
        right_drive = throttle - direction
        if left_drive >= 0:
            self.pwm.setPWM(self.drive["LF"],0,int(min(abs(left_drive),1)*MAXPULSE))
            self.pwm.setPWM(self.drive["LR"],0,0)
        else:
            self.pwm.setPWM(self.drive["LF"],0,0)
            self.pwm.setPWM(self.drive["LR"],0,int(min(abs(left_drive),1)*MAXPULSE))
        if right_drive >= 0:
            self.pwm.setPWM(self.drive["RF"],0,int(min(abs(right_drive),1)*MAXPULSE))
            self.pwm.setPWM(self.drive["RR"],0,0)
        else:
            self.pwm.setPWM(self.drive["RF"],0,0)
            self.pwm.setPWM(self.drive["RR"],0,int(min(abs(right_drive),1)*MAXPULSE))
            
    def update_servos(self, pivot, reach, dip, lift, grip):
        print "P: ", pivot, "  R: ", reach, " D/L: ", dip, "/", lift, " G: ", grip, "\n"
        ## Update Pivot
        self.servo["PIVOT"]["POS"] -= int(pivot) * self.servo["PIVOT"]["MAG"]
        if self.servo["PIVOT"]["POS"] > self.servo["PIVOT"]["MAX"]:
            self.servo["PIVOT"]["POS"] = self.servo["PIVOT"]["MAX"]
        if self.servo["PIVOT"]["POS"] < self.servo["PIVOT"]["MIN"]:
            self.servo["PIVOT"]["POS"] = self.servo["PIVOT"]["MIN"]
        self.pwm.setPWM(self.servo["PIVOT"]["PIN"],0,self.servo["PIVOT"]["POS"])

        ## Update REACH
        self.servo["REACH"]["POS"] -= int(reach) * self.servo["REACH"]["MAG"]
        if self.servo["REACH"]["POS"] > self.servo["REACH"]["MAX"]:
            self.servo["REACH"]["POS"] = self.servo["REACH"]["MAX"]
        if self.servo["REACH"]["POS"] < self.servo["REACH"]["MIN"]:
            self.servo["REACH"]["POS"] = self.servo["REACH"]["MIN"]
        self.pwm.setPWM(self.servo["REACH"]["PIN"],0,self.servo["REACH"]["POS"])

        ## Update LIFT
        self.servo["LIFT"]["POS"] += int((lift - dip) * 100) 
        self.pwm.setPWM(self.servo["LIFT"]["PIN"],0,self.servo["LIFT"]["POS"])

        ## Update GRIP
        if grip == 1:
            self.pwm.setPWM(self.servo["GRIP"]["PIN"],0,self.servo["GRIP"]["MIN"])
        if grip == 0:
            self.pwm.setPWM(self.servo["GRIP"]["PIN"],0,self.servo["GRIP"]["MAX"])

    def read_sensors(self, command):
        pass
    
## Initiate Bogie Rover: Robot({DRIVE MAP},{SENSOR MAP},{SERVO MAP})        
Bogie = Robot({"LR":0, "LF":1, "RR":3, "RF":2},                 # DRIVE MAP
              {},                                               # SENSOR MAP
              {"PIVOT":{"PIN":12,"MIN":100,"POS":400,"MAX":700,"MAG":2},
               "REACH":{"PIN":13,"MIN":200,"POS":400,"MAX":600,"MAG":10},
               "LIFT":{"PIN":14,"MIN":200,"POS":450,"MAX":700,"MAG":10},
               "GRIP":{"PIN":15,"MIN":350,"POS":350,"MAX":450,"MAG":10}}    #SERVO MAP
              )   
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
        Bogie.update_drives(control.controlValues[0],       # Throttle
                            control.controlValues[1])       # Direction
        Bogie.update_servos(control.controlValues[2],       # Pivot
                            control.controlValues[3],       # Reach
                            control.controlValues[4],       # Dip
                            control.controlValues[5],       # Lift
                            control.controlValues[11])      # Grip

except control.controlValues[12] == 1:
    Bogie.halt()
    control.stop()
    
except KeyboardInterrupt:
    Bogie.halt()
    control.stop()
