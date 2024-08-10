#!/usr/bin/env python3

import sys

class Pallino:
    def __init__(self):
        pass

    def greetings(self, name="noble stranger"):
        print("Hello, " + name + ".")

def main():
	pallino = Pallino()
	if len(sys.argv) > 2:
		print("just one name")
	elif len(sys.argv) == 2:
		try:
			float(sys.argv[1])
		except:
			pallino.greetings(sys.argv[1])
		else:
			print("Error! It was not a name.")
	else:
         pallino.greetings()

if __name__ == "__main__":
    main()
