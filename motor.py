import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pwm, ctrl1, ctrl2, mode=GPIO.BOARD):
        self.ctrl1_pin = ctrl1
        self.ctrl2_pin = ctrl2
        self.pwm_pin = pwm
        self.freq = 100
        self.dc = 0
        self.mode = mode
        
        GPIO.setmode(self.mode)
        GPIO.setup(self.ctrl1_pin, GPIO.OUT)
        GPIO.setup(self.ctrl2_pin, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.pwm_pin, self.freq)
        
    def clockwise(self):
        GPIO.output(self.ctrl1_pin, True)
        GPIO.output(self.ctrl2_pin, False)

    def counter_clockwise(self):
        GPIO.output(self.ctrl1_pin, False)
        GPIO.output(self.ctrl2_pin, True)

    def stop(self):
        pwm.stop()
        GPIO.output(self.ctrl1_pin, False)
        GPIO.output(self.ctrl2_pin, False)
        
    def set_duty_cycle(self, dc):
        self.dc = dc
        self.pwm.ChangeDutyCycle(self.dc)

    def start(self, ):
        self.pwm.start(self.dc)
