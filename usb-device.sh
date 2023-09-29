#!/bin/sh

# Specify the PID file you want to read
file="/var/last-usb-device-event.txt"

# Check if the PID file exists
if [ -f "$file" ]; then
    echo "touching existing file: $file"
    sudo touch $file
else
    echo "touching new file: $file"
    sudo touch $file
fi
