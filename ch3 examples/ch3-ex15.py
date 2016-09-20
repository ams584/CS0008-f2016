# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 15
s = float(input("Enter the number of seconds:"))    #Receives the number of seconds
m = s/60    #Calculates minutes
h = s/3600  #Calculates hours
d = s/86400 #Calculates days
if s >= 60 and s < 3600:    #Tests how many seconds there are
    print("That is the equivalent of", m, "minutes.")
elif s >= 3600 and s < 86400:
    print("That is the equivalent of", h, "hours.")
elif s >= 86400:
    print("That is the equivalent of", d, "days.")
