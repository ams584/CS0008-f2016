# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, exercise 12
def max():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    if n1 > n2:
        max = n1
    elif n2 > n1:
        max = n2
    else:
        print("These values are equal.")
    print(max, "is greater.")
    return max
max()