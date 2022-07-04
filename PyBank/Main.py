#Pybank main
import csv
import os

def formatMoney(amount):
    return "${:,.2f}".format(amount)

#GrabData = os.path.join("Resources","budget_data.csv")
GrabData = "C:/Users/MattM/Desktop/GaTech Boot Camp/assignments/Lesson 3/Python-challenge/PyBank/Resources"


#Makeing output file
 
#outputfile_PyBank = os.path.join("analysis","Outputfile_PyBank")
outputfile_PyBank = "C:/Users/MattM/Desktop/GaTech Boot Camp/assignments/Lesson 3/Python-challenge/PyBank"


#--- got the files ----

#Tasked to create a Python script that analyzes the records to calculate each of the following:

    # 1.The total number of months included in the dataset

    # 2.The net total amount of "Profit/Losses" over the entire period

    # 3.The changes in "Profit/Losses" over the entire period, and then the average of those changes

    # 4.The greatest increase in profits (date and amount) over the entire period

    # 5.The greatest decrease in profits (date and amount) over the entire period


# Make all variables set data type

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

    f" \n"
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonthsCount}\n"
    f"Total:{formatMoney(NetToatlProfit_Loss)}\n"
    f"Average Change:{formatMoney(Profit_Loss_change)}\n"
    f"Greatest Increase in Profits: {maxIncDate} {formatMoney(maxIncrease)}\n"
    f"Greatest Increase in Profits: {maxDecDate} {formatMoney(maxDecrease)}\n"
 
)



print(output)


#Exporting output to a text file.

with open(outputfile_PyBank, "w") as textfile:
    textfile.write(output)
