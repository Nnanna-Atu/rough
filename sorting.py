#!/usr/bin/python3

words = input("Enter hyphen-separated words: ")

split = words.split("-")

sort = '-'.join(sorted(split)).title()
print(sort)

