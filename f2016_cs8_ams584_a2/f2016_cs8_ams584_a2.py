def printKV(key, value):
    if value is isinstance(value, float):
        value = format(value, '10.6f')
    elif value is isinstance(value, int):
        value = format(value, '10')
    if key is isinstance(key, str):
        key = format(key, '20s')
    print(key, ':', value)


def processFile(x):
    n = 0
    distance_x = 0
    for line in x:
        n = n+1
        contents = (x.readline())
        name, distance = contents.split(',')
        if isinstance(distance, str):
            distance = float(distance)
        distance_x = distance_x + distance
        distance_x = float(distance_x)
    printKV("Partial Distance Run", distance_x)
    printKV("Partial Number of Lines", n)
    return(distance_x)
t = 0
distance_total = 0


while t == 0:
    x = str(input("Enter the name of the file and location: "))
    x = open(x, 'r')
    variable = processFile(x)
    y = str(input("Read another file? 'y' or 'n': "))
    if y == 'y':
        distance_total = variable + distance_total
    elif y == 'n':
        distance_total = distance_total + variable
        printKV("Total Distance Run: ", distance_total)
        t = 1
    else:
        Y = str(input("That was not a valid input."))