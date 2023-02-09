#!/usr/bin/env python3

import statistics

if __name__ == '__main__':

    temp_8am = int(input('Enter 8am Temp:  ')[:-1])
    temp_11am = int(input('Enter 11am Temp: ')[:-1])
    temp_2pm = int(input('Enter 2pm Temp:  ')[:-1])
    temp_5pm = int(input('Enter 5pm Temp:  ')[:-1])
    temp_8pm = int(input('Enter 8pm Temp:  ')[:-1])

    max_temp = max(temp_8am, temp_11am, temp_2pm, temp_5pm, temp_8pm)
    min_temp = min(temp_8am, temp_11am, temp_2pm, temp_5pm, temp_8pm)

    print()
    print(f'Max Temp: {max_temp}C')
    print(f'Min Temp: {min_temp}C')
    print(f'Range:    {max_temp - min_temp}')
    print(f'Avg Temp: {statistics.mean([temp_8am, temp_11am, temp_2pm, temp_5pm, temp_8pm])}')
