#!/usr/bin/python3
import sys
word = input("What was the parameter? ")
if len(sys.argv) > 1:
    print("Nope, sorry..." if word != sys.argv[1] else "Good job!")