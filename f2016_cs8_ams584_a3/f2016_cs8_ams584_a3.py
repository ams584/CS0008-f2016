#
# MN: header with user, instructor and course info is missing
#
# Notes:
# Have mercy
# MN: I don't need to have mercy, I know that my students are good!!!
#
# MN: please please please do not use inline comments!!! IT's hard to read the code
#

# MN: try to keep line sof code that belong to the same block of code together
#     moved below
#master_file_list = input("Enter the location of the file list: ")   # Requests the location of the master file list
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
            # MN: are you sure about your logic in this loop?
            length_files[length_mfl-1] += 1     # Makes a counter that counts the total number of lines throughout every data file
            # MN: what's the purpose of this variable?
            z = 0
            line = line.rstrip('\n')        # Strips the \n
            name, dist = line.split(',')    # Splits each line into name and distance
            p_dist = float(dist)
            t_dist += p_dist           # Totals the distance
            # MN: if you initialize the dictionary at every iteration, you end up only with the last entry
            #dictionary = {}
            # MN: are you testing if name is in the keys of a dictionary or if it is in a list
            if name in dictionary.keys():
                z = 1
                # MN: are you sure that this syntax is correct?
                #dictionary.append(dist)     # Appends a name if it appears more than once
                dictionary[name].append(p_dist)
                # MN: given that you have the same statment in both branches of the if statement, you can move it outside right after
                #     although I do not suggest to print lengthy output unless you are debugging the program
                #print(dictionary)
            else:
                # MN: are you sure of this syntax?
                #dictionary = name, dist
                dictionary[name] = [p_dist]
                #print(dictionary)
    # MN: why do you return last distance and name found and z?
    return(dictionary, t_dist, length_mfl, length_files, z, dist, name)     # Returnes the values needed

master_file_list = input("Enter the location of the file list: ")   # Requests the location of the master file list
output = processfile(master_file_list, global_dictionary)

max_name = ' '
max_dist = 0
# MN: what are you trying to do here?
#name, dist = output[0]
# MN: I assume that you want to iterate on the keys of the dictionary, correct?
for name in output[0].keys():
    # MN: where is dist defined?
    # MN: I assume that you want to find the total distance run by the participant?
    #l_values = float(dist)      # Searches the dictionary for the max distance of each name
    l_values = sum(output[0][name])
    if l_values > max_dist:     # Tests which value is greater if there is more than one value for distance per name
        max_dist = l_values
        max_name = name

min_name = ' '
min_dist = 10000
# MN: same as for max
#for name in output[0]:      # Does the same thing as for the max distance run
for name in output[0].keys():
    # MN: where is dist defined?
    #x_values = float(dist)
    x_values = sum(output[0][name])
    if (x_values < min_dist):
        min_dist = x_values
        min_name = name

# MN: you want loop on all the participants
# MN: you do not need this loop, beacuse you can count the records in other ways, see below
#for dist in output[0]:
    # MN: done this way you are computing for the number of records for each participant, but... I'm not sure what
    #times_participated = 0      # Counts the number of times each person participated
    #times_participated += 1
    #times_participated = str(times_participated)

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
# MN: are you sure about this loop? Have you checked the output file?
# MN: you need to loop an all the participants
#for name in output:
for name in output[0].keys():
    # MN: you have already name from the loop
    #output_file.write(output[6])        # Writes to the output file for each name
    output_file.write(name)
    output_file.write(',')
    # MN; the number of records can be computed by the len of the distances found for the particpant
    #output_file.write(times_participated)
    output_file.write(str(len(output[0][name])))
    output_file.write(',')
    # MN: the total distance run can be found summing all the distances found for the participant
    output_file.write(output[5])
    output_file.write(str(sum(output[0][name])))
    # MN: new line to make output look nice
    output_file.write('\n')
# MN: you need to close every file that you open
output_file.close()
