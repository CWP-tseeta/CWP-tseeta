#!/usr/bin/python3

password = "Python is awesome"

entry = input().strip()

if entry == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")