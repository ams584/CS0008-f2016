def main():
    def processFile():
        x = str(input("Enter the name of the file and location: "))
        x = open(x, 'r')
        n = 0
        distance_x = 0
        for line in x:
            n = n+1
            contents = (x.readline())
            name, distance = contents.split(',')
            if isinstance(distance, str):
                distance = float(distance)
            distance_x = distance_x + distance
        print(distance_x)
        return(distance_x)
    t = 0
    distance_total = 0
    while t == 0:
        variable = processFile()
        y = str(input("Read another file? 'y' or 'n': "))
        if y == 'y':
            distance_total = variable + distance_total
        elif y == 'n':
            distance_total = distance_total + variable
            print("Total distance run: ", variable)
            print(distance_total)
        else:
            Y = str(input("That was not a valid input."))
main()