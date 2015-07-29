import time
import RPi.GPIO as GPIO

LEDS = {1: 5,
        2: 6,
        4: 13,
        8: 19}
t = 1.0
GPIO.setmode(GPIO.BCM)

for LED in LEDS:
    GPIO.setup(LEDS[LED], GPIO.OUT)
    GPIO.output(LEDS[LED], GPIO.LOW)

for i in range(16):
    bin_string = '{0:04b}'.format(i)
    print bin_string
    GPIO.output(LEDS[1], int(bin_string[3]))
    GPIO.output(LEDS[2], int(bin_string[2]))
    GPIO.output(LEDS[4], int(bin_string[1]))
    GPIO.output(LEDS[8], int(bin_string[0]))
    time.sleep(t)
GPIO.cleanup()

