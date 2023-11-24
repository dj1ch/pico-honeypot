#!/bin/bash
# startup script
output=$(minicom -D /dev/ttyACM0 2>&1)

if [[ $? -ne 0 && $output == "minicom: cannot open /dev/ttyACM0: No such file or directory" ]]; then
  echo "Failed to open /dev/ttyACM0. Trying /dev/ttyUSB0..."

  # try ttyUSB0
  output=$(minicom -D /dev/ttyUSB0 2>&1)

  if [[ $? -ne 0 ]]; then
    echo "Failed to open /dev/ttyUSB0 and /dev/ttyACM0. Is the device properly attached?"
    exit 1
  fi
fi

# If the script reaches this point, the command was successful
echo "Started successfully!"
