#!/usr/bin/env python3

def divide_students(student_number, number_in_group):
    return student_number // number_in_group, student_number % number_in_group


def labs_needed(student_number, number_in_group):
    groups, spares = divide_students(student_number, number_in_group)

    return groups if spares == 0 else groups + 1


if __name__ == '__main__':

    while 1:
        try:
            students = int(input('How many students? '))
            if students < 0:
                print('Error: Number of students cannot be negative.')
            else:
                break

        except ValueError:
            print('Error: Integer needed here.')

    if students > 0:

        while 1:
            try:
                group_size = int(input('Required group size? '))

                if group_size >= 0:

                    labs = labs_needed(students, group_size)
                    print(f'There should be {labs} lab{"" if labs == 1 else "s"}.')

                    break
                else:
                    print('Error: Group size cannot be negative.')

            except ValueError:
                print('Error: Integer needed here.')
            except ZeroDivisionError:
                print('Error: Group size cannot be zero.')

    else:
        print('No students, so no labs needed.')
