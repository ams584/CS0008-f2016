# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 11
b = int(input("Enter the number of books you purchased this month:"))   #Recieves the number of books the customer purchased
p = 0   #Defines the variable points
if b >= 0 and b < 2:    #Checks what number of points to assign based on books purchased
    p = 0
elif b >= 2 and b < 4:
    p = 5
elif b >= 4 and b < 6:
    p = 15
elif b >= 6 and b < 8:
    p = 30
elif b >= 8:
    p = 60
print("You earned:", p, "points!")  #Prints the number of points