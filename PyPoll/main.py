import os
import csv
from datetime import datetime

# get timestamp for output file
now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")

# get the resource file based on the PWD
csvName = "election_data.csv"
resultsName = "ANALYSIS_PyPoll_" + csvName + "_" + dt_string + ".txt"

# Init results variable
totalvotes=0
candidate=[]
voteCount=[]

# initialise file paths
csvpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Resources', csvName)
resultspath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'analysis', resultsName)

print(f"Input file: {csvpath}")

with open(csvpath, encoding="utf8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Loop through votes
    for row in csvreader:
        # increment votes
        totalvotes = totalvotes + 1

        # Add to the candidate's vote otherwise create new candidate if not existing
        if row[2] in candidate:
            # add to candidate's vote
            voteCount[candidate.index(row[2])] = int(voteCount[candidate.index(row[2])]) + 1
        else:
            # create candidate and vote qty list
            candidate.append(row[2])
            voteCount.append(1)

# build result text header
resultText = "\nElection Results " \
    + "\n-------------------------" \
    + "\nTotal Votes: " + str(totalvotes) \
    + "\n-------------------------\n"

# build result candidates total
for i in (range(len(candidate))):
    percentage = round(((voteCount[i]/totalvotes) * 100),3)
    resultText = resultText + candidate[i] + ": " +  "{:.3f}".format(percentage) + "% (" + str(voteCount[i]) + ")\n"

# build result text footer
resultText = resultText \
    + "-------------------------" \
    + "\nWinner: " + candidate[voteCount.index(max(voteCount))] \
    + "\n-------------------------\n"

# create the results file
f= open(resultspath,"w+")

# write the results in a file
f.write(resultText)
f.close

# print the results on screen
print(resultText)
print("\n Output File Name: " + resultspath + "\n")