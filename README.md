# pianopi

## How to ssh into raspberrypi if ".local" DNS name is not resolving
* In a browser go to 192.168.0.1
* Login
* Go to Wireless - Access Control to see connected devices and their ips
* `ssh michael@<ip>`

## How to check logs on raspberry pi
```shell
sudo systemctl status pianopi.service
sudo journalctl -f -n 100 -u pianopi.service
```

## How to share self-signed certificate with raspberry pi for local development
```shell
# from the web server machine (update user@ip if needed)
scp /Users/michael/certs/ca.crt michael@192.168.0.11:/home/michael/ca.crt

# then ssh into the raspberry pi
sudo cp /home/michael/ca.crt /usr/local/share/ca-certificates/
sudo rm /home/michael/ca.crt
sudo update-ca-certificates
```

## Raspberry Pi Installation / (Update in case of startup.sh changes)
* SSH into the raspberry pi
```shell
# install minimal dependencies
sudo apt update -y
sudo apt upgrade -y
sudo apt install vim -y
sudo apt install git -y

# set up local network hosts
sudo -- sh -c "echo \"192.168.0.3 mbp.local\" >> /etc/hosts"
sudo -- sh -c "echo \"192.168.0.11 pianopi.local\" >> /etc/hosts"

# pull code from github
cd ~
sudo git clone https://github.com/michael-dean-haynie/pianopi.git
cd pianopi

# copy startup script to system directory
sudo cp pianopi-startup.sh /usr/local/bin/pianopi-startup.sh
sudo chmod +x /usr/local/bin/pianopi-startup.sh

# setup environment file for python script
sudo mkdir -p /etc/pianopi/
sudo cp .env.example.local /etc/pianopi/.env # then, manually update secrets

# configure startup script to be run when system reboots
sudo cp pianopi.service /etc/systemd/system/pianopi.service
sudo systemctl daemon-reload
sudo systemctl enable pianopi.service
sudo systemctl start pianopi.service
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
