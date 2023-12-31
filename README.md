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
scp /Users/michael/certs/ca.crt michael@pianopi.local:/home/michael/ca.crt

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

# add useful pp (pianopi) aliases
sudo -- sh -c "echo \"alias ppstart='sudo systemctl start pianopi.service'\" >> /home/michael/.profile"
sudo -- sh -c "echo \"alias ppstop='sudo systemctl stop pianopi.service'\" >> /home/michael/.profile"
sudo -- sh -c "echo \"alias pprestart='sudo systemctl restart pianopi.service'\" >> /home/michael/.profile"
sudo -- sh -c "echo \"alias ppreload='sudo systemctl daemon-reload'\" >> /home/michael/.profile"
sudo -- sh -c "echo \"alias ppstatus='sudo systemctl status pianopi.service'\" >> /home/michael/.profile"
sudo -- sh -c "echo \"alias ppjournal='sudo journalctl -f -n 100 -u pianopi.service'\" >> /home/michael/.profile"
source /home/michael/.profile

# pull code from github
cd ~
sudo git clone https://github.com/michael-dean-haynie/pianopi.git
cd pianopi

# copy startup script to system directory
sudo cp pianopi-startup.sh /usr/local/bin/pianopi-startup.sh
sudo chmod +x /usr/local/bin/pianopi-startup.sh

# setup environment file for python script ###### MANUAL STEP HERE ###############
sudo mkdir -p /etc/pianopi/
sudo cp .env.example.local /etc/pianopi/.env # then, manually update secrets

# configure startup script to be run when system reboots
sudo cp pianopi.service /etc/systemd/system/pianopi.service
sudo systemctl daemon-reload
sudo systemctl enable pianopi.service
sudo systemctl start pianopi.service
```

* reboot the raspberry pi `sudo reboot`
* see the section on installing cert authority for local network ssl
* see the section firewall settings for the mac so pi can connect without having ssh'ed from mpb to pi

## Firewall settings for the mac so pi can connect without having ssh'ed from mpb to pi
* Mac > System Preferences > Security & Privacy > Firewall Advanced > Add item to list
  * in finder go to `/usr/local/bin` to select the node application


## Information about the midi device maker/product
Bus 001 Device 009: ID 09e8:0050 AKAI  Professional M.I. Corp. MPK mini Play mk3    

## Temp Debugging Reference
[Errno 113] No route to host - reconnect
Sep 29 11:19:07 pianopi pianopi-startup.sh[1222]: Calling custom dispatcher reconnect [8 frames in stack]