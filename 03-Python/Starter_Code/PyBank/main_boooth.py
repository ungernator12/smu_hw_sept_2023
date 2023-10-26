# Modules
import os
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# variables
total_months = 0
total_profit_loss = 0

# vars for the changes
changes = []
last_profit_loss = 0

max_change = -999999999
min_change = 999999999
max_month = ""
min_month = ""

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        # changes
        # if first row, no change, but assign last_profit_loss
        # else, calculate the change

        if total_months != 0:
            change = int(row[1]) - last_profit_loss
            changes.append(change)

            # check max/min change
            if change > max_change:
                max_change = change
                max_month = row[0]
            elif change < min_change:
                min_change = change
                min_month = row[0]
            else:
                pass # do nothing, not a max/min change

        # assign last month profit
        last_profit_loss = int(row[1])

        # add 1 to a month counter
        total_months = total_months + 1

        # add the profit loss to the variable
        total_profit_loss = total_profit_loss + int(row[1])

# print out KPIs
print(total_months)
print(total_profit_loss)

avg_change = sum(changes) / len(changes)
print(avg_change)

print(max_change)
print(max_month)
print(min_change)
print(min_month)

# create output
with open("output_booth.txt", "w") as txt_file:
    output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""

    txt_file.write(output)
