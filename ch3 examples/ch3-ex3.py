# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 3

a = int(input("Enter an age:")) #Recives an age from the user
if a <= 1:
    print("That person is an infant.")  #If the person is 1 or younger they are an infant
if a > 1 and a < 13:
    print("That person is a child.")    #If the person is between 1 and 13 they are a child
if a >= 13 and a < 20:
    print("That person is a teenager.") #If the person is 13 or older, but younger than 20 they are a teenager
if a >= 20:
    print("That person is an adult.")   #If the person is 20 or older, they are an adult