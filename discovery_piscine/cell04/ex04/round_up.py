#!/usr/bin/python3

import math

inp = input("Give me the number: ")
try:
    inp = int(inp)
    print(math.ceil(inp))
except:
    inp = float(inp)
    print(math.ceil(inp))
