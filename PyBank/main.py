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
AvgChange = []

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    # Loop through 
    for row in csvreader:
        
        monthcount.append(row[0])
        nettotal.append(row[1])
#change netotal to an integer from ' ' to int
nettotal = [int(x) for x in nettotal]
#Sum up all the numbers in library nettotal
Total = (sum(nettotal))
#Sum up all the months by the length of the library monthcount
SumMonths = (len(monthcount))
#Calculating an average change of nettotal library
AvgChange = [nettotal[x+1]-nettotal[x] for x in (range(len(nettotal)-1))]
#Average change 
avgchangetotal = (sum(AvgChange)/len(AvgChange))
#Print out text to Terminal
print("\033[1mFinancial Analysis\033[0m")
print("------------------")
print(f"\033[1mTotal Months: \033[0m{SumMonths}")
print(f"\033[1mTotal: $\033[0m{Total}")
print(f"\033[1mAverage Change: $\033[91m{round(avgchangetotal,2)}\033[0m")