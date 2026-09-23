#!/usr/bin/python3
inp = input("Give me the number: ")
try:
    inp = int(inp)
    print("This number is an integer.")
except:
    inp = float(inp)
    print("This number is an float.")