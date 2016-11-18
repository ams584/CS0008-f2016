master_file_list = input("Enter the location of the file list: ")
global_dict = {}
def processfile(master_file_list, global_dict):
    contents_mfl = open(master_file_list, 'r')
    files = contents_mfl.readlines()
    for line in contents_mfl:
        filename = line.rstrip('\n')
        length_mfl = len(files)
        x = open(filename, 'r')
        x.readline()
        file_length = len(filename)
        for line in x:
            z = 0
            line = line.rstrip('\n')
            name, dist = line.split(',')
            p_dist = int(dist)
            t_dist = 0
            t_dist += p_dist
            if name in dict:
                z = 1
                dict[name] = dict[name].append(dist)
    return(dict, t_dist, length_mfl, file_length, z, dist)

processfile(master_file_list, global_dict)
max_name = ' '
max_dist = 0
for name in global_dict:
    l_values = global_dict[name]
    if (max(l_values) > max_dist):
        max_dist = max(l_values)
        max_name = name
min_name = ' '
min_dist = 0
for name in global_dict:
    x_values = global_dict[name]
    if (min(x_values) < min_dist):
        min_dist = min(x_values)
        min_name = name
total_participants = len(global_dict)
print("Number of input files read       :",processfile(2))
print("Number of lines read             :",processfile(3))
print("\n")
print("Total Distance                   :",processfile(1))
print("\n")
print("Max Distance Run                 :",max_dist)
print("  by participant                 :",max_name)
print("\n")
print("Min Distance Run                 :",min_dist)
print("  by participant                 :",min_name)
print("Total Number of Participants     :",total_participants)

output_file = open('output_file.txt', 'w')
for name in dict:
    output_file.write(name)
    output_file.write(',')
    output_file.write()
    output_file.write(',')
    output_file.write(processfile(5))