# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

totalMonths = 1
plTotal = 0
plChanges = 0
profitValue = 0
plDiff = []
date = []

outputPath = os.path.join(r"C:\Users\bxprd\Data Analytics Bootcamp\Git_Repos\python-challenge\PyBank\Analysis\PyBank")
budget_csv = os.path.join(r"C:\Users\bxprd\Data Analytics Bootcamp\Git_Repos\python-challenge\PyBank\Resource\budget_data.csv")
print(budget_csv)

with open(budget_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Reading the header row
    csv_header = next(csv_reader)

    #Reading the row after the header row
    nextRow = next(csv_reader)
    #print(nextRow)

    #Set Profit Value and plTotal = to the first row in column 2 (index 1)
    profitValue = int(nextRow[1])
    #print(profitValue)
    plTotal = int(nextRow[1])
    #print(plTotal)

    #startPoint = str(nextRow[0])
    #date.append(startPoint)

    # Read through each row of data after the header
    for column in csv_reader:

        #append the dates from the CSV to a dates list
        date.append(column[0])
        #print(date)

        #aggregate the total months and the total profit & loss

        totalMonths += 1
        #print(totalMonths)
        plTotal += int(column[1])

        #Calculate the difference between the first 2 values and append it to a new list
        plChanges = int(column[1]) - profitValue
        plDiff.append(plChanges)
        #print(plDiff)
        profitValue = int(column[1])
        avgChange = round(sum(plDiff) / len(plDiff), 2)

        # Greatest increase in profits
        increase = max(plDiff)
        #print(increase)
        bestIndex = plDiff.index(increase)
        #print(bestIndex)
        greatDate = date[bestIndex]

        # Greatest decrease (lowest increase) in profits
        decrease = min(plDiff)
        # print(increase)
        bestIndex = plDiff.index(decrease)
        # print(bestIndex)
        worstDate = date[bestIndex]

    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {str(totalMonths)}")
    print(f"Total: {str(plTotal)}")
    print(f"Average Change: {str(avgChange)}")
    print(f"Greatest Increase in Profits: {greatDate} - (${str(increase)})")
    print(f"Greatest Decrease in Profits: {worstDate} - (${str(decrease)})")
    print(f"------------------")

with open(outputPath, "w", newline='') as textfile:
    print(f"Financial Analysis", file=textfile)
    print(f"------------------", file=textfile)
    print(f"Total Months: {str(totalMonths)}", file=textfile)
    print(f"Total: {str(plTotal)}", file=textfile)
    print(f"Average Change: {str(avgChange)}", file=textfile)
    print(f"Greatest Increase in Profits: {greatDate} - (${str(increase)})", file=textfile)
    print(f"Greatest Decrease in Profits: {worstDate} - (${str(decrease)})", file=textfile)
    print(f"------------------", file=textfile)