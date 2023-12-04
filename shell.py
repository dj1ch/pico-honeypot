# this script must be included on your machine for this to work
# this is a serial shell, that will not allow anyone to exit
import serial

# connect to the pico at /dev/ttyACM0 with 9600 bauds
serial = serial.Serial("/dev/ttyACM0", 9600)

# constantly print info
try:
    while true:
        data = serial.readline().decode("utf-8").strip()
        print(data)

# don't allow them to exit!
except KeyboardInterrupt:
    pass
