t = 0
while t == 0:
    def processFile():
        x = str(input("Enter the name of the file and location: "))
        x = open(x, 'r')
        n = 0
        distance_total = 0
        for line in x:
            n = n+1
            contents = (x.readline())
            name, distance = contents.split(',')
            if isinstance(distance, str):
                distance = float(distance)
            distance_total = distance_total + distance
        c = 0
        while c == 0:
            y = str(input("Read another file? 'y' or 'n': "))
            if y == 'n':
                t = 1
                c = 1
                print("File to be read: ", x)
                if line != '':
                    print("Number of lines in file: ", n)
                print("Total distance run: ", distance_total)
            elif y == 'y':
                t = 0
                c = 1
            else:
                c = 0
                Y = str(input("That was not a valid input."))
    processFile()

