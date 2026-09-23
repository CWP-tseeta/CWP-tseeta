#!/usr/bin/env python3

import sys

def downcase_it(string):
    return string.lower()

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
        return
    for arg in args:
        print(downcase_it(arg))

if __name__ == "__main__":
    main()