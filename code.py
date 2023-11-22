import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def loading_animation_slash(iterations=10):
    symbols = ['/', '|', '\\']
    for _ in range(iterations):
        for symbol in symbols:
            led.value = True
            time.sleep(0.1)
            led.value = False
            print('\rLoading ' + symbol, end='')
            time.sleep(0.1)

def server_startup():
    print('\nLinux raspberrypi 6.1.0-rpi6-rpi-v7 #1 SMP Raspbian 1:6.1.58-1+rpt2 (2023-10-27) armv7l')
    print('\nThe programs included with the Debian GNU/Linux system are free software; the exact distribution terms for each program are described in the individual files in /usr/share/doc/*/copyright.')
    print('\nDebian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law.')

    current_time = time.monotonic()
    login_time = f"\nLast login: {current_time}" # this might turn out weird, but its close enough
    print(login_time)
    while True:
        command = input('pi@raspberrypi:~ $ ')
        print(f"bash: {command}: command not found")
        time.sleep(5)  # adjust this time
        break

def count_numbers(starting_number):
    current_number = starting_number
    print("\nYou should leave now!")  # you can set the message the attacker sees before this starts
    time.sleep(2)  # delay before the counting
    while True:
        try:
            led.value = True # the led will turn on and stay on when the numbers are going
            print(current_number)
            current_number += 1
            time.sleep(0.0000000000000000000000001)  # keep in mind this will go really fast
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    try:
        loading_animation_slash() # you can remove this if you want to make it look realistic
        server_startup()
        count_numbers(1)
    except KeyboardInterrupt:
        print("Sorry, you can't exit!")
        pass  # prevent program from exiting
