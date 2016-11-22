#
# MN: header with user, instructor and course info is missing
#


# MN: could you please not use inline comments
def printKV(key, value, klen = 0):  # Defines a function that formats output
    kl = max(len(key), klen)
    if isinstance(value, str):  # Tests if the value is a string
        fs = '10s'
    elif isinstance(value, float):  # Tests if the value is a float
        fs = '10.3f'
    if isinstance(value, int):  # Tests if the value is an integer
        fs = '10'
    print(format(key, str(kl)+'s'),     # Sets up the format
          format(value, fs))


# MN: could you please not use inline comments
def processFile(x):     # Defines a function to read a file
    partial_lines = 0
    partial_distance = 0
    for line in x:      # Creates a loop that reads every line in a file
        partial_lines = partial_lines+1         # Counts the number of lines in the file
        contents = (x.readline())   # Reads an individual line
        contents.rstrip('\n')   # Removes the \n from the line
        name, distance = contents.split(',')    # Separates the line into a name and number
        if isinstance(distance, str):   # Converts the number from a string to a float
            distance = float(distance)
        partial_distance = partial_distance + distance  # Totals the distance for the file
    printKV("Partial Distance Run", partial_distance)   # Prints partial distance
    printKV("Partial Number of Lines", partial_lines)   # Prints partial number of lines
    print('\n')     # Prints a blank line
    x.close()       # Closes the file
    return(partial_distance, partial_lines)   # Returns the total distance and number of lines for a file

t = 0
distance_total = 0
total_lines = 0
z = 1
while z != 0:   # Loops the process file function
    x = str(input("Enter the name of the file and location, or enter 'q', 'quit', or 'space' to quit: "))# Receives the file name
    print("\n")
    if x == 'quit' or x == 'q' or x == ' ':     # Quits if the user doesn't enter a file location
        z = 0
        print('\n')
        print("File to be read:", x)
        print("Total: ")
        printKV("Total Number of Lines", distance_total)    # Prints the total distances
        printKV("Total Number of Lines", total_lines)       # Prints the total number of lines
    else:
        print("File to be read:", x)
        x = open(x, 'r')    # Opens the file
        partial_distance, partial_lines = processFile(x)
        distance_total = partial_distance + distance_total      # Totals the distances
        total_lines = partial_lines + total_lines       # Totals the lines

