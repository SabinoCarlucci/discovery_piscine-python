#!/usr/bin/env python3

input_string = input()
output_string = ""

for x in input_string:
	if x.isupper():
		output_string += x.lower()
	else:
		output_string += x.upper()

print(output_string)