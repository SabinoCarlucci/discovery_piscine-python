#!/usr/bin/env python3

import sys

check = "ism"

if len(sys.argv) == 1:
	print("none")
else:
	for x in sys.argv[1:]:
		if x.find(check) > -1:
			continue
		else:
			output = x + check
			print(output)