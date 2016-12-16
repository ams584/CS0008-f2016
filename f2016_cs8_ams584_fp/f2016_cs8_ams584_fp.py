class participant:      # Creates the participant class
    name = "unknown"
    distance = 0    # Defines the distance variable
    runs = 0    # Defines the runs variable
    def __init__(self, name, distance=0):   # Initiates the class
        self.name = name
        if distance > 0:
            self.distance = distance
            self.runs = 1
    def addDistance(self, distance):    # Creates a function to add distances in a file
        if distance > 0:
            self.distance += distance
            self.runs += 1
    def addDistances(self, distances):   # Creates a function to add all the individual distances
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
    def getName(self):  # Returns the name of the participant
        return self.name

    def getDistance(self):  #  Returns the particpants distance
        return self.distance

    def getRuns(self):  # Returns the number of runs for each particpant
        return self.runs

    def __str__(self):  # Turns the object into a string
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

    def tocsv(self):    # Converts to csv
        return ','.join([self.name, str(self.runs), str(self.distance)])


def getData(file):      # Defines the getData function
    output = []     # Creates the output list
    file = open(file,'r')       # Opens the file
    for line in file:   # Iterates through each line
        if "distance" in line:      # Skips the header line
            continue
        line = line.rstrip('\n').split(',')     # Splits the line into name and distance, and strips the \n
        try:    # Appends the name and distance to the output list
            output.append({'name': line[0].strip(' '), 'distance':float(line[1])})
        except:     # If there is an error, print an error
            print('Invalid row : '+line.rstrip('\n'))
    return output
masterFile = input("Enter the Master File : ")      # Prompts the user for the master file

try:
   data = open(masterFile, 'r')     # Reads the master file and recieves the list of files
   for file in masterFile:
       dataFiles = file.rstrip('\n')    # Strips the \n
except:
    print("Invalid file name")      # Prints an error message if the file name is invalid
    exit(1)

for data in dataFiles:  # Reads each of the data files
    rawData = sum(getData(file))    # Totals the data
nfiles = len(dataFiles)     # Gets the length of the data files

totalLines = len(rawData)   # Gets the total number of lines

totalDistance = sum([item['distance'] for item in rawData])     # Sums all of the distances

participants = {}       # Creates the participants dictionary

for item in rawData:

    if not item['name'] in participants.keys():     # Adds the participant to the dictionary
        participants[item['name']] = participant(item['name'])
    participants[item['name']].addDistance(item['distance'])

minDistance = { 'name' : None, 'distance': None }   # Defines the minDistance

maxDistance = { 'name' : None, 'distance': None }   # Defines the maxDistance

appearences = {}     # Defines the appearances

for name, object in participants.items():   # Loops through all the participants

    distance = object.getDistance()     # Gets the distance for each particpant

    if minDistance['name'] is None or minDistance['distance'] > distance:   # Redefines the minDistance if there is no distance run or if the minimum distance is bigger than the distance run
        minDistance['name'] = name
        minDistance['distance'] = distance

    if maxDistance['name'] is None or maxDistance['distance'] < distance:   # Redefines the maxDistance if there is no distance run or if the maximum distance is smaller than the distance run
        maxDistance['name'] = name
        maxDistance['distance'] = distance

    participantAppearences = object.getRuns()   # Gets the number of runs for each particpant

    if not participantAppearences in appearences.keys():    # Adds the number of times the participants appeared to the dictionary
        appearences[participantAppearences] = []
    appearences[participantAppearences].append(name)

totalParticipants = len(participants)   # Gets the length of the participant list

totalParticipantsMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])     # Creates a total and adds to it each time a participants name appears in the particpants dictionary

int = '5d'  # Formats the integers
float = '12.5f' # Formats the floats
str = '20s' # Formats the strings

print("")       # Prints everything
print(" Number of Input files read   : " + format(nfiles,int))
print(" Total number of lines read   : " + format(totalLines,int))
print("")
print(" Total distance run           : " + format(totalDistance,float))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],float))
print("   by participant             : " + format(maxDistance['name'],str))
print("")
print(" Min distance run             : " + format(minDistance['distance'],float))
print("   by participant             : " + format(minDistance['name'],str))
print("")
print(" Total number of participants : " + format(totalParticipants,int))
print(" Number of participants")
print("  with multiple records       : " + format(totalParticipantsMultipleRecords,float))
print("")

outputFile = "f2016_cs8_ams584_fp.output.csv"       # Creats an output file

fh = open(outputFile,'w')       # Opens the output file

fh.write('name,records,distance\n')     # Writes the names, records, and distances to the output file

for name, object in participants.items():

    fh.write(object.tocsv() + '\n')     # Writes the tocsv function

fh.close()      # Closes the file


