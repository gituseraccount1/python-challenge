# Create file path across operating systems   
import os

# Module for reading CSV file
import csv

# Finds the CVS file needed for this
csvpath = os.path.join("Resources", "budget_data.csv")

# Holds the number of month as it counts
monthCount = 0
# Holds the net total
netTotal = 0
# Empty list which will evetually hold all the changes in Profit/Loss over the entire period
changeList = []
# Empty list which will eventualy hold all the months
monthList = []

# Open and read csv
with open(csvpath) as csv_file:
    # CSV reader specifies delimiter and varuables it holds
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read through each row of data after the header
    csv_header = next(csv_file)
    #print(f'Header: {csv_header}')

    for row in csv_reader:
        #print(row)

        # Count each month for the total month count
        monthCount += 1

        # Adds the previous net total (if any) and add it to the current row net total
        netTotal = netTotal + int(row[1])

        # Appending each month 
        monthList.append(row[0])

        # This loops works when row equals 2, since the header was skip and I want to compare the 3rd profit/loss to the second one to find the difference
        if monthCount > 1:
            # 
            change = int(row[1]) - previousValue
            changeList.append(change)

        # outside of the if condition, since this will hold the 2nd row's profit/loss for the first time so when if statement above runs, it can help calculated the difference betweem the 3rd minus 2nd profit/loss amount... then this will continue correctly  
        previousValue = int(row[1])
        

# This helps find the average change overall by adding everything in the changeList divided by the count of the change list. 
averageChange = round(sum(changeList) / len(changeList), 2)
# This helps find the max increased  in the ChangeList
maxIncrease = max(changeList)
# This helps find the min decreased in the ChangeList
maxDecrease = min(changeList)

# Finds the index of the max increase  
maxIndex = changeList.index(maxIncrease)
#Takes the month and day corresponding to the max increase, but I needed to add 1 to get the correct month and day
maxIncreaseMonth = monthList[maxIndex+1] 

# Finds the index of the max decrease 
minIndex = changeList.index(maxDecrease)    
# Takes the month and day corresponding to the max increase, but I needed to add 1 to get the correct month and day
maxDecreaseMonth = monthList[minIndex+1]   

# Prints final results per the challenge
print('Financial Analysis')
print("----------------------------")
print(f'Total months: {monthCount}')
print(f'Total: ${netTotal}')
print(f"Average Change: ${averageChange}")
print(f'Greatest Increase in Profits: {maxIncreaseMonth} ${maxIncrease}')
print(f'Greatest Decrease in Profits: {maxDecreaseMonth} ${maxDecrease}')


# creates a text file name budget anaylsis.txt with the information
output_path = os.path.join("analysis", "budget_anaylsis.txt")
with open(output_path, "w") as output_file:
    output_file.write(f'Financial Analysis\n')
    output_file.write(f"----------------------------\n")
    output_file.write(f'Total months: {monthCount}\n')
    output_file.write(f'Total: ${netTotal}\n')
    output_file.write(f"Average Change: ${averageChange}\n")
    output_file.write(f'Greatest Increase in Profits: {maxIncreaseMonth} ${maxIncrease}\n')
    output_file.write(f'Greatest Decrease in Profits: {maxDecreaseMonth} ${maxDecrease}')