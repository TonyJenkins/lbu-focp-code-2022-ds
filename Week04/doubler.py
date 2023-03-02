#!/usr/bin/env python3


import sys


if __name__ == '__main__':
    try:
        print(int(sys.argv[1]) * 2)
    except IndexError:
        print(f'{sys.argv[0]}: Nothing on the command-line to double.')
    except ValueError:
        print(f'{sys.argv[0]}: Data on the command-line cannot be doubled.')
