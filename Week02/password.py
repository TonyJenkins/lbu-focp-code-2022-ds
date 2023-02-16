#!/usr/bin/env python3

from time import sleep

if __name__ == '__main__':
    PASSWORD = 'cheese'

    bad_guesses = 0

    while True:
        guess = input('Enter the password: ')
        if guess == PASSWORD:
            print('Access Granted')
            break
        else:
            bad_guesses += 1
            if bad_guesses == 5:
                print('Too many attempts. System Access Blocked!')
                break
            else:
                sleep(bad_guesses)
