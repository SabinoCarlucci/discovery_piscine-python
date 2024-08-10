#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
	print("none")
else:
	matches = len(re.findall(sys.argv[1], sys.argv[2]))
	if matches == 0:
		print("none")
	else:
		print(matches)