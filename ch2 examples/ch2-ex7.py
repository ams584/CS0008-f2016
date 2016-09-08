#
# Template for code submission
# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# description of this file goes here
# Example: Starting with Python, Chapter 1, Exercise 3

#
# Notes:
# any notes to the instructor and/or TA goes here

m = float(input("Enter the number of miles driven:"))
g = float(input("Enter the number of gallons used:"))
km = m*1.60934
l = g*3.78541
t = 100*l/km
print("Kilometers driven:", km, "Liters used:", l, "Liters per 100km:", t)
