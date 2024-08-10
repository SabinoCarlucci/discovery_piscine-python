#!/usr/bin/env python3

import sys

class Pallino:
	def __init__(self):
		self.str = sys.argv

	def downcase_it(self):
		if len(sys.argv) == 1:
			print("none")
		for x in self.str[1:]:
			print(x.lower())

pallino = Pallino()
pallino.downcase_it()
