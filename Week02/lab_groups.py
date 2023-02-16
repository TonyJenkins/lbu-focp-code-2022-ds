#!/usr/bin/env python3

if __name__ == '__main__':

    while True:
        number_of_students = int(input('Enter number of students: '))
        if number_of_students > 0:
            break
        else:
            print('Invalid number of students. Try again!')

    while True:
        group_size = int(input('Enter required group size: '))
        if group_size > 1:
            break
        else:
            print('Invalid group size. Try again!')

    full_groups = number_of_students // group_size
    left_over = number_of_students % group_size

    print(f'There will be {full_groups} full groups, with {left_over} in a left over group.')
