#!/usr/bin/env python
# coding: utf-8

# In[70]:


# create variables I need
totVotes = 0
candidate = "start"
candidates_names = []
candidates_votes = []
candidates = {}

import os
import csv

# Create the path to the file I'm pulling data from
csvpath = os.path.join( 'Resources', 'election_data.csv')
# create a variable to define the read/write method to use on the file
with open(csvpath, newline='') as csvfile:
# Create the reader and define the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
# check if there is a header, and skip it if there is
    if csv.Sniffer().has_header(open(csvpath).read(1024)):
        csv_header = next(csvfile)
    print(csv_header)
    # Starting with the first row of data, loop through to calculate:
    for row in csvreader:
    # The total number of votes cast
        # For each line, add 1 to totVotes
        totVotes = totVotes + 1
        # A complete list of candidates who received votes
        # Look through each row, at col 2, if candidate name isn't in 
        # the candidates list, add it
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    print(totVotes)
    print(candidates)


# In[77]:


for key in candidates:    
    percentage = candidates[key]*100/totVotes
print(percentage)


# In[78]:


print("Election Results")
print("-------------------------")
print("Total Votes: ", '{:,.0f}'.format(totVotes))
print(candidates)


# In[ ]:





# In[ ]:




