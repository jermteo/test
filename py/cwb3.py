# Filename: cwb3.py
# Name: Jermaine Teo
# Centre No / Index No: 3101 /
# Descripttion: Append validated loan data, write to LOAN.DAT

from classes import *
import datetime

def LOANRESOURCE():

    try:
        #open loan file for appending
        loan_file = open("LOAN.DAT", "a")
        
        #open updated resource file for reading
        uresource_file = open("URESOURCE.DAT", "r")

        #skip heading line from updated resource file - get details
        heading_line = uresource_file.readline()

        #initialize resource number list
        resourceno_list = []
        
        #read record details
        detail_lines = uresource_file.readlines()

        #loop through all record in uresource
        for resource_line in detail_lines:

            #get resource number and append to list
            resourceno = resource_line[0:5]
            resourceno_list.append(resourceno)

        #get NoOfResourcesBorrowing
        valid_numborrowing = False
        while not valid_numborrowing:
            num_borrowing = input("Enter number of resources you want to borrow: ")
            if len(num_borrowing) == 0: #presence check
                print("Invalid! Number of items borrowing cannot be empty. Try again.")
            elif not num_borrowing.isdigit(): #datatype check
                print("Invalid! Number of items borrowing can only consist of digits. Try again")
            elif int(num_borrowing) > 3:
                print("Invalid! Maximum of resources borrowed at one time cannot exceed 3. Try again.")
            else:
                valid_numborrowing = True

        for record in range(int(num_borrowing)):

            #get and validate ResourceNo - assuming resource is not loaned already
            valid_resourceno = False
            while not valid_resourceno:
                resourceno = input("Enter resource number: ")
                if len(resourceno) == 0: #presence check
                    print("Invalid! Resource number must not be empty. Try again.")
                elif not len(resourceno) == 5: #length check
                    print("Invalid! Resource number must be exactly 5 digits. Try again.")
                elif not resourceno.isdigit(): #data type check
                    print("Invalid! Resource number must be numbers only. Try again.")
                elif resourceno not in resourceno_list:
                    print("Invalid! Resource does not exist. Try again.")
                else:
                    valid_resourceno = True
        
            #get and validate StudentID
            valid_studentid = False
            while not valid_studentid:
                studentid = input("Enter Student ID: ")
                if len(studentid) == 0: #presence check
                    print("Invalid! Student ID cannot be empty. Try again.")
                elif not len(studentid) == 5: #length check
                    print("Invalid! Student ID must be exactly 5 characters. Try again.")
                elif not studentid[0:1].upper() == 'S': #use single quote for characters
                    print("Invalid! Student ID must start with a 'S'. Try again.")
                elif not studentid[1:5].isdigit(): #data type check
                    print("Invalid! Student ID must contain 4 digits after the 'S'. Try again.")
                elif not ( 0 < int(studentid[1:5]) <= 9999):
                    print("Error, student ID must be from S0001 to S9999. Try again.")
                else:
                    valid_studentid = True
                
            #get and validate StudentName - what about names with numbers?!
            valid_studentname = False
            while not valid_studentname:
                studentname = input("Enter student name: ")
                if len(studentname) == 0: #presence check
                    print("Invalid! Student name cannot be empty. Try again.")
                elif len(studentname) > 30: #length check
                    print("Invalid! Student name must contain at most 30 characters. Try again.")
                else:
                    valid_studentname = True
                   
                    
            #calculate DateDueBack - 7 days from loan date
            dateloaned = datetime.date.today()

            #add 7 days to get datedueback
            datedueback = dateloaned + datetime.timedelta(days=7)

            ddb = datedueback.strftime("%d%m%y")
            
            #validate Evaluation
            evaluation = " " * 50        

            #initialise loan list
            loan_list = []

            #write validated record to LOAN.DAT
            loan_list.append([(resourceno), studentid, "{0:30s}".format(studentname), ddb, evaluation])
            
            for loan_details in loan_list:
                for loan in loan_details:
                    loan_file.write(loan)
                loan_file.write("\n")      
        
        #close files
        loan_file.close()
        uresource_file.close()
        
    except IOError:
        print("Error! Unable to read from input file or write to output file!")
        

#main
if __name__ == "__main__":
    LOANRESOURCE()
