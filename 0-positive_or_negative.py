#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
if number == 0:
    print("{:d} is zero".format(number))
elif number > 0:
    print("{:d} is positive".format(number))
else:
    print("{:d} is negative".format(number))
=======
if number > 0:
    print(f"{number} is positive")
if number == 0:
    print(f"{number} is zero")
if number < 0:
    print(f"{number} is negative")
>>>>>>> 1b1fd30 (Positive anything is better than negative nothing)
