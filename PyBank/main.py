import csv


with open("./Resources/budget_data.csv", newline="") as csvfile:
    rows = csv.reader(csvfile)
    totMonths = 0
    netPL = 0
    greatestProfit = 0
    greatestLoss = 0
    next(rows)
    for row in rows:
        totMonths+=1
        profitLoss = int(row[1])
        netPL+= profitLoss
        if greatestProfit < profitLoss:
            greatestProfit = profitLoss
        if greatestLoss > profitLoss:
            greatestLoss = profitLoss
    
    print("\nFinancial Analysis\n----------------------------")
    print(f"Total Months: {totMonths}")
    print(f"Total: ${netPL}")
    print("Average Change: $%.2f" % (float(netPL)/totMonths))
    print(f"Greatest Increase in Profits: ${greatestProfit}")
    print(f"Greatest Decrease in Profits: ${greatestLoss}")