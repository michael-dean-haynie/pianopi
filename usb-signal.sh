#!/bin/sh

# Specify the PID file you want to read
pid_file="/var/pianopi.pid"

# Check if the PID file exists
if [ -f "$pid_file" ]; then
    # Read the PID from the PID file and store it in a variable
    read -r pid < "$pid_file"
    echo "PID read from $pid_file: $pid"
    sudo kill -USR1 "$pid"
else
    echo "PID file not found: $pid_file"
fi
