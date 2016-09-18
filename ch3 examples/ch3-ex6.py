# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 6
month = int(input("Enter the month in number form:"))   #Asks for input for the month, day, and year
day = int(input("Enter the day of the month:"))
year = int(input("Enter the year in two digits:"))

if month * day == year:     #Determines if the month times the day equals the year
    print("This date is magic!")
else:
    print("This date is not magic!")