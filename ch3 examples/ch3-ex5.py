# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 5

m = float(input("Enter the objects mass in newtons:")) #Askes for an objects weight
w = m*9.8   #Calculates weight
if m > 500:
    print("The object is too heavy.")   #Error message if the object is too heavy
elif m < 100:
    print("The object is too light.")   #Error message if the object is too light
else:
    print("The weight of the object is:", w)    #Prints the weight of the object
