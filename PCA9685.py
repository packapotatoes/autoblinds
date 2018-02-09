import smbus
import time

bus = smbus.SMBus(1)

# Registers
DEVICE_ADDRESS = 0x40
MODE1 = 0x00
MODE2 = 0x01

# Bits
SLEEP = 0x10

class PCA9685:
    def __init__(self):
        pi = 1
        
    def wake(self):
        mode1 = bus.read_byte_data(DEVICE_ADDRESS, MODE1)
        print "{0:#010b}".format(mode1)
        asleep = mode1 & SLEEP
        if asleep:
            # set bit 4 of MODE1 register to 0 to turn on oscilator
            bus.write_byte_data(DEVICE_ADDRESS, MODE1, mode1 & (SLEEP ^ 0xFF)) # use xor (SLEEP ^ 0xFF) instead of ~SLEEP to avoid problems with signed numbers
            time.sleep(1)
        mode1 = bus.read_byte_data(DEVICE_ADDRESS, MODE1)
        if mode1 & SLEEP == True:
            print "{0:#010b}".format(mode1)
        else:
            print "PWM controller is now woke."
        
    def sleep(self):
        mode1 = bus.read_byte_data(DEVICE_ADDRESS, MODE1)
        asleep = mode1 & SLEEP
        if not asleep:
            bus.write_byte_data(DEVICE_ADDRESS, MODE1, MODE1 | SLEEP)

        print_register(MODE1)

def print_register(register):
    reg = bus.read_byte_data(DEVICE_ADDRESS, register)
    print "{0:#010b}".format(reg)
