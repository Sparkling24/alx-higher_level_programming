#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    lastDigit = number % 10
    print(lastDigit, end='')
    return lastDigit
