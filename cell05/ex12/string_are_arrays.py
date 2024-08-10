#!/usr/bin/env python3

import sys

count = 0
output = ""
if len(sys.argv) != 2:
	print("none")
else:
	for x in sys.argv[1]:
		found = x.find("z")
		if found > -1:
			count = count + 1
	if count > 0:
		while count:
			output += "z"
			count -= 1
		print(output)
	else:
		print("none")