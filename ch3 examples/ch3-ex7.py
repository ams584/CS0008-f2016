w = 1
while w < 2:
    c1 = str(input("Enter the first color:"))   #Recieves the first two colors
    c2 = str(input("Enter the second color:"))
    if c1 == "red" or c1 == "yellow" or c1 == "blue":   #Checks if the first color is primary
        if c2 == "red" or c2 == "yellow" or c2 == "blue":   #Checks if the second color is primary
            if c1 == "red" and c2 == "blue" or c1 == "blue" and c2 == "red":    #Checks if the combination makes purple
                print("This combination makes purple.")
            elif c1 == "red" and c2 == "yellow" or c1 == "yellow" and c2 == "red":  #Checks if the combination makes orange
                print("This combination makes orange.")
            elif c1 == "yellow" and c2 == "blue" or c1 == "blue" and c2 == "yellow":    #Checks if the combination makes green
                print("This combination makes green.")
            if c1 == c2:    #Checks if both colors are the same
                print("These are both the same color!")
        else:   #Error message if the second color is not primary
            print("The second color is not a primary color.")
    else:   #Error message if the first color is not primary
        print("The first color is not a primary color.")
        if c2 == "red" or c2 == "yellow" or c2 == "blue":   #Checks the second color if the first is not primary
            continue
        else:
            print("The second color is not a primary color.")

