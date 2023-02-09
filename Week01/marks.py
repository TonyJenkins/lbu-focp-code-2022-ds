#!/usr/bin/env python3

import statistics

if __name__ == '__main__':

    mark_1 = int(input('Enter mark #1: '))
    mark_2 = int(input('Enter mark #2: '))
    mark_3 = int(input('Enter mark #3: '))
    mark_4 = int(input('Enter mark #4: '))
    mark_5 = int(input('Enter mark #5: '))

    print()
    print(max(mark_1, mark_2, mark_3, mark_4, mark_5))
    print(min(mark_1, mark_2, mark_3, mark_4, mark_5))
    print(statistics.mean([mark_1, mark_2, mark_3, mark_4, mark_5]))
