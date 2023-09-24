# pianopi

## How to ssh into raspberrypi if ".local" DNS name is not resolving
* In a browser go to 192.168.0.1
* Login
* Go to Wireless - Access Control to see connected devices and their ips

## Raspberry Pi Installation / (Update in case of startup.sh changes)
* SSH into the raspberry pi
* Follow the `pianopi-startup.sh` script manually to
* Just need to be able to clone the repository and use vim
* Copy the `pianopi-startup.sh` script into `~` and make it executable
```shell
cd ~
cp pianopi/pianopi-startup.sh pianopi-startup.sh
chmod +x pianopi-startup.sh 
```
* With `sudo vim` add these lines to the `/etc/rc.local` file:
```shell
# pianopi startup script
sudo /home/michael/pianopi-startup.sh > /home/michael/pianopi.log 2>&1 &

# < ... exit 0 goes right below here>
```

Boom. Now rebooting the raspberry pi should automatically pull latest code form git and start the node project.

Should only need to do this again if the `piano-startup.sh` script changes.


## Information about the midi device maker/product
Bus 001 Device 009: ID 09e8:0050 AKAI  Professional M.I. Corp. MPK mini Play mk3    

## Python Attempt
```shell
sudo apt install python3-pip -y
sudo pip install mido
chmod +x midi_reader.py # get this from this git repository
./midi_reader.py
```
