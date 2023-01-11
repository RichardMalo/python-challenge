# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#List to Store Variables
monthcount = []
nettotal = []
Total = 0
SumMonths = 0

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    # Loop through 
    for row in csvreader:
        
        monthcount.append(row[0])
        nettotal.append(row[1])
nettotal=[int(i) for i in nettotal]
Total=sum(nettotal)
SumMonths = len(monthcount)
print(f"Total Months: {SumMonths}")
print(f"Total: {Total}")