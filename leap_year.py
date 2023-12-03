#!/usr/bin/python3

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
            leap = True
            print("Leap year")

    return leap

year = int(input("Enter a year: "))
result = is_leap(year)
print(result)
