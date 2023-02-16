#!/usr/bin/env python3

if __name__ == '__main__':

    numbers = []

    while True:
        number = input('Enter a number: ')
        if not number:
            break
        else:
            numbers.append(int(number))

    print(f'You entered {len(numbers)} numbers.')
