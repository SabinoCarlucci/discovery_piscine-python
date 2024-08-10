#!/usr/bin/env python3

import sys

class Pallino:
	def __init__(self, persons):
		self.persons = persons

	def find_the_redheads(self, family):
		output = []
		for x in family.keys():
			if family[x] == "red":
				output.append(x)
		print(output)

def main():
	dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
	}
	pallino = Pallino(dupont_family)
	pallino.find_the_redheads(dupont_family)
	

if __name__ == "__main__":
	main()