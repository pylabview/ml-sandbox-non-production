#!/bin/sh

# 1. Check if the user actually type a file
if [ -z "$1" ]; then
  echo "Error: No file or directory name provided."
  echo "Usage: $0 <name>"
  exit 255
fi

FILE_NAME="$1"

# Check if this is an actually file

if [ -f "$FILE_NAME"  ]
then
    echo "$FILE_NAME is a regular file "
    exit 0

elif [ -d "$FILE_NAME"  ]
then 
    echo "$FILE_NAME is a DIR"
    exit 1
else
    echo "$FILE_NAME is not a file or DIR"
    exit 2
fi

