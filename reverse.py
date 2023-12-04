#!/usr/bin/python3

# Function to print reverse of words given
# Discovered this on my Birthday: 04-12-2023

words = input("Enter words here: ")
# This splits the input strings into lists
splits = words.split()
# Notice that the [i] near the slicing handles the rows
for i in range(len(splits)):
    splits[i] = splits[i][::-1]
# Notice that I reversed using slicing the second time
# This is because the first word reverses words alone
# but the second reversed slicing reversed the whole sentence

splits = splits[::-1]
# joining the list into strings
output = ' '.join(splits)
print(output)
