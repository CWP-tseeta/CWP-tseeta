#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    result = string
    while len(result) < 8:
        result += 'Z'
    print(result)

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("none")
        return
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()