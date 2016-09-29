# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 12

units = str(input("Would you like to use USC or Metric? "))                  # Asks for the user to select USC or Metric
if units == "USC":                                                          # Runs if the user selected usc
    miles = float(input("Enter the number of miles driven: "))               # Receives the number of miles
    gallons = float(input("Enter the number of gallons used: "))             # Receives the number of gallons
    mpg = miles/gallons
    kilometers = miles*1.60934                                              # Converts miles to kilometers
    liters = gallons*3.78541                                                # Converts gallons to liters
    lkm = 100*liters/kilometers                                             # Calculates liters per 100 km

elif units == "Metric":                                                     # Runs if the user selects Metric
    kilometers = float(input("Enter the number of kilometers driven: "))     # Receives the number of kilometers
    liters = float(input("Enter the number of liters used: "))               # Receives the number of liters
    lkm = 100*liters/kilometers                                             # Calculates liters per 100 km
    miles = kilometers*.621371                                              # Converts kilometers to miles
    gallons = liters*.264172                                                # Converts liters to gallons
    mpg = miles/gallons                                                     # Calculates miles per gallon

if lkm > 20:                                                                # Tests the number of liters used
    cc = "Extremely Poor"
elif lkm > 15 and lkm <= 20:
    cc = "Poor"
elif lkm > 10 and lkm <= 15:
    cc = "Average"
elif lkm > 8 and lkm <= 10:
    cc = "Good"
elif lkm <= 8:
    cc = "Excellent"

print("                   USC:", "     Metric:")                                    # Displays the titles
print("Distance_____:",   format(miles, '10.3f'), format(kilometers, '10.3f'))      # Displays the distances
print("Gas__________:",    format(gallons, '10.3f'), format(liters, '10.3f'))       # Displays the amount of gas
print("Consumption__:",   format(mpg, '10.3f'), format(lkm, '10.3f'))               # Displays gas used over distance
print("Gas Consumption Rating:", cc)                                                # Displays consumption rating
