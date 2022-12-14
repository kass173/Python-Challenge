# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Your analysis should look similar to the following:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# First need to import the os module
# To allow us to create file paths across operating systems
import os

# Module to read CSV files
import csv

# Module for statistics - help us do math!
import statistics

# here's my bank data - it's within resources folder on desktop and in git repo same level as main.py
csvpath = "./resources/budget_data.csv"


monthCount = 0
totalVolume = 0
averageChange = 0
greatestIncrease = 0
bestMonth = ''
greatestDecrease = 0
worstMonth = ''



change = []
monthToMonthChange = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        monthCount += 1
       
        currentVolume =int(row[1])
        previousVolume = 0
        totalVolume += currentVolume
        if len(change) >0:
            previousVolume =change[-1]
        if  currentVolume - previousVolume > greatestIncrease:
            bestMonth = (row[0])
            greatestIncrease = currentVolume - previousVolume
        elif currentVolume - previousVolume < greatestDecrease:
            worstMonth = (row[0])
            greatestDecrease = currentVolume - previousVolume
        change.append(currentVolume)
       

  
# track monthly changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)   

averageChange = statistics.mean(monthToMonthChange)

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(monthCount))
print("Total: $" + str(totalVolume))
print("Average Change is: $" + str(round(averageChange, 2)))
print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

# now write this to an output file
f = open("./Analysis/financial_analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("___________________________________\n")

f.write("Total Months: " + str(monthCount)+"\n")
f.write("Total: $" + str(totalVolume)+"\n")
f.write("Average Change is: $" + str(round(averageChange, 2))+"\n")
f.write("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")\n")
f.write("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")



