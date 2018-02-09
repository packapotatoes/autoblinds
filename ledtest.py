import RPi.GPIO as GPIO
import time

ledPin = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 100)
pwm.start(85)
time.sleep(2)
