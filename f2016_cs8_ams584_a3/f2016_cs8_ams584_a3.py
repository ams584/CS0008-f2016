def processfile(master_file_list):
    master_file_list = str(input("Enter the location of the file list: "))
    contents_mfl = open(master_file_list, 'r')
    length_mfl = len(master_file_list)
    for line in master_file_list:
        files = (master_file_list.readline())
        files2 = files.split(',')
        files3 = line.append[files.rstrip('\n')]
    print(length_mfl, files3)
    return(files3, length_mfl)
def process(files3):
    files3, length_mfl = processfile()
    length_lines = len(files3) * length_mfl
    contents_file2 = open(files3, 'r')
    for line in files3:
        data = files3.readline()
        name, distance = data.split(',')

process()