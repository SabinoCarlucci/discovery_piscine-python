#!/usr/bin/env python3

import sys

class Pallino:
	def __init__(self, persons):
		self.persons = persons

	def array_of_names(self, persons):
		guy = ""
		output = []
		for x in persons.keys():
			guy = x.capitalize() + " " + persons[x].capitalize()
			output.append(guy)
		print(output)

def main():
	persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier",
	"ciccio": "pasticcio",
	"mario": "rossi"
	}
	pallino = Pallino(persons)
	pallino.array_of_names(persons)
	

if __name__ == "__main__":
	main()