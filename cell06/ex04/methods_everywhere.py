#!/usr/bin/env python3

import sys

class Pallino:
	def __init__(self, words):
		self.words = words

	def shrink(self, word):
		print(word[:8])

	def enlarge(self, word):
		while len(word) < 8:
			word += "z"
		print(word)



def main(arguments):
	if len(arguments) == 1:
		print("none")
	else:
		pallino = Pallino(arguments)
		for x in pallino.words[1:]:
			if len(x) > 8:
				pallino.shrink(x)
			elif len(x) < 8:
				pallino.enlarge(x)
			else:
				print(x)

if __name__ == "__main__":
	main(sys.argv)