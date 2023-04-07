#!/bin/bash
# Bash script sends a request to a URL used as argument
# and show the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
