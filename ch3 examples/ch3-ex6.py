month = int(input("Enter the month in number form:"))   #Asks for input for the month, day, and year
day = int(input("Enter the day of the month:"))
year = int(input("Enter the year in two digits:"))

if month * day == year:     #Determines if the month times the day equals the year
    print("This date is magic!")
else:
    print("This date is not magic!")