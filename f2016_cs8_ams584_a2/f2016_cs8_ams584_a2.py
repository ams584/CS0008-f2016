def printKV(key, value, klen = 0):  # Defines a function that formats output
    kl = max(len(key), klen)
    if isinstance(value, str):  # Tests if the value is a string
        fs = '20s'
    elif isinstance(value, float):  # Tests if the value is a float
        fs = '10.3f'
    if isinstance(value, int):  # Tests if the value is an integer
        fs = '10'
    print(format(key, str(kl)+'s'),     # Sets up the format
          format(value, fs))


def processFile(x):     # Defines a function to read a file
    n = 0
    distance_x = 0
    for line in x:      # Creates a loop that reads every line in a file
        n = n+1         # Counts the number of lines in the file
        contents = (x.readline())   # Reads an individual line
        name, distance = contents.split(',')    # Separates the line into a name and number
        if isinstance(distance, str):   # Converts the number from a string to a float
            distance = float(distance)
        distance_x = distance_x + distance  # Totals the distance for the file
    return(distance_x, n)   # Returns the total distance and number of lines for a file

t = 0
distance_total = 0
total_lines = 0
z = 1
while z != 0:   # Loops the process file function
    x = str(input("Enter the name of the file and location: "))     # Receives the file name
    if x == 'quit' or x == 'q' or x == ' ':     # Quits if the user doesn't enter a file location
        z = 0
        print("File 1: ")
        printKV("Partial Distance Run", partial_distance_2)
        printKV("Partial Number of Lines", partial_lines_2)
        print('\n')

        print("File 2: ")
        printKV("Partial Distance Run", partial_distance)
        printKV("Partial Number of Lines", partial_lines)
        print('\n')

        print("Total: ")
        printKV("Total Number of Lines", distance_total)
        printKV("Total Number of Lines", total_lines)
    else:
        x = open(x, 'r')    # Opens the file
        partial_distance, partial_lines = processFile(x)
        partial_distance_2, partial_lines_2 = processFile(x)

        distance_total = partial_distance + distance_total      # Totals the distances
        total_lines = partial_lines + total_lines       # Totals the lines

