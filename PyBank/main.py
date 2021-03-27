import csv


with open("./Resources/budget_data.csv", newline="") as csvfile:
    with open("./Analysis/results.txt", 'w') as resultfile:
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
        
        resultfile.write("Financial Analysis\n----------------------------\n")
        resultfile.write(f"Total Months: {totMonths}\n")
        resultfile.write(f"Total: ${netPL}\n")
        resultfile.write("Average Change: ${:.2f}\n".format(float(netPL)/totMonths))
        resultfile.write(f"Greatest Increase in Profits: ${greatestProfit}\n")
        resultfile.write(f"Greatest Decrease in Profits: ${greatestLoss}\n")
    print("\nFinancial Analysis\n----------------------------")
    print(f"Total Months: {totMonths}")
    print(f"Total: ${netPL}")
    print("Average Change: ${:.2f}\n".format(float(netPL)/totMonths))
    print(f"Greatest Increase in Profits: ${greatestProfit}")
    print(f"Greatest Decrease in Profits: ${greatestLoss}")