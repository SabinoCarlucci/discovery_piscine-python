#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("none")
else:
	output = []
	for x in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
		output.append(x)
	print(output)