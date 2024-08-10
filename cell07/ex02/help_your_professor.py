#!/usr/bin/env python3

import sys

class Pallino:
	def __init__(self):
		pass

	def average(self, class_name):
		students = 0
		scores = 0
		for x in class_name.keys():
			scores += class_name[x]
			students += 1
		average_score = scores / students
		return average_score

def main():
	class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
	}
	class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13
	}
	pallino = Pallino()
	print(f"Average for class 3B: {pallino.average(class_3B)}.")
	print(f"Average for class 3C: {pallino.average(class_3C)}.")

	

if __name__ == "__main__":
	main()