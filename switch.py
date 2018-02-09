#!/usr/bin/env python

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitions
ledPin = 18 # Broadcom pin 18 (P1 pin 12)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

GPIO.output(ledPin, not GPIO.input(ledPin))
