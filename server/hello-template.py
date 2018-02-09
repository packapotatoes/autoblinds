from __future__ import print_function
from flask import Flask, request, render_template
#from RPIO import PWM
import pigpio
import sys
#import RPi.GPIO as GPIO
import datetime

pi = pigpio.pi()
#pwm = PWM.Servo()
#ledPin = 36 # Board numbering
#LED.set_servo(16, 1200)

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(ledPin, GPIO.OUT)
#pwm = GPIO.PWM(ledPin, 100)
#pwm.start(0)
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'Hello!',
        'time' : timeString
    }
    return render_template('main.html', **templateData)

#@app.route("/phptest")
#def phptest():
#    return render_template('phptest.php')


@app.route("/phptest/", methods=['POST', 'GET'])
def phptest():
    if request.method == 'GET':
        return render_template('phptest.php')
    if request.method == 'POST':
        data = request.form['sliderValue']
        print('Setting LED duty cycle to ' + data, file=sys.stderr)
#        LED.set_servo(16, float(data)*1000)
        #pwm.ChangeDutyCycle(float(data))
        pi.set_PWM_dutycycle(16, data) #BCM 1 = Board 28
        return '1'
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
