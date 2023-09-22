#!/bin/sh

sudo apt update -y
sudo apt upgrade -y

sudo apt install -y vim
sudo apt install -y nodejs
sudo apt install -y npm
sudo apt install -y git

# avoid warnings about executing files from git repository
project_directory="$HOME/pianopi"
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
cd ~ || exit
sudo git clone https://github.com/michael-dean-haynie/pianopi.git

# install project dependencies
cd pianopi || exit
sudo npm install

# run project
npm start
