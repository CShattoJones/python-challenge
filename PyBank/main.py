import os
import csv
BudgetData_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(BudgetData_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
   
    # Loop through the data
    for row in csvreader:
        print(row)
           
 
# print (len(csvfile))
# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period
