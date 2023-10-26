# Modules
import os
import csv

# Set path for file
csvpath = "Resources/election_data.csv"

#variables
total_votes = 0
cand_dict = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)

        #add 1 to month counter
        total_votes += 1

        #get candidates
        #if candidates trapped in dictionary, value+1
        #else add to dict with value=1
        candidate = row[2]

        if candidate in cand_dict.keys():
            cand_dict[candidate] += 1
        else:
            cand_dict[candidate] = 1

#print(total_votes)
#print(cand_dict)

#Variable
#loop candidates
#more votes then update variable

winning_votes = 0
winning_candidate = ""

for cand in cand_dict.keys():
    votes = cand_dict[cand]

    #verify if more votes than previous candidate
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = cand

#print(winning_candidate, winning_votes)

####################################################################################################

# create output
output = f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------\n"""

for key in cand_dict.keys():
    perc = round(100*cand_dict[key]/total_votes, 3)
    newline = f"{key}: {perc}% ({cand_dict[key]})\n"
    output += newline

lastline = f"""
----------------------------
Winner: {winning_candidate}
----------------------------
"""

output += lastline
print(output)

# create txt
with open("pypoll_output_JU.txt", "w") as txt_file:
    txt_file.write(output)