#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"

# Make a request to the server with a specific header
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

