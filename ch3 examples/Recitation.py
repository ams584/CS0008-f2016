l = 0
while l<1: #loops program
    n = float(input("Enter a number:"))
    if (n > 0):
        a = n * 3 #multiplies by 3 if input is greater than zero
    elif (n == 0):
        a = str("What a cool number!") #prints this if input is zero
    elif (n < 0):
        a = n + 5  #adds 5 if input is less than zero
    print(a)