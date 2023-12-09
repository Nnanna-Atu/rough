#!/usr/bin/python3

from random import choice
from string import ascii_letters, digits, punctuation

length = int(input('Enter Password length: '))
chars = ascii_letters + digits + punctuation

Password = ''

for _ in range(length):
    Password += choice(chars)

print(f'Your Password is: ({Password})')
