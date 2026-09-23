#!/usr/bin/python3
import sys

count = 0
if len(sys.argv) == 2:
    for i in sys.argv[1]:
        if i == 'z':
            count += 1
    if count != 0:
        print("z" * count)
    else:
        print("none")
else:
    print("none")
