#!/usr/bin/env python3

from statistics import mean


def valid_mark(m):
    if 0 <= m <= 100:
        return True
    else:
        return False


def read_marks():
    marks = []

    while True:
        next_mark = input(f'Enter next mark: ')
        if not next_mark:
            break
        else:
            if valid_mark(int(next_mark)):
                marks.append(int(next_mark))
            else:
                print('Error. Invalid number. Ignoring.')

    return marks


def get_results(list_of_marks):
    return max(list_of_marks), min(list_of_marks), mean(list_of_marks)


def get_letter_grade(avg_mark):
    if avg_mark >= 70:
        return 'A'
    elif avg_mark >= 60:
        return 'B'
    elif avg_mark >= 50:
        return 'C'
    elif avg_mark >= 40:
        return 'D'
    else:
        return 'F'


def print_results(max_mark, min_mark, avg_mark, letter_grade):
    print()
    print(f'Highest Mark: {max_mark}')
    print(f'Lowest Mark:  {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')
    print()
    print(f'Overall Grade: {letter_grade}')


if __name__ == '__main__':

    marks = read_marks()   # Read the marks.

    max_mark, min_mark, avg_mark = get_results(marks)
    letter_grade = get_letter_grade(avg_mark)

    print_results(max_mark, min_mark, avg_mark, letter_grade)
