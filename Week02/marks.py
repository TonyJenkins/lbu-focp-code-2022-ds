#!/usr/bin/env python3

from statistics import mean, median, stdev

if __name__ == '__main__':

    NUMBER_OF_MARKS = 4



    print()
    print(f'Highest Mark: {max(marks)}')
    print(f'Lowest Mark:  {min(marks)}')
    print(f'Average Mark: {mean(marks):.2f}')
    print(f'Median Mark:  {median(marks):.2f}')
    print(f'Std Devn:     {stdev(marks):.2f}')
