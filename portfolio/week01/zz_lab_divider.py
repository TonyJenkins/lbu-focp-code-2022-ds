#!/usr/bin/env python3

def labs_needed(student_count, lab_size=24):
    full_labs = student_count // lab_size
    extra_lab = 0 if student_count % lab_size == 0 else 1

    return full_labs + extra_lab


if __name__ == '__main__':

    for students in [113, 175, 12]:
        print(f'{students:3} students need {labs_needed(students)} lab{"" if labs_needed(students) == 1 else "s"}.')
