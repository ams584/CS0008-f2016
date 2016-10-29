def printKV(key, value, klen = 0):
    kl = max(len(key), klen)
    if isinstance(value, str):
        fs = '20s'
    elif isinstance(value, float):
        fs = '10.3f'
    if isinstance(value, int):
        fs = '10'
    print(format(key, str(kl)+'s'),
          format(value, fs))


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
    return(distance_x, n)

t = 0
distance_total = 0
total_lines = 0
z = 1
while z != 0:
    x = str(input("Enter the name of the file and location: "))
    if x == 'quit':
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
    if x != 'quit':
        x = open(x, 'r')
        partial_distance, partial_lines = processFile(x)
        partial_distance_2, partial_lines_2 = processFile(x)

        distance_total = partial_distance + distance_total
        total_lines = partial_lines + total_lines

