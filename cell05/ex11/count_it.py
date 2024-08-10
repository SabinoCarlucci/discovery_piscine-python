#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
else:
	print("parameters: " + str((len(sys.argv) - 1)))
	for x in sys.argv[1:]:
		print(x + ": " + str(len(x)))