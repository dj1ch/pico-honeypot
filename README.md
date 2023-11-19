# fake-pico-server
## a raspberry pi pico honeypot, that pretends to be a linux server.

This pretends to be a debian 12 server. I would host this on some sort of port for your server, but as soon as attackers log in they will be put into a serial shell(hosted on your own server), which is on the raspberry pi pico. It will troll them by saying "command not found" as they attempt to do things on it. If you want to, you can mess with the python to make it a server using the pico w, although I use the regular pico. 
