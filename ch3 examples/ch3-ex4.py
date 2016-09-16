# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 4

n = int(input("Enter a number between 1 and 10:")) #Askes for a number between 1 and 10
if n < 1 or n > 10:
    print("The number must be between 1 and 10.") #Error message if the number is not in range

#Displays the correct roman numerals.
elif n == 1:
    print("I")
elif n == 2:
    print("II")
elif n == 3:
    print("III")
elif n == 4:
    print("IV")
elif n == 5:
    print("V")
elif n == 6:
    print("VI")
elif n == 7:
    print("VII")
elif n == 8:
    print("VIII")
elif n == 9:
    print("IX")
elif n == 10:
    print("X")
