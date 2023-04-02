#!/bin/bash
#The purpose of the script below is to take in a url and display the size of the body response
curl -s1 "$1" | grep "Content-Length:" | cut -d' ' -f2
