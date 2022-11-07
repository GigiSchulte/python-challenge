#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)



#imported modules
import csv
import os

budgetData = os.path.join("Resources","budget_data.csv") #source file

outputFile = os.path.join("analysis","budgetanalysis.txt")
#variables
totalMonths = 0
totalRevenue = 0
monthlyChange = []
months = []


with open(budgetData) as file: 
    csvReader = csv.reader(file) 
    header = next(csvReader)

    firstRow = next(csvReader) #get starting row for change calc
    totalMonths += 1 #calc total months
    totalRevenue += float(firstRow[1]) #calc revenue
    prevRevenue = float(firstRow[1]) #get initial amount
    
    for row in csvReader:
        totalMonths += 1 #calc total months
        totalRevenue += float(row[1]) #calc revenue
        netChange = float(row[1]) - prevRevenue #calc net change
        monthlyChange.append(netChange) #add to monthlyChange list
        months.append(row[0]) #first month a change occured
        prevRevenue = float(row[1])


avgChange = sum(monthlyChange) / len(monthlyChange)

greatestIncrease = [months[0], monthlyChange[0]] #month of greatest increase
greatestDecrease = [months[0], monthlyChange[0]] #month of greatest decrease

for m in range(len(monthlyChange)):
    if(monthlyChange[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChange[m]
        greatestIncrease[0] = months[m]

    if(monthlyChange[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChange[m]
        greatestDecrease[0] = months[m]


output = (
    f"\nFinancial Analysis \n"
    f"---------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${totalRevenue:,.2f}\n"
    f"Average Change: ${avgChange:,.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} ${greatestIncrease[1]:,.2f})\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} ${greatestDecrease[1]:,.2f})"
    )
print(output)

with open(outputFile,"w") as textfile:
    textfile.write(output)