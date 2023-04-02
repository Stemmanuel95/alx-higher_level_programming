#!/bin/bash
#The purpose of the script below is to take in a url and display the size of the body response
$(curl -s1 "$1" | grep "Content-Length:" | wc -c) echo "Size of response: $size
bytes"
