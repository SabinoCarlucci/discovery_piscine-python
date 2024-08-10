#!/usr/bin/env python3

base = int(input("Enter a number\n"))

mult = 0
while mult < 10:
	print(mult, "x", base, "=", (mult * base))
	mult += 1