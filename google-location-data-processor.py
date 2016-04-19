import json
import random
import sys
import os


def load_file(JSONFile):
    ''' Load aJSON file. '''
    f = open(JSONFile)

    j = json.load(f)
    return j


hlp = "Google location Data processor. \n Application takes Google takeout location data im JSON format and splits it uo into N number of specific trips.\n Useage: google-location-data-processor [JSON file] [number of trips] [longest trip]\n"


if len(sys.argv) < 2:
    print(hlp)
else:
    locationsFile = open(sys.argv[3], "a")   #open the outputfile for append
    JSON = load_file(sys.argv[1])       #load JSON

    print("Number of possible locations: "+str(len(JSON["locations"])))

    for j in range(0,int(sys.argv[2])): #for the number of people we want


        starting = random.randint(0,len(JSON["locations"]))        #Pick a random starting location
        lengthOfWalk = random.randint(5,50)         #and a random number of locations

        iterator = 0


        records = list()

        print("Length of walk: "+str(lengthOfWalk))

        print("Generating locations... \n")
        while iterator < lengthOfWalk:
            records.append(JSON["locations"][starting+iterator])
            iterator= iterator+1


        print("Writing locations")
        locationsFile.write("{ \"type\": \"lineString\", \"coordinates\":[ ")
        s = True
        for record in records:
            if s == False:
                locationsFile.write(",")
            lng = int(record["longitudeE7"]) /10000000 #-1.345345
            lat = int(record["latitudeE7"])/10000000  #52.324

            locationsFile.write("["+str(lng)+","+str(lat)+"]")
            s = False
        locationsFile.write("] } ") 
        locationsFile.write("\n")














