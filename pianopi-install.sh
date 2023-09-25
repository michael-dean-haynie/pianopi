#!/bin/sh

# adds this line to the /etc/rc.local file which will run the line on startup
# the line will run the pianopi-startup.sh file, log output, and fork the process to avoid blocking
sudo sed -i -e '$i sudo /usr/local/bin/pianopi-startup.sh > /opt/pianopi.log 2>&1 &' /etc/rc.local
