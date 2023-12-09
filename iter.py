#!/usr/bin/python3

if __name__ == '__main__':
    while 1:
        n = input('Enter length: ')
        if n == 'end':
            break
        if n.isalpha():
            print('Sorry, enter a digit.')
        else:
            n = int(n)
            total = 0
            for i in range(1, n + 1):
                print(i, end=", ")
                total += i
            print(f'\nTotal: {total}')
