t = 0
while t == 0:
    def processFile():
        x = str(input("Enter the name of the file and location: "))
        x = open(x, 'r')
        n = 0
        for line in x:
            n = n+1
            contents = (x.readline())
            name, distance = contents.split(',')
            if isinstance(distance, str):
                distance_i = float(distance)
            print(distance_i)
        if line != '':
            print("Number of lines in file: ", n)


    processFile()