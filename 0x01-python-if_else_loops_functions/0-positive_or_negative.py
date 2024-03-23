#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    status = "positive"
elif number < 0:
    status = "negative"
else:
    status = "zero"

print(f"{number:d} is {status}")
