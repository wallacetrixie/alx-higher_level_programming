#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response

# Check if filename argument is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Check if file exists
if [ ! -f "$2" ]; then
    echo "File '$2' does not exist"
    exit 1
fi

# Check if file contains valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with JSON content
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

