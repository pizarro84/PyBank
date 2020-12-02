import os
import csv
from datetime import datetime

# get timestamp for output file
now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")

# get the resource file based on the PWD
csvName = "budget_data.csv"
resultsName = "ANALYSIS_" + csvName + "_" + dt_string + ".txt"

# Init results variable
totalmonths=0
total=0
current=0   
previous=0
totChange=0
greatestInc=['',0]
greatestDec=['',0]

csvpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Resources', csvName)
resultspath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'analysis', resultsName)

# Method 2: Improved Reading using CSV module
with open(csvpath, encoding="utf8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read the header row first (skip this step if there is now header)
    first_row = next(csvreader)
    previous = int(first_row[1])

    for row in csvreader:
        # increment total months
        totalmonths = totalmonths + 1

        # get total profit / loss
        total = total + int(row[1])

        # get change values
        current = int(row[1])
        change = current - previous
        totChange = totChange + change # add change to total change for the average

        # get the greatest increase and decrease
        if change > int(greatestInc[1]):
            greatestInc = [row[0],str(change)]
        elif change < int(greatestDec[1]):
            greatestDec = [row[0],str(change)]

        previous = current # update preveious for next cycle


#run avechg formula
aveChg = totChange/totalmonths

# load the result text in a variable
line1 = "\n Financial Analysis " \
        + "\n ----------------------------" \
        + "\n Total Months: " + str(totalmonths) \
        + "\n Total: " + str(total) \
        + "\n Average  Change: $ " + str(round(aveChg,2)) \
        + "\n Greatest Increase in Profits: " + greatestInc[0]+ " $(" + greatestInc[1] + ")" \
        + "\n Greatest Decrease in Profits: " +greatestDec[0]+ " $(" + greatestDec[1] + ")"

# create the results file
f= open(resultspath,"w+")

# write the results in a file
f.write(line1)
f.close

# print the results on screen
print(line1)
print("\n Output File Name: " + resultspath + "\n")