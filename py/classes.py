# Filename: classes.py
# Author: Esther Tan
# Centre No / Index No: 3024 / 9
# Description: Support classes for music library

'''Superclass Resource'''
class Resource:

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        #self.__data is for private data
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    '''Resource number accessor'''
    def getResourceNo(self):
        return self.__ResourceNo

    '''Title accessor'''
    def getTitle(self):
        return self.__Title

    '''Date acquired accessor'''
    def getDateAcquired(self):
        return self.__DateAcquired

    '''Resource type accessor'''
    def getResourceType(self):
        return self.__ResourceType

    #No '''Resource number modifier''' because primary key should not be edited
        
    '''Title modifier'''
    def setTitle(self, newTitle):
        self.__Title = newTitle

    '''Date acquired modifier'''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    '''Resource type modifier'''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    '''Display helper function'''
    def display(self):
        return "{0:5s}{1:30s}{2:6s}{3}".format \
               (self.getResourceNo(), self.getTitle(), self.getDateAcquired(), self.getResourceType())

#subclasses should be in the form: title-of-subclass(title-of-superclass)
'''Subclass MusicCD'''
class MusicCD(Resource):

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType) #super().__init__ shows inheritance
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks
    
    '''Artist accessor'''
    def getArtist(self):
        return self.__Artist

    '''Number of tracks accessor'''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    '''Artist modifier'''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    '''Number of tracks modifier'''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks

    '''Display helper function'''
    def display(self):
        return "{0}{1:50}{2}".format \
               (super().display(), self.getArtist(), self.getNoOfTracks())

'''Subclass FilmDVD'''
class FilmDVD(Resource):

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime
    
    '''Director accessor'''
    def getDirector(self):
        return self.__Director

    '''Running time accessor'''
    def getRunningTime(self):
        return self.__RunningTime

    '''Director modifier'''
    def setDirector(self, newDirector):
        self.__Director = newDirector

    '''Running time modifier'''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime

    '''Display helper function'''
    def display(self):
        return "{0}{1:50}{2}".format \
               (super().display(), self.getDirector(), self.getRunningTime()) #backslash takes coding in next line to be joined to this line

#main
##r1 = Resource("00001", "Best of SHINee", "030309", "C")
##
##print(r1.getResourceNo())
##
##r1.setTitle("Falala SHINee")
##
##print(r1.getTitle())
##
##print(r1.display())
##
##r2 = Resource("00002", "", "", "")
##
##r2.setTitle("TVXQ Collection")
##r2.setDateAcquired("050510")
##r2.setResourceType("C")
##
##print(r2.display())

# print(r2.__Title) -> illegal should not access private data directly
                 #  -> data/information hiding (encapsulation)


##cd1 = MusicCD("00003", "FT Island Hits", "090807", "C", "FT Island", 5) #no need to turn num of tracks into string
##print(cd1.getResourceNo()) #inherited method
##print(cd1.getArtist()) #class method
##print(cd1.display()) #overriding
##
##dvd1 = FilmDVD("00004", "The Green Hornet", "091209", "D", "Blah", 120)
##print(dvd1.display())
##
##resource_list = []
##
##resource_list.append(cd1)
##resource_list.append(dvd1)
##
##print(resource_list)
##
##for item in resource_list:
##    print(item.display()) #polymorphism - can display both cd and dvd using their respective display methods
##
