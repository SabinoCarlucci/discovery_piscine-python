#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
print("You are currently", age, "years old")

time = 10
while time < 40:
	print("In", time, "years, you'll be", age + time, "years old.")
	time += 10