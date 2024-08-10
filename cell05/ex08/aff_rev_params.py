#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("none")
else:
	for x in reversed(sys.argv[1:]):
		print(x)

	#count = len(sys.argv)


	#while count > 1:
	#	print(sys.argv[count - 1])
	#	count -= 1