#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")