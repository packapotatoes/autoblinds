# Tests sending commands to the PWM controller (PCA9685) via i2c

import time
import smbus

bus = smbus.SMBus(1)

# Registers
DEVICE_ADDRESS = 0x40  # i2c bus address of PCA9685
MODE1 = 0x00           # MODE1 register
OUT3_ON_H = 0x13       # MSBs for output 3 on PCA9685

# Bits
SLEEP = 0x10

result = bus.read_byte_data(DEVICE_ADDRESS, MODE1) # read current contents of MODE1 register
print "{0:b}".format(result)
bus.write_byte_data(DEVICE_ADDRESS, MODE1, result & ~SLEEP)
time.sleep(1)
result = bus.read_byte_data(DEVICE_ADDRESS, MODE1)
print "{0:b}".format(result)
print "{0:b}".format(~SLEEP)

bus.write_byte_data(DEVICE_ADDRESS, OUT3_ON_H, 0x10) # Turn on PWM output 3 fully by writing 1 to bit 
led3 = bus.read_byte_data(DEVICE_ADDRESS, OUT3_ON_H)

#bus.write_byte_data(DEVICE_ADDRESS, 0x07, 8)
time.sleep(3)
bus.write_byte_data(DEVICE_ADDRESS, 0x13, 0)
bus.write_byte_data(DEVICE_ADDRESS, 0x07, 0)

#led3 = bus.read_byte_data(DEVICE_ADDRESS, OUT3_ON_H)

print "{0:b}".format(led3)
print "{0:b}".format(result)

on_l = 0x00
on_h = 0x00
off_l = 0x00
off_h = 0x00
on = 100

bus.write_byte_data(DEVICE_ADDRESS, 0x08, off_l)
bus.write_byte_data(DEVICE_ADDRESS, 0x09, off_h)

bus.write_byte_data(DEVICE_ADDRESS, 0x06, on & 0xff)
bus.write_byte_data(DEVICE_ADDRESS, 0x07, on >> 8)
time.sleep(1)

while(1):
    num = raw_input()
    num = int(num)
    if( num > 4095):
        break
    bus.write_byte_data(DEVICE_ADDRESS, 0x06, num & 0xff)
    bus.write_byte_data(DEVICE_ADDRESS, 0x07, num >> 8)
    

#while(on < 4095):
#    bus.write_byte_data(DEVICE_ADDRESS, 0x06, on & 0xff)
#    bus.write_byte_data(DEVICE_ADDRESS, 0x07, on >> 8)
#    on += 1
#    print(str(on) + "\n")
#    time.sleep(.01)

bus.write_byte_data(DEVICE_ADDRESS, MODE1, 0x80)
