# Modules.
import os
import csv

#List to Store Variables.
Candidates = []
AllCandidates = []
Total = 0
count1 = 0
count2 = 0
count3 = 0
name1 = "Charles Casper Stockham"
name2 = "Diana DeGette"
name3 = "Raymon Anthony Doane"

# Set path for file.
csvpath = os.path.join("Resources", "election_data.csv")

# Open the Reader from above path.
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and skip the header row.
    csv_header = next(csvreader)

    # Loop through cvs document.
    for row in csvreader:
        #Send Candidate Name to list.
        Candidates.append(row[2])  
    
    # Loop through Candidates Library to extract numbers and names.  
    for x in (Candidates):
        if x == name1:
            count1 = count1 + 1
        elif x == name2:
            count2 = count2 + 1
        elif x == name3:
            count3 = count3 + 1

# Grab total # of votes from all counts. I could have used a simple counter of total inside the loop but this seemed as simple as that.
Total = count1+count2+count3
per1 = round(((count1/Total)*100),2) 
per2 = round(((count2/Total)*100),2)
per3 = round(((count3/Total)*100),2)

# Use a library to determine max amount of votes to determine position of topCandiate position in library to later print it out.
Candidates1 = [count1,count2,count3]
Candidates2 = [name1,name2,name3]
topamount = (max(Candidates1))
topCandidate = (Candidates2[Candidates1.index(topamount)])

# Printout of Text to Terminal.
print("\033[1mElection Results\033[0m")
print("---------------------")
print(f"Total Votes: {Total}")
print(f"{name1}: {per1}%, Total Votes : ({count1})")
print(f"{name2}: {per2}%, Total Votes : ({count2})")
print(f"{name3}: {per3}%, Total Votes : ({count3})")
print("---------------------")
print(f"\033[1mWinner:\033[0m {topCandidate}")
print("---------------------")

# Printout of Text to File output.txt.
output = os.path.join("analysis", "output.txt")

with open(output, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------\n")
    text.write(f"Total Votes: {Total}\n")
    text.write(f"{name1}: {per1}%, Total Votes : ({count1})\n")
    text.write(f"{name2}: {per2}%, Total Votes : ({count2})\n")
    text.write(f"{name3}: {per3}%, Total Votes : ({count3})\n")
    text.write("---------------------\n")
    text.write(f"Winner: {topCandidate}\n")
    text.write("---------------------")