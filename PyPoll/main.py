# import modules

import os
import csv

#cvs path

cvspath = os.path.join('/Users/olivereve/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

#variables
total_votes = 0

# read the csv file and skip header
with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)
    
    #loop through rows
    for row in csvreader:

        # total  number of votes
        total_votes += 1

# print out results
print('Election Results')
print('-------------------------')
print('Total Votes: ', total_votes)
print('-------------------------')
