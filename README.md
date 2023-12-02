# Pico Honeypot
## A raspberry pi pico honeypot, that pretends to be a linux server.

### Intro
This pretends to be a debian 12 server. I would host this on some sort of port for your server, but as soon as attackers log in they will be put into a serial shell(hosted on your own server container), which is on the raspberry pi pico. It will troll them by saying "command not found" as they attempt to do things on it. After a couple seconds, the pico will start counting, really fast. This might confuse the attacker. Along with that, they will be trapped in this shell, unless they deliberatly get out of the serial shell. However, this is in a container and everything can be deleted by the host system. If you want to, you can mess with the python to make it a server using the pico w, although I use the regular pico. It might be a bit much to make it an entire server, handling multiple connections at once.

### What you need
- a container with bash installed
- a raspberry pi pico
- circuitpython firmware(latest version)
- another pc to copy the files onto the pico
- an IDE if you want to test new changes

### Install guide
- get a docker container with debian, ubuntu, etc. any works as long as it has bash, as this will run the serial shell on startup
- download the code for the [pico](code.py), and the code to put on the [container](script.sh), along with these two python scripts for the container. [here's the first one](shell.py), and [here's the second one](shell_usb.py)
- copy the `code.py` onto the pico
- put the `script.sh`, `shell.py` and `shell_usb.py` onto the container
- on the container, install the `pyserial` library using `pip`. be sure to install python and pip as well!

```shell
sudo apt install python3 pip -y
```

then run the command

```shell
pip install pyserial
```

by now we should have all of our depedancies and needed libraries now.

- mark the script as an executable

```shell
sudo chmod +x script.sh
```

- edit your .bashrc and add this line(.bashrc is usually in `/home/$USER/.bashrc`, although this is only for the user that is being logged into by the attacker. you can add it to the `/etc/.bashrc` if you want changes to be for the whole system)

```shell
/path/to/script.sh  # replace with the actual path to the script.sh
```
- make sure to apply these changes

```shell
source /home/$USER/.bashrc
```

- plug the pico into your server/container
- you may need to give the container permissions to access the `/dev` directory, or perhaps the name of the usb device. most of the time the raspberry pi pico is referred to as `ttyACM0` in the `/dev` directory. sometimes, it could be referred to as `ttyUSB0`. when in doubt, you can always check the devices in the `/dev` directory using the command:

```shell
ls /dev | grep tty
```

- you can give docker permissions to that device with a command like this:

```shell
docker <some command> <some flag> -v /dev:/dev/<name of usb device> <other arguments>
```
- or just give it access to the entire `/dev` directory

```shell
docker <some command> <some flag> -v /dev:/dev <other arguments>
```

- see [this article](https://www.losant.com/blog/how-to-access-serial-devices-in-docker) for more information, although you can google yourself.
- expose your server(docker or any other container service) to the internet, by any means necessary.
- if the light is blinking, that means the pico is starting up normally
- wait for the light on the pico to turn on and stay on, as this means the 'troll' is running, and that the attacker has logged in
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
