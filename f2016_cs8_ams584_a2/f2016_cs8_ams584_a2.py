def processFile():
    x = str(input("Enter the name of the file: "))
    x = open('/users/Alex/Desktop/Data_File_1.txt', 'r')
    n_1 = 0
    for line in Data_File_1:
        n_1 = n_1+1
        contents_f1 = (Data_File_1.readline())
        name_f1, distance_f1 = contents_f1.split(',')
        if isinstance(distance_f1, str):
            distance_f1 = float(distance_f1)
        print(distance_f1)
    if line != '':
        print("Number of lines in file 1:", n_1)
    Data_File_2 = open('/users/Alex/Desktop/Data_File_2.txt', 'r')
    n_2 = 0
    for line in Data_File_2:
        n_2 = n_2 + 1
        contents_f2 = (Data_File_2.readline())
        name_f2, distance_f2 = contents_f2.split(',')
        if isinstance(distance_f2, str):
            distance_f2 = float(distance_f2)
        print(distance_f2)
    if line != '':
        print("Number of lines in file 2:", n_2)


processFile()