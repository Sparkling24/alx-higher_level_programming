#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = -lastDigit

if lastDigit == 0:
    print(f"Last digit of {number:d} is {lastDigit:d} and is 0")
elif lastDigit > 5:
    print(f"Last digit of {number:d} is {lastDigit:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {lastDigit:d} and\
 is less than 6 and not 0")
