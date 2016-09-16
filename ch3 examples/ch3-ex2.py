# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 2

w1 = float(input("Enter the width of the first rectangle:"))    #Recieves the lengths and widths of the rectangles.
l1 = float(input("Enter the length of the first rectangle:"))
w2 = float(input("Enter the width of the second rectangle:"))
l2 = float(input("Enter the length of the second rectangle:"))
r1 = w1*l1  #Calculates the areas of the rectangles
r2 = w2*l2
if r1 > r2:
    print("The first rectangle's area is bigger.")  #Determines which rectangle is bigger
elif r1 < r2:
    print("The second rectangle's area is bigger.")
elif r1 == r2:
    print("The areas are the same.")