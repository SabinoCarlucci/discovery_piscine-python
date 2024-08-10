#!/usr/bin/env python3

class Pallino:
	def __init__(self, str):
		self.str = str

	def upcase_it(self):
		print(self.str.upper())

pallino = Pallino("peppino")
pallino.upcase_it()