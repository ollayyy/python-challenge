# import modules
import os
import csv
# csv file path
budget_csv = os.path.join('/Users/olivereve/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

# variables
total_months = 0
profit_total = 0

# open / read csv
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # skip headers
    csv_header = next(csvreader)

    # read through rows and get total # of months and net total of profit/losses
    for row in csvreader:

        total_months += 1

        profit_total += int(row[1])

# financial alysis and months and profits
print('Financial Analysis')
print('-------------------')
print('TotalMonths: ', total_months)
print('Total: ', profit_total)

profit_sum = 0
profit_average = 0

with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        profit_sum += int(row[1])
profit_average =  profit_sum / total_months

print(profit_average)

