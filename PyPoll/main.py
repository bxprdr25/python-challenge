# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2,218,231)
# Correy: 20.000% (704,200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

import os
import csv

totalVotes = 0
candidateTotalVotes = []
candidates = []
winVotes = 0

outputPath = os.path.join(r"C:\Users\bxprd\Data Analytics Bootcamp\Git_Repos\python-challenge\PyPoll\Analysis\PyPoll")
election_csv = os.path.join(".", "Resources", "election_data.csv")

#with statement to open the csv file
with open(election_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Reading the header row
    csv_header = next(csv_reader)

    # iterate through each row of data after the header in the csv file
    for column in csv_reader:

        #aggregate the total votes
        totalVotes += 1

        #set candidateTransfer list = to values in column 2 in the csv file
        candidateTransfer = column[2]

        #conditional to test if information in candidateTransfer list is in the candidates list
        if candidateTransfer not in candidates:

           #Append to the candidates list from the candidateTransfer list & add 1 if a new candidate is found
            candidates.append(candidateTransfer)
            candidateTotalVotes.append(1)

        #if candidates is already in candidates list, find index of that candidate in the list to keep track of all votes
        else:
            indexofCandidate = candidates.index(candidateTransfer)
            voteTotal = candidateTotalVotes[indexofCandidate]
            candidateTotalVotes[indexofCandidate] = voteTotal + 1

    #Print to terminal the results
    print(f"Election Results")
    print(f"------------------")
    print(f"Total Votes: {str(totalVotes)}")
    print(f"------------------")

    #iterate through the list to calculate % of votes, total votes & determine the winner.
    for candidateTransfer in candidates:

        voteCount = candidateTotalVotes[(candidates.index(candidateTransfer))]
        percentWonVotes = float(voteCount / totalVotes) * 100

        if voteCount > winVotes:
            winningCandidate = candidateTransfer
            winVotes = voteCount

        print((candidateTransfer + ": " + str(round(percentWonVotes, 2)) + "00%" + " (" + str(voteCount) + ")"))

    print(f"------------------")
    print(f"Winner: {str(winningCandidate)}")

#save a text file of the results to analysis folder
with open(outputPath, "w", newline='') as textfile:
    print(f"Election Results", file=textfile)
    print(f"------------------", file=textfile)
    print(f"Total Votes: {str(totalVotes)}", file=textfile)
    print(f"------------------", file=textfile)
    for candidateTransfer in candidates:

        voteCount = candidateTotalVotes[(candidates.index(candidateTransfer))]
        percentWonVotes = float(voteCount / totalVotes) * 100

        if voteCount > winVotes:
            winningCandidate = candidateTransfer
            winVotes = voteCount

        print((candidateTransfer + ": " + str(round(percentWonVotes, 2)) + "00%" + " (" + str(voteCount) + ")"), file=textfile)

    print(f"------------------", file=textfile)
    print(f"Winner: {str(winningCandidate)}", file=textfile)