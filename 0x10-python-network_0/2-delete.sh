#!/bin/bash
#Script sends a delete resquest to the url passed as argument 1
curl -sX DELETE "$1"
