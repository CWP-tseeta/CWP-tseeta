#!/usr/bin/env python3

first = float(input("Give me the first number: "))
second = float(input("Give me the second number: "))

print("Thank you!")
print(f"{first:g} + {second:g} = {first + second:g}")
print(f"{first:g} - {second:g} = {first - second:g}")
if second != 0:
    print(f"{first:g} / {second:g} = {first / second:g}")
else:
    print("Division by zero is not allowed.")
print(f"{first:g} * {second:g} = {first * second:g}")