# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# List to Store Variables
monthcount = []
nettotal = []
Total = 0
SumMonths = 0
AvgChange = []

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and skip the header row
    csv_header = next(csvreader)

    # Loop through 
    for row in csvreader:
        monthcount.append(row[0])
        nettotal.append(row[1])
# Change netotal to an integer from ' ' to int
nettotal = [int(x) for x in nettotal]
# Sum up all the numbers in library nettotal
Total = (sum(nettotal))
# Sum up all the months by the length of the library monthcount
SumMonths = (len(monthcount))

# Create new library of Change from cell 1 to 2 = and so on for one less iteration than total amount of rows.
AvgChange = [nettotal[x+1]-nettotal[x] for x in (range(len(nettotal)-1))]
# Average change Sum of all Change variables divided by length of library AvgChange.
avgchangetotal = (sum(AvgChange)/len(AvgChange))

# Calculation of max/min AvgChange and storing of date index in varaiable top/bot date
topamount = (max(AvgChange))
topdate = (monthcount[AvgChange.index(max(AvgChange))+1])
botamount = (min(AvgChange))
botdate =(monthcount[AvgChange.index(min(AvgChange))+1])

# Printout an esthetically pleasing result =) of Text to Terminal
print("\033[1mFinancial Analysis\033[0m")
print("------------------")
print(f"\033[1mTotal Months: \033[0m{SumMonths}")
print(f"\033[1mTotal: $\033[0m {Total}")
print(f"\033[1mAverage Change: $\033[91m {round(avgchangetotal,2)}\033[0m")
print(f"Greatest Increase in Profits: {topdate} ($  {topamount})")
print(f"Greatest Decrease in Profits: {botdate} (\033[91m$ {botamount}\033[0m)")

# Set path for printout to Textfile
output = os.path.join("analysis", "output.txt")

# Print to textfile output.txt substituing 
with open(output, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------\n")
    text.write(f"Total Months: {SumMonths}\n")
    text.write(f"Total: ${Total}\n")
    text.write(f"Average Change: $ {round(avgchangetotal,2)}\n")
    text.write(f"Greatest Increase in Profits: {topdate} ($  {topamount})\n")
    text.write(f"Greatest Decrease in Profits: {botdate} ($ {botamount})")