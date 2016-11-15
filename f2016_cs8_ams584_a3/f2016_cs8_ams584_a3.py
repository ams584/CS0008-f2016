def processfile(master_file_list):
    master_file_list = str(input("Enter the location of the file list: "))
    contents_mfl = open(master_file_list, 'r')
    length_mfl = len(master_file_list)
    for line in master_file_list:
        files = (master_file_list.readline())
        files2 = line.append[files.rstrip('\n')]
    return(files2, length_mfl)
def process(files2):
    processfile()
    contents_file2 = open(files2, 'r')
    for line in files2:
        data = files2.readline()
        name, distance = data.split(',')
        

