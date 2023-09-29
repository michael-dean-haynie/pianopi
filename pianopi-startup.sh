#!/bin/sh

# parameters
project_directory="/pianopi"

# might be able to get rid of parts of this (enabling midi for user)
sudo usermod -a -G audio michael
sudo usermod -a -G audio root
sudo usermod -a -G plugdev michael
sudo usermod -a -G plugdev root

# apt house-keeping
sudo apt update -y
sudo apt upgrade -y

# install dependencies from apt
sudo apt install -y vim
sudo apt install -y git
sudo apt install python3-pip -y
#sudo apt install -y nodejs
#sudo apt install -y npm

# avoid warnings about executing files from git repository
if [ "$(sudo git config --global --get-all safe.directory "$project_directory")"  = "$project_directory" ]; then
  echo "project directory $project_directory already exists in git config safe.directory"
else
  echo "adding project directory $project_directory to git config safe.directory"
  sudo git config --global --add safe.directory "$project_directory"
fi

# delete the project directory if it already exists
if [ -d "$project_directory" ]; then
    echo "Deleting directory: $project_directory"
    sudo rm -rf "$project_directory"
    echo "Directory deleted."
else
    echo "Directory does not exist: $project_directory"
fi

# clone project git repository
cd / || exit
sudo git clone https://github.com/michael-dean-haynie/pianopi.git
cd pianopi || exit
sudo git pull

# copy usb-device.sh script
sudo cp usb-device.sh /usr/local/bin/usb-device.sh
sudo chmod +x /usr/local/bin/usb-device.sh

# initial run of usb-device.sh script
sudo /usr/local/bin/usb-device.sh

# copy udev rules to fire script on usb device added/removed
sudo cp 99-usb-device.rules /etc/udev/rules.d/99-usb-device.rules
sudo chmod +x /etc/udev/rules.d/99-usb-device.rules
sudo udevadm control --reload-rules
sudo udevadm trigger
sudo systemctl restart systemd-udevd

# install dependencies form pip
sudo pip install -r requirements.txt

# replace script in system directory and make it executable
sudo rm -rf /usr/local/bin/pianopi.py
sudo cp pianopi.py /usr/local/bin/pianopi.py
sudo chmod +x /usr/local/bin/pianopi.py

# run script
sudo /usr/local/bin/pianopi.py 2>&1
