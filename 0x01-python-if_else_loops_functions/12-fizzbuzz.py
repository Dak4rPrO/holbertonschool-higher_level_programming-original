#!/usr/bin/python3
def fizzbuzz():
    for i in range((1), (101)):
        if (i % 15) == 0:
            i += 1
            print(f"FizzBuzz", end=" ")

        elif (i % 3) == 0:
            i += 1
            print(f"Fizz", end=" ")

        elif (i % 5) == 0:
            i += 1
            print(f"Buzz", end=" ")

        else:
            print(f'{i}', end=" ")
