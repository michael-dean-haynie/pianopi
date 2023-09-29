#!/bin/sh

# Redirect stdout to systemd journal using a subshell
{
  file="/var/last-usb-device-event.txt"

  # Check if the PID file exists
  if [ -f "$file" ]; then
      echo "touching existing file: $file"
      sudo touch $file
  else
      echo "touching new file: $file"
      sudo touch $file
  fi

  sudo ping mbp.local -c 1
} 2>&1 | logger -t "$(basename "$0")"

