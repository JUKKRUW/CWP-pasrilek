#!/usr/bin/python3
import sys

if len(sys.argv) <= 1:
    print("none")
    sys.exit()

for arg in sys.argv[1:]:
    if not arg.endswith("ism"):
        print(f"{arg}ism")
