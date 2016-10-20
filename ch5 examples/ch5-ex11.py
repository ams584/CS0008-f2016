# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, exercise 11
import random
def quiz():
    n1 = random.randint(0, 1000)
    n2 = random.randint(0, 1000)
    print(n1, '+', n2, '= ')
    answer = int(input())
    if answer == n1 + n2:
        d = print("Congratulations! You're correct!")
    else:
        d = print("That is incorrect. The correct answer is: ", n1 + n2)
    return d
quiz()