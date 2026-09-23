#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    result = ""
    for char in sys.argv[1]:
        if char == "z":
            result += "z"
    if result:
        print(result)
    else:
        print("none")
else:
    print("none")