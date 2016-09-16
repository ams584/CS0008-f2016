# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 1

n = int(input("Enter a number from 1-7:"))  #Recieves a number from the user
if n > 7 or n < 1:
    print("Number must be between 1 and 7") #Prints an error message if outside range
if n == 1:  #Determines day of week
    print("Monday")
if n == 2:
    print("Tuesday")
if n == 3:
    print("Wednesday")
if n == 4:
    print("Thursday")
if n == 5:
    print("Friday")
if n == 6:
    print("Saturday")
if n == 7:
    print("Sunday")
