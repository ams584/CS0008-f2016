w = float(input("Enter the weight of the package:"))    #Recieves the weight of the package
c = 0   #Deifines the cost variable
if w <= 2:  #Determines the cost of shipping based on the weight of the package
    c = 1.50
elif w > 2 and w < 6:
    c = 3.00
elif w > 6 and w < 10:
    c = 4.00
elif w > 10:
    c = 4.75
print("The cost of shipping is:", c, "dollars.")