#!/bin/bash
#Script takes in the url and displays all the http methods the sever accepts
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d' ' -f2-
