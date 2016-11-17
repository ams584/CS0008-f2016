master_file_list = (input("Enter the location of the file list: "))
def processfile(master_file_list):
    contents_mfl = open(master_file_list, 'r')
    length_mfl = len(master_file_list)
    for line in contents_mfl:
        files = (contents_mfl.readline())
        files2 = files.split(',')
    print(length_mfl, files2)
    return(files2, length_mfl)
processfile(master_file_list)
def process(files2):
    length_lines = len(files2)
    contents_file2 = open(files2, 'r')
    for line in files2:
        data = files2.readline()
        name, distance = data.split(',')

process()