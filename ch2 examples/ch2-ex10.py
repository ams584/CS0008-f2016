#
# Template for code submission
# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 2, Exercise 10

#
# Notes:
# any notes to the instructor and/or TA goes here

s = 300     # Sugar
b = 240     # Butter
f = 330     # Flour

c = float(input("How many cookies do you want to make?"))
p = c/48    # Amount of ingredients needed in relation to the base number of ingredients

S = float(s*p)  # Amount of sugar needed
B = float(b*p)  # Amount of butter needed
F = float(f*p)  # Amount of flour needed

print("To make", c, "cookie(s), you need", S, "grams of sugar,", B, "grams of butter, and", F, "grams of flour")




