#!/usr/bin/env python3

num = int(input("Enter number less than 25:\n"))


if num > 25:
    print("ERROR")
else:
    for i in range(25-num):
        num +=1
        print(f"Inside the loop, my variable is {num}")