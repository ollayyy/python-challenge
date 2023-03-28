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

monthly_change = []
month_count = []
previous_change = 0

with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        if total_months > 1:
            monthly_change.append(int(row[1]) - previous_change)
            month_count.append(row[0])

        previous_change = int(row[1])

average_change = sum(monthly_change) / len(monthly_change)

print(average_change)