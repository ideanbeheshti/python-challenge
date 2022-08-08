import os 
import csv

csvpath = os.path.join('..','Resources', 'budget_data.csv')

#CSV Values to add

total_months = []
net_profit = []
profit_change = []

#Opening csv file 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    #Importing the correct values
    for row in csvreader:
            total_months.append(row[0])
            net_profit.append(int(row[1]))

    for i in range(len(net_profit)-1):
            profit_change.append(net_profit[i+1]-net_profit[i])


#Summarize max and min from values
increase = max(profit_change)
decrease = min(profit_change)

#Obtain the max and min for monthly change

monthly_increase = profit_change.index(max(profit_change)) + 1
monthly_decrease = profit_change.index(min(profit_change)) + 1

#Print Statements

print("Financial Analysis")
print("-------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(net_profit)}")
print(f"Average Change:{round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(decrease))})")

#exporting to text file of printed results

output = "output.txt"

with open("output","w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("--------------------")
    new.write("\n")
    new.write(f"Total Months:{len(total_months)}")
    new.write("\n")
    new.write(f"Total: ${sum(net_profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(increase))})") 

