#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Ld = int(repr(number)[-1])
if Ld > 5:
    print(f"Last digit of %d is {Ld} and is greater than 5" % number)
elif Ld == 0:
    print(f"Last digit of %d is {Ld} and is 0" % number)
elif Ld < 6 and number != 0:
    print(f"Last digit of %d is {Ld} and is less than 6 and not 0" % number)
