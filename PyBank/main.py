# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader, None)  

    # Set starting variables before looping through rows...
    # Variable to hold total profits:
    sum_profits = 0
    # Lists to hold names of months and profits:
    months = []
    profits = []

    # Loop through rows in csv file
    for row in csvreader:
        # Define and add month and profit/loss to respective lists
        month = row[0]
        profit = row[1]
        months.append(month)
        profits.append(profit)

        # Add profit/loss for month to total
        sum_profits += int(profit)
    # End loop through rows

    # Set number of increases/decreases over months
    number_of_changes = len(profits) - 1

    # Set starting variables before looping through profits...
    # Variable to hold the total $ amount of changes (use to calculate average):
    sum_changes = 0
    # Variables to hold greatest $ increase and greatest $ decrease:
    highest_change = 0
    lowest_change = 0

    # Loop through list of profits
    for i in range(number_of_changes):
        # Increase/decrease = difference between next profit in list and current in list
        change = int(profits[i+1]) - int(profits[i])

        # Add to total changes
        sum_changes += change

        # Set greatest increase/decrease as applicable, and retrieve corresponding month
        if change > highest_change:
            highest_change = change
            highest_change_month = months[i+1]
        elif change < lowest_change:
            lowest_change = change
            lowest_change_month = months[i+1]
    # End loop through profits
        
    # Calculate average change
    average_change = round(sum_changes / number_of_changes, 2)

    # Calculate number of months
    number_of_months = len(months)

    # Output message
    output = ("Financial Analysis\n"
              "----------------------------\n"
              f'Total Months: {number_of_months}\n'
              f'Total: ${sum_profits}\n'
              f'Average Change: ${average_change}\n'
              f'Greatest Increase in Profits: {highest_change_month} (${highest_change})\n'
              f'Greatest Decrease in Profits: {lowest_change_month} (${lowest_change})\n')
    
    # Set output file path
    output_path = os.path.join("Analysis","financial_analysis.txt")

    # Write output to text file
    with open(output_path, "w") as txtfile:
        txtfile.write(output)

    # Print output to terminal
    print(output)