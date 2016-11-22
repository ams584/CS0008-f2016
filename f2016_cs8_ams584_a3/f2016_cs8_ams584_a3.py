master_file_list = input("Enter the location of the file list: ")
global_dictionary = {}
def processfile(master_file_list, dictionary):
    contents_mfl = open(master_file_list, 'r')
    length_mfl = 0
    length_files = []
    for line in contents_mfl:
        length_files.append(0)
        length_mfl+=1
        filename = line.rstrip('\n')
        x = open(filename, 'r')
        x.readline()
        t_dist = 0
        for line in x:
            length_files[length_mfl-1] += 1
            z = 0
            line = line.rstrip('\n')
            name, dist = line.split(',')
            p_dist = float(dist)
            t_dist += p_dist
            dictionary = {}
            if name in dictionary:
                z = 1
                dictionary.append(dist)
            else:
                dictionary = name, dist
    return(dictionary, t_dist, length_mfl, length_files, z, dist, name)

output = processfile(master_file_list, global_dictionary)
max_name = ' '
max_dist = 0
name, dist = output[0]
dist = dist
for name in output[0]:
    l_values = dist
    print(l_values)
    if l_values > max_dist:
        max_dist = l_values
        max_name = name
min_name = ' '
min_dist = 0
for name in output[0]:
    x_values = dist
    if (x_values < min_dist):
        min_dist = x_values
        min_name = name
for dist in output[0]:
    times_participated = 0
    times_participated += 1
total_participants = len(global_dictionary)
print("Number of input files read       :",output[2])
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

output_file = open('output_file.txt', 'w')
for name in output:
    output_file.write(output[6])
    output_file.write(',')
    output_file.write(times_participated)
    output_file.write(',')
    output_file.write(output[5])