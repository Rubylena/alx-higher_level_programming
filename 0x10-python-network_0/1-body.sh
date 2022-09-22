#!/usr/bin/bash
# script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
status=200
if [ "$response" -eq "$status" ]
then
  curl -sb -H "$1"
fi
