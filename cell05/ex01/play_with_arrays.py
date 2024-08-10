#!/usr/bin/env python3

or_array =  [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

def main():
	for x in or_array:
		new_array.append(x + 2)

	print("Original array: ", or_array)
	print("New array: ", new_array)

if __name__=="__main__":
	main()