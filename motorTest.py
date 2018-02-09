import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
ctrl1_pin = 7
ctrl2_pin = 11
pwm_pin = 12

freq = 100 # frequency for pwm
dc = 0     # duty cycle for pwm
GPIO.setup(ctrl1_pin, GPIO.OUT)
GPIO.setup(ctrl2_pin, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 100)
pwm.start(0)

def clockwise():
    GPIO.output(ctrl1_pin, True)
    GPIO.output(ctrl2_pin, False)

def counter_clockwise():
    GPIO.output(ctrl1_pin, False)
    GPIO.output(ctrl2_pin, True)

def set_control_pins( pin1, pin2 ):
    ctrl1_pin = pin1;
    ctrl2_pin = pin2;

def set_pwm_pin( pin ):
    pwm_pim = pin;

def setup():
    GPIO.setup(ctrl1_pin, GPIO.OUT)
    GPIO.setup(strl2_pin, GPIO.OUT)
    GPIO.setup(pwm_pin, GPIO.OUT)
    pwm = GPIO.PWM(pwm_pin, 100)
    pwm.start(0)           
    
clockwise()
    
while True:
    cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "x":
        pwm.stop()
        GPIO.cleanup()
        break
    elif direction == "f":
        clockwise()
    else:
        counter_clockwise()
    speed = int(cmd[1]) * 11
    pwm.ChangeDutyCycle(speed)
    
