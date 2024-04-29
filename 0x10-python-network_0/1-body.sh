#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response for status code 200
curl -sL "$1" -w "%{http_code}" -o /dev/null | grep -q 200 && curl -sL "$1"

