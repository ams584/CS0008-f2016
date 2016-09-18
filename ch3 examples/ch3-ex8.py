import math
people = int(input("Enter the number of people attending:"))    #Recieves the number of people attending
hdogs = int(input("Enter the number of hot dogs per person:"))  #Receives the number of hot dogs per person
hp = people*hdogs   #Calculates the number of hot dogs
h = (math.ceil(hp/10)) #Calculates the minimum number of hot dog packages
b = (math.ceil(hp/8)) #Calculates the minimum number of bun packages
hdogsleft = h*10-hp #Calculates the number of hot dogs left
bunsleft = b*8-hp   #Calculates the number of buns left
print("Packages of hot dogs required:", h, "Packages of buns required:", b, "Leftover hot dogs:", hdogsleft, "Leftover buns:", bunsleft)