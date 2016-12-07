def processData(file):
    dictionary_1 = {}   # Creates a dictionary
    n_lines = 0
    datafile = open(file, 'r')   # Opens the master file
    datafile.readline()   # Reads the master file
    for line in datafile:
        if 'distance' in line:  # Skips the header line
            continue
        n_lines += 1    # Counts the number of files in the master file
        line.rstrip('\n')   # Strips the \n from each line
        name, dist = line.split(',')    # Splits each line into the name and the distance
        if not name in dictionary_1:
            dictionary_1.append({'name': name, 'distance': float(dist)})    # Appends the name and distance for each line if it's not in the dictionary already
        return(dictionary_1, n_lines)
masterFile = input("Enter the name of the master file: ")   # Recieves the master file list
for line in masterFile:
    line.rstrip('\n')
t_dist = 0
for item in processData[0]:
    p_dist = 'distance'
    t_dist = t_dist + p_dist    # Totals the distances






