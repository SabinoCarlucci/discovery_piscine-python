#!/usr/bin/env python3

or_array =  [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
this_set = set()

def main():
	for x in or_array:
		if x > 5:
			y = x + 2
			new_array.append(y)
			this_set.add(y)

	print(or_array)
	print(this_set)

if __name__=="__main__":
	main()