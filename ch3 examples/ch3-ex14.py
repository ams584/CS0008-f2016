# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, exercise 14
w = int(input("Enter your weight in pounds:"))    #Recieves the users weight
h = int(input("Enter your height in inches:"))    #Recieves the users height
bmi = 703 / (h ^ 2) * w #Calculates the users BMI
if bmi < 18.5:  #Determines if the user is overweight, underweight, or has an optimal weight based on their BMI
    print("Your BMI is:", bmi, "You are underweight.")
elif bmi >= 18.5 and bmi <= 25:
    print("Your BMI is:", bmi, "Your weight is optimal.")
elif bmi > 25:
    print("Your BMI is:", bmi, "You are overweight.")