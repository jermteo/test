#cwb4.py

def REPORT():
    
    try:
        #open resource file for input
        report_file = open("REPORT.DAT", "w")

        #open uresource_list for reading
        uresource_file = open("URESOURCE.DAT", "r")

        #open loan file for reading
        loan_file = open("LOAN.DAT", "r")

        #skip heading line from updated resource file
        heading_line = uresource_file.readline()

        #get resource number, title and resource type into list of lists
        resource_list = []
        resource_details = uresource_file.readlines()
        for resource_line in resource_details:
            resource_list.append(resource_line[0],resource_line[1], resource_line[3])
        
                   #resource list ["00001", "The Planets Suite", "C"]

            #append to resource list? ["01001", "Wuthering Height", "D"]
        
        
        #get date due back, student id, student name, evaluation into list of lists
        loan_list = []
        loan_details = loan_file.readlines()

            #loan list ["00001", "S0237", "J Cho", "150211", "Returned"]

            #append to loan list? ["01001", "S0237", "J Cho", "150211", "<50blanks>"]
        
        #process

        #get dates due back in list format
        ddb_list = []
        for loan in loan_list:
            if loan[3] not in ddb_list:
                ddb_list.append(loan[3]) #stores unique list of ddbs
                
        #initialise dictionary of date due back
        ddb_dict = {}

        for ddb in ddb_list:
            ddb_dict[ddb] = []

        #set up data structure to hold merged record
            #["00001", "The Planets Suite", "CD", "S0001", "Lim Ah Seng")
        final_record = []
        
        #compare resource no in loan_list with resource no in resource list
        for loan in loan_list:
            for resource in resource_list:
                if (loan[0] == resource[0]): #check if resource numbers match
                    if resource[2] == 'C':
                        resource_type = "CD"
                    else:
                        resource_type = "DVD"
                    if loan[4] ==(" " * 50):
                        final_rec.append([resource[0], resource[1], resource_type, loan[1], loan[2]])

            #report list ["01001", "Wuthering Heights", "DVD", "S0237", "J Cho"]
        
        #display report
        print(final_record)
        




        #close files
        report_file.close()
        uresource_file.close()
        loan_file.close()

    except IOError:
        #dislpay file i/o error
        print("Error! Unable to read from file or write to file. Try again.")

#main
if __name__ == "__main__":
    REPORT()
