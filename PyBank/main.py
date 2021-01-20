import os
import csv
BudgetData_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(BudgetData_csv, 'r', newline='') as csvfile:

    # Instantiate csv reader and split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove header from the usable data
    header = next(csvreader)
   
    # Loop through the data
    for row in csvreader:

        # Assign variables to discrete data and assign profits/losses as float
        months = row[0]
        profits_losses = float(row[1]) 
       
        # Find total number of months 
        

        # The net total amount of "Profit/Losses" over the entire period
        net_profits_losses += profits_losses
        print(net_profits_losses)

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period
