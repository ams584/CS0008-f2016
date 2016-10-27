def printKV(key, value, klen = 0):
    if value is isinstance(value, float):
        klen = 10.3
    elif value is isinstance(value, int):
        klen = 10
    elif key is isinstance(key, str):
        klen = 20
    print(key, value)

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
    printKV("Partial Distance Run: ", distance_x)
    printKV("Partial Number of Lines: ", n)
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
    else:
        Y = str(input("That was not a valid input."))