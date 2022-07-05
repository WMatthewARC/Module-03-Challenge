#Pybank main

import csv
import os

def formatMoney(amount):
    return "${:,.2f}".format(amount)

#GrabData = os.path.join("Resources","budget_data.csv")
GrabData = "C:/Users/MattM/Documents/GitHub/Module-03-Challenge/PyBank/Resources/budget_data.csv"

#Makeing output file
 
#outputfile_PyBank = os.path.join("analysis","Outputfile_PyBank")
outputfile_PyBank = "C:/Users/MattM/Documents/GitHub/Module-03-Challenge/PyBank/analysis/Outputfile_PyBank.txt"


totalMonthsCount = 0

NetToatlProfit_Loss = 0 
Profit_Loss_change = 0

previous = 0
change = 0
changeSum = 0

maxIncrease = 0
maxDecrease = 0
maxIncDate = ""
maxDecDate = ""

#Read the file to use it

with open(GrabData) as budgetData:
    csvreader = csv.reader (budgetData,delimiter=",")
    header = next(csvreader)

    for row in csvreader: 

        totalMonthsCount += 1
        value = int(row[1])
        NetToatlProfit_Loss += value

        change = value - previous if previous != 0 else 0
        changeSum += change
        previous = value
        maxIncrease = max(maxIncrease, change)
        if maxIncrease == change:
            maxIncDate = row[0]
        maxDecrease = min(maxDecrease, change)
        if maxDecrease == change:
            maxDecDate = row[0]

    Profit_Loss_change = changeSum/(totalMonthsCount-1)


# start output 
output = (

    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonthsCount}\n"
    f"Total:{formatMoney(NetToatlProfit_Loss)}\n"
    f"Average Change:{formatMoney(Profit_Loss_change)}\n"
    f"Greatest Increase in Profits: {maxIncDate} {formatMoney(maxIncrease)}\n"
    f"Greatest Decrease in Profits: {maxDecDate} {formatMoney(maxDecrease)}\n"
 
)

print(output)

#Exporting output to a text file

with open(outputfile_PyBank, "w") as textfile:
    textfile.write(output)