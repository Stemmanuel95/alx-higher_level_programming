#!/bin/bash
#This script is to take in a url and display the size of the body response
curl -s1 "$1" | wc -c
