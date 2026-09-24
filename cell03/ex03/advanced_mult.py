#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 50:
        line = f"Table de {i}: "
        j = 0
        while j <= 10:
            line += str(i * j) + " "
            j += 1
        print(line.strip())
        i += 1