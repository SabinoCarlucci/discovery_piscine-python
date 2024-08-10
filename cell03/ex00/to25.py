#!/usr/bin/env python3

usr_input = int(input("Enter a number less than 25\n"))

if usr_input > 25:
	print("Error")

while usr_input <= 25:
	print("Inside the loop, my variable is", usr_input)
	usr_input += 1