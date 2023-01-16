# import modules for CSV
import os
import csv

# ----------------------------------------- INSTRUCTIONS -------------------------------------------------
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire periodo
# --------------------------------------------------------------------------------------------------------



#  ----------------------------------------- LIST CREATION -----------------------------------------------
# stores each month
total_month = []

# stores each profit value
total_profit = []

# stores the change in profit from one month to the next
monthly_change_profit = []
#---------------------------------------------------------------------------------------------------------



#----------------------------------------- BEGIN ANALYSIS ------------------------------------------------
# define path for CSV file
csvpath = os.path.join("/Users/calebsteeves/Desktop/python-challenge/PyBank/Resources/budget_data.csv")

# Read in the CSV file
with open(csvpath) as csv_file:

    #split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)

    # print(f'Header:{csv_header}')

    # 'for loop' to search through rows 
    for row in csv_reader:

        # Appending the total_month list. Loop will add each "month" value into the list
        total_month.append(row[0])
        
        # Appending the total profit list. loop will add each "profit" value into the list
        total_profit.append(int(row[1]))

# verified that both list were filled in properly
    # print(*total_month, sep = ",")
    # print(total_profit, sep = ",")

    # interate through the list of profits and subtract the next item (x+1) from the current item (x) in the list
    # Need to use "-1" otherwise we get "list index out of range". 
    # There are 86 values in the "total_profit list" however since our loop looks ahead one value we need it to stop at 85
    for x in range(len(total_profit)-1):
        monthly_change_profit.append(total_profit[x+1]-total_profit[x])

# verified that the list filled out properly        
    # print(*monthly_change_profit, sep=",")
    # print(len(monthly_change_profit))

# get the max profit change value from the list
max_profit = max(monthly_change_profit)

# get the min profit change value from the list
min_profit = min(monthly_change_profit)

# Create an variable to hold the index of the month that corresponds with the max/min profit change. 
# Need to add 1 to the index otherwise you will get the previous month.
max_month_index = monthly_change_profit.index(max(monthly_change_profit))+1
min_month_index = monthly_change_profit.index(min(monthly_change_profit))+1

# create a variable to hold the name of the month for the above index
max_increase_month = {total_month[max_month_index]}
min_decrease_month = {total_month[min_month_index]}

# print(max_increase_month)
# print(min_decrease_month)
# ---------------------------------------------------------------------------------------------------------------

# --------------------------------------------- PRINT SUMMARY ---------------------------------------------------
# print each of the following variables.
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_month)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_change_profit)/len(monthly_change_profit),2)}")
print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_profit))})")
print(f"Greatest Decrease in Profits: {min_decrease_month} (${(str(min_profit))})")
# ---------------------------------------------------------------------------------------------------------------

# ----------------------------------------- OUTPUT SUMMARY ------------------------------------------------------
# identify output file location
output_file = os.path.join("/Users/calebsteeves/Desktop/python-challenge/PyBank/analysis/budget.txt")

# open output file and write to it.
with open(output_file, "w") as final_output:

    final_output.write("Financial Analysis")

    final_output.write("----------------------------\n")

    final_output.write(f"Total Months: {len(total_month)}\n")

    final_output.write(f"Total: ${sum(total_profit)}\n")

    final_output.write(f"Average Change: ${round(sum(monthly_change_profit)/len(monthly_change_profit),2)}\n")

    final_output.write(f"Greatest Increase in Profits: {max_increase_month} ${max_profit}\n")

    final_output.write(f"Greatest Decrease in Profits: {min_decrease_month} ${min_profit}\n")
# ---------------------------------------------------------------------------------------------------------------