#!/bin/sh

curl -s $1 | grep -e "http" | cut -d '"' -f 2
