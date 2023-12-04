#!/usr/bin/python3
# Write a Python script which finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence (csv) on a single line.

nums = []

for i in range(1500, 3201):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(str(i))

print(','.join(nums))
