# Filename: cwb2.py
# Name: Jermaine Teo
# Centre No / Index No: 3024 /
# Description: Read resource info from RESOURCE.DAT, get and validate extra details based on resource type, write to URESOURCE.DAT

from classes import *

def UPDATERESOURCE():
    
    try:
        #open resource file for reading
        resource_file = open("RESOURCE.DAT", "r")

        #open updated resource file for writing
        uresource_file = open("URESOURCE.DAT", "w")
        
        #read heading line from resource file
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")

        #store creation date and number of records
        creation_date = heading_line[0:10]
        num_records = heading_line[10:]

        #write creation date and number of records to updated resource file
        uresource_file.write(creation_date + num_records + "\n")        

        #get resource details
        detail_lines = resource_file.readlines()

        #initialize resource list
        resource_list = []

        #loop through each resource
        for record_line in detail_lines:

            #clean each rcord line
            record_line = record_line.rstrip("\n")

            #get and store record info
            resource_no = record_line[0:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:42]
                      
            #display resource info
            print("Resource no: " + resource_no)
            print("Title: " + title)
            print("Date acquired: " + date_acquired)
            print("Resource type: " + resource_type)

            #if music CD
            if resource_type == "C":
                #get and validate music CD details
                    #get and validate artist
                valid_artist = False
                while not valid_artist:
                    artist = input("Enter artist: ")
                    if len(artist) == 0: #presence check
                        print("Invalid! Empty input. Try again.")
                    elif len(artist) > 50: #length check
                        print("Invalid! Cannot exceed 50 characters. Try again.")
                    else:
                        valid_artist = True
                        
                    #get and validate number of tracks
                valid_num_tracks = False
                while not valid_num_tracks:
                    num_tracks = input("Enter number of tracks: ")
                    if len(num_tracks) == 0: #presence check
                        print("Invalid! Empty input. Try again.")
                    elif not num_tracks.isdigit(): #data type check
                        print("Invalid! Number of tracks must contain digits only. Try again.")
                    elif not (0 < int(num_tracks) <= 20): #range check
                        print("Invalid! Number of tracks must be within 1 to 20. Try again.")
                    else:
                        valid_num_tracks = True

                #create music CD object and add to resource list
                resource_list.append(MusicCD(resource_no, title, date_acquired, resource_type, artist, num_tracks))

            #else (if film DVD)
            else: #resource_type == "D"
                #get and validate film DVD details
                    #get and validate director
                valid_director = False
                while not valid_director:
                    director = input("Enter director: ")
                    if len(director) == 0: #presence check
                        print("Invalid! Empty input. Try again.")
                    elif len(director) > 50: #length check
                        print("Invalid! Cannot exceed 50 characters. Try again.")
                    else:
                        valid_director = True
                        
                    #get and validate running time
                valid_running_time = False
                while not valid_running_time:
                    running_time = input("Enter running time(mins): ")
                    if len(running_time) == 0: #presence check
                        print("Invalid! Empty input. Try again.")
                    elif not running_time.isdigit(): #data type check
                        print("Invalid! Running time must contain digits only. Try again.")
                    elif not (30 <= int(running_time) <= 180): #range check
                        print("Invalid! Running time must be within 30 to 180 minutes. Try again.")
                    else:
                        valid_running_time = True

                #create film DVD object and add to resource list
                resource_list.append(FilmDVD(resource_no, title, date_acquired, resource_type, director, running_time))

            #write full resource details to updated resource file
##            for resource in resource_list: # long-winded way
##                if resource.getResourceType == "C":
##                    uresource_file.write(resource.getResourceNo() + resource.getTitle() + resource.getDateAcquired() + resource.getResourceType() + \
##                                         resource.getArtist() + resource.getNumOfTracks() + "NULL                                              " + "000" + "\n")
##                else:
##                    uresource_file.write(resource.getResourceNo() + resource.get(Title() + resource.getDateAcquired() + resource.getResourceType() + \
##                                         "NULL                                              " + "00" + resource.getDirector() + resource.getRunningTime() + "\n")
##
        #a better way
        for resource in resource_list:
            uresource_file.write(resource.display() + "\n")
            

        #close files
        resource_file.close()
        uresource_file.close()
        
    except IOError:
        #display file input/output errors
        print("Error! Cannot read from input file or write to output file.")

#main
if __name__ == "__main__":
    UPDATERESOURCE()
