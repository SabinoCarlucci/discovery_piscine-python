#!/usr/bin/env python3

arrest_command = "STOP"

message = input("What you gotta say? : ")

while 1:
	if message == arrest_command:
		break
	message = input("I got that! Anything else? : ")