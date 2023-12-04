#!/usr/bin/python3

words = input("Enter some words: ")
print(words)
word_list = words.split(" ")
output = reversed(word_list)
for i in output:
    print(i, end=" ")
print()
