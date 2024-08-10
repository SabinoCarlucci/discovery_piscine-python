#!/usr/bin/env python3

import sys

class Pallino:
	def __init__(self):
		pass

	def famous_births(self, women_scientists):
		out = list(women_scientists.items())
		out = sorted(out, key= lambda x:x[1]['date_of_birth'])
		for elem in out:
			print(f"{elem[1]['name']} is a great scientist bron in {elem[1]['date_of_birth']}")

		

def main():
	women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
	}
	pallino = Pallino()
	pallino.famous_births(women_scientists)
	
	

if __name__ == "__main__":
	main()