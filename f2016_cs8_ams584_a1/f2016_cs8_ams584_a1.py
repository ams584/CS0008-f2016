# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 12

units = str(input("Would you like to use USC or Metric?"))
if units == "USC":
    miles = float(input("Enter the number of miles driven:"))
    gallons = float(input("Enter the number of gallons used:"))
    mpg = miles/gallons
    kilometers = miles*1.60934
    liters = gallons*3.78541
    lkm = 100*liters/kilometers

elif units == "Metric":
    kilometers = float(input("Enter the number of kilometers driven:"))
    liters = float(input("Enter the number of liters used:"))
    lkm = 100*liters/kilometers
    miles = kilometers*.621371
    gallons = liters*.264172
    mpg = miles/gallons

if lkm > 20:
    cc = "Extremely Poor"
elif lkm > 15 and lkm <= 20:
    cc = "Poor"
elif lkm > 10 and lkm <= 15:
    cc = "Average"
elif lkm > 8 and lkm <= 10:
    cc = "Good"
elif lkm <= 8:
    cc = "Excellent"

print("                     USC:     ", "       Metric:")
print("Distance_____:  ",   format(miles, 3),   format(kilometers, 3))
print("Gas____:        ",   format(gallons, 3), format(liters, 3))
print("Consumption____:",   format(mpg, 3), "", format(lkm, 3))
print("Gas Consumption Rating:", cc)
