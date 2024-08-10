#!/usr/bin/env python3

import sys

base = 0

while base < 11:
	if  len(sys. argv) > 1:
		print("none")
		break
	
	mult = 0
	table = ""
	while mult < 11:
		res = base * mult
		table += str(res) + " "
		mult += 1
	print("Table de", base, ":", table)
	base += 1