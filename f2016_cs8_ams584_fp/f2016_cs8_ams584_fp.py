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

    def __str__(self):  # Formats the output
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

    def tocsv(self):    #
        return ','.join([self.name, str(self.runs), str(self.distance)])


def getData(file):
    output = []
    for line in open(file,'r'):
        if "distance" in line:
            continue
        line = line.rstrip('\n').split(',')
        try:
            output.append({'name': line[0].strip(' '), 'distance':float(line[1])})
        except:
            print('Invalid row : '+line.rstrip('\n'))
    return output
masterFile = input("Enter the Master File : ")

try:
   data = open(masterFile, 'r')
   for file in masterFile:
       dataFiles = file.rstrip('\n')
except:
    print("Invalid file name")
    exit(1)

for data in dataFiles:
    rawData = sum(getData(file))
nfiles = len(dataFiles)

totalLines = len(rawData)

totalDistance = sum([item['distance'] for item in rawData])

participants = {}

for item in rawData:

    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    participants[item['name']].addDistance(item['distance'])

minDistance = { 'name' : None, 'distance': None }

maxDistance = { 'name' : None, 'distance': None }

apparences = {}

for name, object in participants.items():

    distance = object.getDistance()

    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance

    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance

    participantAppearences = object.getRuns()

    if not participantAppearences in apparences.keys():
        apparences[participantAppearences] = []
    apparences[participantAppearences].append(name)

totalParticipants = len(participants);

totalParticipantsMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])

int = '5d'
float = '12.5f'
str = '20s'

print("")
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

outputFile = "f2016_cs8_ams584_fp.output.csv"

fh = open(outputFile,'w')

fh.write('name,records,distance\n')

for name, object in participants.items():

    fh.write(object.tocsv() + '\n')

fh.close()


