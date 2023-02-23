#!/usr/bin/env python3

if __name__ == '__main__':
    students = int(input('How many students? '))
    group_size = int(input('Required group size? '))

    full_groups = students // group_size
    left_over = students % group_size

    print('There will be', full_groups, 'groups with', left_over, 'students left over.')
