import os
import csv
# variable to start count of total votes for all cand_dict at 0
totVotes = 0
# empyt dictionary to hold candidate names as keys and # of votes as values 
cand_dict = {}
# Create the path to the file I'm pulling data from
csvpath = os.path.join( 'Resources', 'election_data.csv')
# create a variable to define the read/write method to use on the file
with open(csvpath, newline='') as csvfile:
# Create the reader and define the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
# check if there is a header, and skip it if there is
    if csv.Sniffer().has_header(open(csvpath).read(1024)):
        csv_header = next(csvfile)
    # Starting with the first row of data, loop through to calculate:
    for row in csvreader:
        # The total number of votes cast by adding 1 to totVotes variable for each row
        totVotes = totVotes + 1
        # Look through each row, at col 2, if candidate name isn't in cand_dict dictionary, add it as a key and set value to 1
        if row[2] in cand_dict:
            cand_dict[row[2]] += 1
        # If candidate is already in dictionary, increase the value by 1
        else:
            cand_dict[row[2]] = 1
    # Create list of cand_dict from keys in cand_dict dictionary
    cnames = list(cand_dict.keys())
    # Create list of cand_dict' vote totals from values in cand_dict dictionary
    cv_count = list(cand_dict.values())
    # Create empty list to hold cand_dict' percentages
    percs=[]
    # For each candidate, calculate % of total votes won
    for key in cand_dict:    
        percentage = cand_dict[key]/totVotes
        # append % for each candidate to the percs list after formatting as % with three decimals
        percs.append("{0:.3f}%".format(percentage * 100))
    # print results
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ", '{:,.0f}'.format(totVotes))
    # for each candidate, print their name from the cnames list, 
    # their percentage of votes won from the percs, 
    # and their total votes won from the cv_count list
    for candidate in range(len(cnames)):
        print(cnames[candidate],": ",percs[candidate],
            " (",'{:,.0f}'.format(cv_count[candidate]),")")
    print("-------------------------")
    print("Winner: ",cnames[cv_count.index(max(cv_count))])
    print("-------------------------")

# Open and write to the file using "write" mode. Specify the variable to hold the contents
with open("pypoll_results.csv",'x',newline='') as pypollcsv:
    pypollwriter = csv.writer(pypollcsv,delimiter=',')
    pypollwriter.writerow(["Election Results"])
    pypollwriter.writerow([""])
    pypollwriter.writerow(["Total Votes:",'{:,.0f}'.format(totVotes)])
    pypollwriter.writerow(["Winner:",cnames[cv_count.index(max(cv_count))]])
    pypollwriter.writerow([""])
    pypollwriter.writerow(["Candidate Name","% of Total Votes Won","Total Votes Won"])
    for candidate in range(len(cnames)):
        pypollwriter.writerow([cnames[candidate],percs[candidate],'{:,.0f}'.format(cv_count[candidate])])


