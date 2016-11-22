# Have mercy

master_file_list = input("Enter the location of the file list: ")   # Requests the location of the master file list
global_dictionary = {}      # Creates an emptry dictionary
def processfile(master_file_list, dictionary):      # Defines the main file reading function
    contents_mfl = open(master_file_list, 'r')      # Opens the master file list
    length_mfl = 0
    length_files = []       # Creates an empty list
    for line in contents_mfl:       # Reads every line in the master file list
        length_files.append(0)      # Creates a new spot in the list
        length_mfl+=1       # Makes a counter to total the number of files in the master file list
        filename = line.rstrip('\n')        # Strips the \n
        x = open(filename, 'r')     # Opens each individual data file
        x.readline()        # Reads the data file
        t_dist = 0
        for line in x:
            length_files[length_mfl-1] += 1     # Makes a counter that counts the total number of lines throughout every data file
            z = 0
            line = line.rstrip('\n')        # Strips the \n
            name, dist = line.split(',')    # Splits each line into name and distance
            p_dist = float(dist)
            t_dist += p_dist           # Totals the distance
            dictionary = {}
            if name in dictionary:
                z = 1
                dictionary.append(dist)     # Appends a name if it appears more than once
                print(dictionary)
            else:
                dictionary = name, dist
                print(dictionary)
    return(dictionary, t_dist, length_mfl, length_files, z, dist, name)     # Returnes the values needed

output = processfile(master_file_list, global_dictionary)
max_name = ' '
max_dist = 0
name, dist = output[0]
for name in output[0]:
    l_values = float(dist)      # Searches the dictionary for the max distance of each name
    if l_values > max_dist:     # Tests which value is greater if there is more than one value for distance per name
        max_dist = l_values
        max_name = name
min_name = ' '
min_dist = 0
for name in output[0]:      # Does the same thing as for the max distance run
    x_values = float(dist)
    if (x_values < min_dist):
        min_dist = x_values
        min_name = name
for dist in output[0]:
    times_participated = 0      # Counts the number of times each person participated
    times_participated += 1
    times_participated = str(times_participated)
total_participants = len(global_dictionary)
print("Number of input files read       :",output[2])       # Prints everything
print("Number of lines read             :",output[3])
print("\n")
print("Total Distance                   :",output[1])
print("\n")
print("Max Distance Run                 :",max_dist)
print("  by participant                 :",max_name)
print("\n")
print("Min Distance Run                 :",min_dist)
print("  by participant                 :",min_name)
print("Total Number of Participants     :",total_participants)

output_file = open('f2016_cs8_ams584_a3.data.output.csv', 'w')      # Creates the output file
for name in output:
    output_file.write(output[6])        # Writes to the output file for each name
    output_file.write(',')
    output_file.write(times_participated)
    output_file.write(',')
    output_file.write(output[5])