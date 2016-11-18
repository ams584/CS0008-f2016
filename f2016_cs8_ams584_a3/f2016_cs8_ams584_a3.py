master_file_list = (input("Enter the location of the file list: "))
def processfile(master_file_list):
    contents_mfl = open(master_file_list, 'r')
    files = (contents_mfl.readlines())
    for line in contents_mfl:
        filename = line.rstrip('\n')
        length_mfl = len(files)
        print(filename)
        x = open(filename, 'r')
        x.readline()
        for line in x:
            print(line)
            line = line.rstrip('\n')
            name, dist = line.split(',')
            p_dist = int(dist)
            t_dist = 0
            t_dist += p_dist
            p_names = int(name)
            t_names = 0
            t_names += p_names
            if name in list:
                list = list.append(line, list)
        print(p_dist, p_names)
processfile(master_file_list)