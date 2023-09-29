#!/bin/sh

# Specify the PID file you want to read
file="/var/last-usb-device-event.txt"

# Check if the PID file exists
if [ -f "$file" ]; then
    echo "touching file: $file"
    sudo touch $file
else
    echo "file not found: $file"
fi
