#!/usr/bin/env python3

if __name__ == '__main__':
    sweets = int(input('How many sweets in the tub? '))
    pupils = int(input('How many pupils present today? '))

    sweets_per_pupil = sweets // pupils
    sweets_left_over = sweets % pupils

    print('There will be', sweets_per_pupil, 'sweets for each pupil, with', sweets_left_over, 'sweets left over.')
