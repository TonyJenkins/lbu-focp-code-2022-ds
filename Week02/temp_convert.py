#!/usr/bin/env python3

if __name__ == '__main__':

    celsius_temp = float(input('Enter a temperature in Celsius: '))
    fahr_temp = celsius_temp * (9 / 5) + 32

    print(f'{celsius_temp}C is equivalent to {fahr_temp}F.')
