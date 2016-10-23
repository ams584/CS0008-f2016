# name       : Alexander Shepard
# email      : ams584@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, exercise 15
import random
print("Enter five test scores: ")
score1 = int(input("Enter a score: "))
score2 = int(input("Enter a score: "))
score3 = int(input("Enter a score: "))
score4 = int(input("Enter a score: "))
score5 = int(input("Enter a score: "))
def calc_average():
    avg = (score1 + score2 + score3 + score4 + score5)/5
    print("The average is: ", avg)
calc_average()
def determine_grade():
    score = int(input("Enter a test score to get a grade: "))
    if score > 100:
        score = int(input("That is not valid score. Enter different score: "))
    elif score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score <= 89:
        grade = "B"
    elif score >= 70 and score <= 79:
        grade = "C"
    elif score >= 60 and score <= 69:
        grade = "D"
    elif score < 60:
        grade = "F"
    print("That grade is a(n):", grade)
determine_grade()