master_file_list = (input("Enter the location of the file list: "))
def processfile(master_file_list):
    contents_mfl = open(master_file_list, 'r')
    files = (contents_mfl.readlines())
    for line in files:
        filename = line.rstrip('\n')
        length_mfl = len(files)
        print(filename)
        x = open(filename, 'r')
        contents = x.readline()
        name, dist = contents.split('\n')
        print(contents)
        list = [name]
        for line in contents:
            contents.rstrip('\n')
            p_dist = int(dist)
            t_dist = 0
            t_dist += p_dist
            p_names = int(name)
            t_names = 0
            t_names += p_names
            if name in list:
                list = list.append(name, list)
        print(p_dist, p_names)
