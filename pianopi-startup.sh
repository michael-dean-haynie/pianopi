#!/bin/sh

# parameters
project_directory="/pianopi"

# might be able to get rid of parts of this (enabling midi for user)
#sudo usermod -a -G audio michael
#sudo usermod -a -G audio root

# apt house-keeping
sudo apt update -y
sudo apt upgrade -y

# install dependencies from apt
sudo apt install -y vim
sudo apt install -y git
sudo apt install python3-pip -y
#sudo apt install -y nodejs
#sudo apt install -y npm

# install dependencies form pip
sudo pip install mido
sudo pip install python-rtmidi
sudo pip install websocket-client

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

# replace script in system directory and make it executable
sudo rm -rf /usr/local/bin/pianopi.py
sudo cp pianopi.py /usr/local/bin/pianopi.py
sudo chmod +x /usr/local/bin/pianopi.py

# run script
sudo /usr/local/bin/pianopi.py
