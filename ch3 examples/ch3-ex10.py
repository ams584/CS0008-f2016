# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 10
print("Enter the number of coins to make 1 dollar") #Gives instructions to user
nquarters = int(input("Enter the number of quarters:"))
ndimes = int(input("Enter the number of dimes:"))
nnickels = int(input("Enter the number of nickels:"))
npennies = int(input("Enter the number of pennies:"))
quarter = .25   #Assigns the value of a quarter
dime = .10      #Assigns the value of a dime
nickel = .05    #Assigns the value of a nickel
penny = .01     #Assigns the value of a penny
valquarters = nquarters*quarter #Calculates the value of the number of quarters entered
valdimes = ndimes*dime  #Calculates the value of the number of dimes entered
valnickels = nnickels*nickel    #Calculates the value of the number of nickels entered
valpennies = npennies*penny #Calculates the value of the number of pennies entered
if valquarters + valdimes + valnickels + valpennies == 1.00:    #Checks the value of the coins entered
    print("This equals $1!")
elif valquarters + valdimes + valnickels + valpennies > 1.00:
    print("This is greater than $1!")
elif valquarters + valdimes + valnickels + valpennies < 1.00:
    print("This is less than $1!")
