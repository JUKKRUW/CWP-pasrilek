#!/usr/bin/python3

inp = input()

for i in inp:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
        