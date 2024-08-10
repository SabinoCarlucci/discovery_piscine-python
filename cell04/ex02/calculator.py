#!/usr/bin/env python3

import math

def format_number(num):
    if num.is_integer():
        return int(num)
    else:
        return num

first = float(input("Give me the first number: "))
second = float(input("Give me the second number: "))

print("Thank you!")

result = first + second
print(f"{format_number(first)} + {format_number(second)} = {format_number(result)}")

result = first - second
print(f"{format_number(first)} - {format_number(second)} = {format_number(result)}")

result = first / second
print(f"{format_number(first)} / {format_number(second)} = {format_number(result)}")

result = first * second
print(f"{format_number(first)} * {format_number(second)} = {format_number(result)}")
