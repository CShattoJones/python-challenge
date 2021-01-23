import os
import csv
BudgetData_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(BudgetData_csv, 'r', newline='') as csvfile:

    # Instantiate csv reader and split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove header from the usable data
    header = next(csvreader)

    months = []
    profits_losses = []  
    # Loop through the data
    for row in csvreader:


        # Find total number of months  
        months.append(row[0])

        # The net total amount of "Profit/Losses" over the entire period
        profits_losses.append(int(row[1]))
     

    all_months = len(months)
    print(all_months)
    
    # print(profits_losses)
    net_profits_losses = sum(profits_losses)
    print(net_profits_losses)

# go to the next element and subtract the previous element from it.
    for index, value enumerate profits_losses:
   
        print(profits_losses)



   # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period
