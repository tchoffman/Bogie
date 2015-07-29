import time
import RPi.GPIO as GPIO

YLW = 5
BLU = 6
RED = 13
GRN = 19
t = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(YLW, GPIO.OUT)
GPIO.output(YLW, GPIO.LOW)
GPIO.setup(BLU, GPIO.OUT)
GPIO.output(BLU, GPIO.LOW)
GPIO.setup(RED, GPIO.OUT)
GPIO.output(RED, GPIO.LOW)
GPIO.setup(GRN, GPIO.OUT)
GPIO.output(GRN, GPIO.LOW)

for i in range(50):
    GPIO.output(YLW, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(BLU, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(GRN, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(YLW, GPIO.LOW)
    time.sleep(t)
    GPIO.output(BLU, GPIO.LOW)
    time.sleep(t)
    GPIO.output(RED, GPIO.LOW)
    time.sleep(t)
    GPIO.output(GRN, GPIO.LOW)
    time.sleep(t)
GPIO.cleanup()
