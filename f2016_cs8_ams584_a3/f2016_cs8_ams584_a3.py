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
        for line in x:
            line = line.rstrip('\n')
            name, dist = line.split(',')
            p_dist = int(dist)
            t_dist = 0
            t_dist += p_dist
            if name in dict:
                dict[name] = dict[name].append(dist)
    return(dict, t_dist, length_mfl)

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
