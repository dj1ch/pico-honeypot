# Pico Honeypot
## a raspberry pi pico honeypot, that pretends to be a linux server.

### Intro
This pretends to be a debian 12 server. I would host this on some sort of port for your server, but as soon as attackers log in they will be put into a serial shell(hosted on your own server), which is on the raspberry pi pico. It will troll them by saying "command not found" as they attempt to do things on it. After a couple seconds, the pico will start counting, really fast. This might confuse the attacker. Along with that, they will be trapped in this shell, unless they deliberatly get out of the serial shell. However, this is in a container and everything can be deleted by the host system. If you want to, you can mess with the python to make it a server using the pico w, although I use the regular pico. 

### What you need
- a raspberry pi pico
- circuitpython firmware(latest version)
- another pc to copy the files onto the pico
- an IDE if you want to test new changes

### Install guide
- get a docker container with debian, ubuntu, etc. any works as long as it has bash, as this will run the serial shell on startup
- download the [code](code.py)
- copy it onto the pico
- plug the pico into your server/container
- you may need to give the container permissions to access the `/dev` directory, or perhaps the name of the usb device. most of the time the raspberry pi pico is referred to as `ttyACM0` in the `/dev` directory

```shell
docker <some command> <some flag> -v /dev:/dev/<name of usb device> <other arguments>
```

- see [this article](https://www.losant.com/blog/how-to-access-serial-devices-in-docker) for more information, although you can google yourself.
- set a cronjob to run `minicom -D /dev/ttyACM0` (minicom must be installed, along with user in dialout group)
  
example crontab:
```shell
# this connects to the pico shell on each reboot
@reboot minicom -D /dev/ttyACM0
```
- wait for the light on the pico to turn on and stay on, as this means the 'troll' is running
- in this case, the troll looks something like this:
```shell
pi@raspberrypi :-$ uname -a
bash: uname -a: command not found

You should leave now!! # right here you can customize this message in the python script
1 # note that this output goes really fast. the control c keyboard interrupt doesn't work, and this keeps going forever
2
3
4
5
6
7
8
9
10
```
