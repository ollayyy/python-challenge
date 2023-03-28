# import modules

import os
import csv

#cvs path

cvspath = os.path.join('/Users/olivereve/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

#variables
total_votes = 0
candidates = {}

# read the csv file and skip header
with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)
    
    #loop through rows
    for row in csvreader:

        # total  number of votes
        total_votes += 1

        # check if candidate already exists and add a vote or create a new candidate with 1 vote
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# winner variables
most_votes = 0
winner = ""

# print out results
print('Election Results')
print('-------------------------')
print('Total Votes: ', total_votes)
print('-------------------------')
# for loop to go through each candidate and print out their results, nested if to decide winnner
for candidate, votes in candidates.items():
    votes_percentage = round((votes/total_votes)* 100, 3)

    print(f'{candidate}')
    print(f"{votes} | {votes_percentage}%")
    print('-----------------------')
    # if loop to find winner by votes
    if most_votes < votes:
        most_votes = votes
        winner = candidate

print('Winner:', winner)
print('-------------------------')
