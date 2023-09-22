#!/bin/sh

sudo apt update
sudo apt upgrade

sudo apt install -y vim
sudo apt install -y nodejs
sudo apt install -y npm
sudo apt install -y git

# delete the project directory if it already exists
project_directory="$HOME/pianopi"
if [ -d "$project_directory" ]; then
    echo "Deleting directory: $project_directory"
    rm -r "$project_directory"
    echo "Directory deleted."
else
    echo "Directory does not exist: $project_directory"
fi

# clone project git repository
cd ~ || exit
sudo git clone https://github.com/michael-dean-haynie/pianopi.git

# install project dependencies
cd pianopi || exit
sudo npm install

# run project
npm start
