# Create file path across operating systems   
import os

# Module for reading CSV file
import csv


csvpath = os.path.join("Resources", "election_data.csv")

# To hold total votes overall
totalVotes = 0

# This will eventually grabs the ballet ID and attaches it to the person they voted for
canidatesTotalVotesDictionary = {'Charles Casper Stockham': [],
                 'Diana DeGette': [],
                 'Raymon Anthony Doane': []}

# This will eventially hold just a single number with how many votes each candiates received
canidatesTotalVotes = {'Charles Casper Stockham': [],
                 'Diana DeGette': [],
                 'Raymon Anthony Doane': []}

# Open and read csv
with open(csvpath) as csv_file:
    # CSV reader specifies delimiter and varuables it holds
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read through each row of data after the header
    csv_header = next(csv_file)
    #print(f'Header: {csv_header}')

    # Loops through each row 
    for row in csv_reader:

        # This will keep track of each row the loop goes through, which will total to the number of votes overall
        totalVotes += 1

        # This will grab the candiates name and use it in the next 3 if statemnts
        canidateName = row[2]
        
        # Compares the canidateName (above) if it is equal to Charles Casper Stockham
        if canidateName == 'Charles Casper Stockham':
            # If the above condition is true, the ballot ID will be added to the canidatesTotalVotesDictionary for Charles Casper Stockham
            canidatesTotalVotesDictionary['Charles Casper Stockham'].append(int(row[0]))

        # Compares the canidateName (above) if it is equal to Diana DeGette
        if canidateName == 'Diana DeGette':
            # If the above condition is true, the ballot ID will be added to the canidatesTotalVotesDictionary for Diana DeGette
            canidatesTotalVotesDictionary['Diana DeGette'].append(int(row[0]))

        # Compares the canidateName (above) if it is equal to Raymon Anthony Doane
        if canidateName == 'Raymon Anthony Doane':
            # If the above condition is true, the ballot ID will be added to the canidatesTotalVotesDictionary for Raymon Anthony Doane
            canidatesTotalVotesDictionary['Raymon Anthony Doane'].append(int(row[0]))

# This counts the length of the list for Charles Casper Stockham in the canidatesTotalVotesDictionary. In other words, number of votes for Charles Casper Stockham.
CharlesCasperStockhamCount = len(canidatesTotalVotesDictionary['Charles Casper Stockham'])
# This appends the length number above to the canidatesTotalVotes dictionary for Charles Casper Stockham
canidatesTotalVotes['Charles Casper Stockham'].append(CharlesCasperStockhamCount)

# This counts the length of the list for Diana DeGette in the canidatesTotalVotesDictionary. In other words, number of votes for Diana DeGette.
DianaDeGetteCount = len(canidatesTotalVotesDictionary['Diana DeGette'])
# This appends the length number above to the canidatesTotalVotes dictionary for Diana DeGette
canidatesTotalVotes['Diana DeGette'].append(DianaDeGetteCount)

# This counts the length of the list for Raymon Anthony Doane in the canidatesTotalVotesDictionary. In other words, number of votes for Raymon Anthony Doane.
RaymonAnthonyDoaneCount = len(canidatesTotalVotesDictionary['Raymon Anthony Doane'])
# This appends the length number above to the canidatesTotalVotes dictionary for Raymon Anthony Doane
canidatesTotalVotes['Raymon Anthony Doane'].append(RaymonAnthonyDoaneCount)

# This is the percentage of votes Charles received
CharlesCasperStockhamPercentage = round((CharlesCasperStockhamCount / totalVotes) * 100, 3)
# This is the percentage of votes Diana received
DianaDeGettePercentage = round((DianaDeGetteCount / totalVotes) * 100, 3)
# This is the percentage of votes Raymond received
RaymonAnthonyDoanePercentage = round((RaymonAnthonyDoaneCount / totalVotes) * 100, 3)


# This finds the max number in the canidatesTotalVotes dictionary and returns the corrsponding key (which is the canidate's name)
winner = max(canidatesTotalVotes, key=canidatesTotalVotes.get)

# prints out election results in the terminal
print('Election Results')
print("----------------------------")
print(f'Total Votes: {totalVotes}')
print("----------------------------")
print(f'Charles Casper Stockham: {CharlesCasperStockhamPercentage}% ({CharlesCasperStockhamCount})')
print(f"Diana DeGette: {DianaDeGettePercentage}% ({DianaDeGetteCount})")
print(f'Raymon Anthony Doane: {RaymonAnthonyDoanePercentage}% ({RaymonAnthonyDoaneCount})')
print("----------------------------")
print(f'Winner: {winner}') 

# creates a text file name election results.txt with the results
output_path = os.path.join("anaylsis", "election_results.txt")
with open(output_path, "w") as output_file:
    output_file.write('Election Results\n')
    output_file.write("----------------------------\n")
    output_file.write(f'Total Votes: {totalVotes}\n')
    output_file.write("----------------------------\n")
    output_file.write(f'Charles Casper Stockham: {CharlesCasperStockhamPercentage}% ({CharlesCasperStockhamCount})\n')
    output_file.write(f"Diana DeGette: {DianaDeGettePercentage}% ({DianaDeGetteCount})\n")
    output_file.write(f'Raymon Anthony Doane: {RaymonAnthonyDoanePercentage}% ({RaymonAnthonyDoaneCount})\n')
    output_file.write("----------------------------\n")
    output_file.write(f'Winner: {winner}') 