#!/usr/bin/python3

for n in range(1500, 3201):
    if n % 7 == 0 and n % 5 != 0:
        print(n, end=",")
