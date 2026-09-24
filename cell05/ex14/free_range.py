#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    if start > end:
        array = list(range(start, end - 1, -1))
    else:
        array = list(range(start, end + 1))
    print(array)
else:
    print("none")