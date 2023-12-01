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
