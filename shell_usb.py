# note that this is the same script as shell.py
# this will be run if /dev/ttyACM0 does not exist
import serial

# connect to the pico at /dev/ttyUSB0 with 9600 bauds
serial = serial.Serial("/dev/ttyUSB0", 9600)

# constantly print info
try:
    while True:
        data = serial.readline().decode("utf-8").strip()
        print(data)

# don't allow them to exit!
except KeyboardInterrupt:
    pass
