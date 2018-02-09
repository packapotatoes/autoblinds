from motor import Motor
from time import sleep

motor = Motor(12, 7, 11)

motor.set_duty_cycle(20)
motor.clockwise()
motor.start()
sleep(2)
motor.set_duty_cycle(90)
sleep(2)
motor.counter_clockwise()
sleep(2)
motor.stop()
