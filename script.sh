#!/bin/bash
# startup script
output=$(python3 shell.py 2>&1)

if [[ $? -ne 0 && "$output" == *"Traceback (most recent call last):"* ]]; then
  echo "Failed to open /dev/ttyACM0. Trying /dev/ttyUSB0..."

  # try ttyUSB0
  output=$(python3 shell_usb.py 2>&1)

  if [[ $? -ne 0 ]]; then
    echo "Failed to open /dev/ttyUSB0 and /dev/ttyACM0. Is the device properly attached?"
    exit 1
  fi
fi

# If the script reaches this point, the command was successful
echo "Started successfully!"
