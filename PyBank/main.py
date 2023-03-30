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
print('------------------------------------------')
print('TotalMonths: ', total_months)
print('Total: $',profit_total)

# variables
monthly_change = []
month_count = []
previous_change = 0
max_increase = 0
max_increase_month = ""
min_increase = 0
min_increase_month = ''

with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        # if statement to check if mo
        if total_months > 1:
            monthly_change.append(int(row[1]) - previous_change)
            month_count.append(row[0])

            #if statements to check for the greatest inc/dec on months
            if (int(row[1]) - previous_change) > max_increase:
                max_increase = int(row[1]) - previous_change
                max_increase_month = row[0]

            if (int(row[1]) - previous_change) < min_increase:
                min_increase = int(row[1]) - previous_change
                min_increase_month = row[0]
        # return profit change    
        previous_change = int(row[1])

average_change = sum(monthly_change) / len(monthly_change)
print('Average Change: ', average_change)
print(f'Greatest increase in Profits:', max_increase_month,'($',max_increase,')')
print(f'Greatest Decrease in Profits:',min_increase_month,'($',min_increase,')')
print('----------------------------------------------------------')

# create and print results to a .txt
file = open('Analysis/PyBank_Results.txt', 'w')

file.write('Financial Analysis\n')
file.write('----------------------------------\n')
file.write('Total Months:' + str(total_months) + '\n')
file.write('Total: ' +  str(profit_total) + '\n')
file.write('Average Change: ' + str(average_change) + '\n')
file.write('Greatest increase in Profits: ' + str(max_increase_month) + '($' + str(max_increase) + ')\n')
file.write('Greatest Decrease in Profits: ' + str(min_increase_month) + '($' + str(min_increase) + '\n')
file.write('---------------------------------------------------------')