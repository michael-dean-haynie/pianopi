# pianopi

## How to ssh into raspberrypi if ".local" DNS name is not resolving
* In a browser go to 192.168.0.1
* Login
* Go to Wireless - Access Control to see connected devices and their ips
* `ssh michael@<ip>`

## Raspberry Pi Installation / (Update in case of startup.sh changes)
* SSH into the raspberry pi
```shell
# install minimal dependencies
sudo apt update -y
sudo apt upgrade -y
sudo apt install git -y

# pull code from github
cd ~
sudo git clone https://github.com/michael-dean-haynie/pianopi.git
cd pianopi

# copy startup script to system directory
sudo cp pianopi-startup.sh /usr/local/bin/pianopi-startup.sh
sudo chmod +x /usr/local/bin/pianopi-startup.sh

# configure startup script to be run when system reboots
sudo chmod +x pianopi-install.sh
./pianopi-install.sh
```
* reboot the raspberry pi `sudo reboot`


## Information about the midi device maker/product
Bus 001 Device 009: ID 09e8:0050 AKAI  Professional M.I. Corp. MPK mini Play mk3    

## Python Attempt
```shell
sudo apt install python3-pip -y
sudo pip install mido
sudo pip install python-rtmidi
sudo pip install websocket-client
chmod +x midi_reader.py # get this from this git repository
./midi_reader.py
```
