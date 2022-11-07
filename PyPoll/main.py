#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------

import csv
import os

inputFile   = os.path.join("Resources","election_data.csv") #path to csv file
outputFile = os.path.join("electionanalysis.txt") #path to output file

#Variables
totalVotes = 0 #variable to hold # of votes
candidates = [] #variable to hold cadidates
candiateVotes = {} #variable to hold cadidate votes
winningCount = 0 #holds the winner count
winner = ""


with open(inputFile) as electionData:
    csvreader = csv.reader(electionData)
    header = next(csvreader)
    #index 0 = ballot ID
    #index 1 = county
    #index 2 = candidate
    for row in csvreader:
        totalVotes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candiateVotes[row[2]] = 1
        else:
            candiateVotes[row[2]] += 1

voterOutput = ""

for candidate in candiateVotes:
    votes = candiateVotes.get(candidate)
    votePct = (float(votes) / float(totalVotes)) * 100
    voterOutput += f"{candidate}: {votePct:.2f}% ({totalVotes:,})\n"
    if votes > winningCount:
        winningCount = votes
        winner = candidate

output = (
    f"\t\tElection Results\n"
    f"----------------------------------------------\n"
    f"Total Votes: {totalVotes:,}\n"
    f"{voterOutput}\n"
    f"----------------------------------------------\n"
    f"Winner: {winner} with {winningCount:,} votes\n"
    f"----------------------------------------------\n"
)

print(output)

with open(outputFile,"w") as textFile:
    textFile.write(output)