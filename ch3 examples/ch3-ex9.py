# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 9
number = input('Give me a number from 0 to 36:')
number = int(number)
if number < 0 and number > 36: #If the number is out of range of 0 and 36
    print("Give me a number in range:")
if number == 0:
    color = "Green"
elif number > 0 and number <= 10:
    if number %2 == 0:
        color = "Black"
    else:
        color = "Red"
elif number >= 11 and number <= 18:
    if number %2 == 0:
        color = "Red"
    else:
        color = "Black"
print(color)