#!/usr/bin/env python3

from statistics import mean, median, stdev

if __name__ == '__main__':

    NUMBER_OF_MARKS = 4

    marks = []

    for counter in range(NUMBER_OF_MARKS):
        while True:
            next_mark = int(input(f'Enter mark #{counter + 1}: '))
            if 0 <= next_mark <= 100:
                break
            else:
                print('Mark out of range. Must be between 0 and 100.')

        marks.append(next_mark)

    print()
    print(f'Highest Mark: {max(marks)}')
    print(f'Lowest Mark:  {min(marks)}')
    print(f'Average Mark: {mean(marks):.2f}')
    print(f'Median Mark:  {median(marks):.2f}')
    print(f'Std Devn:     {stdev(marks):.2f}')
