import os
import csv

# --------------------------------------------- INSTRUCTIONS ----------------------------------------------------
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# ------------------------------------------ LIST CREATION ---------------------------------------------------
total_votes = []
candidates = []
unique_candidates = []
votes_cs = []
votes_dg = []
votes_rd = []

# ------------------------------------------- ANALYSIS -------------------------------------------------------

# determine path to CSV file
csvpath = os.path.join("Resources","election_data.csv")

# open CSV file and read it in
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    # print(f'header:{csv_header}')
    
# iterate through rows add ballot values to total_votes and candidate names to cadidates
    for row in csv_reader:
        total_votes.append(row[0])
        candidates.append(row[2])
    # print(len(total_votes))

# iterate through the candidates list and add unique values to the unique_candidates list
    for x in candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)
    # print(*unique_candidates, sep=",")

# iterate through candidates list if match to candidate is found, add to that candidates vote count
    for x in candidates:
        if x == "Charles Casper Stockham":
            votes_cs.append(x)
        elif x == "Diana DeGette":
            votes_dg.append(x)
        elif x == "Raymon Anthony Doane":
            votes_rd.append(x)
    # print(len(votes_cs))
    # print(len(votes_dg))
    # print(len(votes_rd))

# create variables for percent of votes each candidate won
vote_percent_cs = round((len(votes_cs)/len(candidates))*100,3)
vote_percent_dg = round((len(votes_dg)/len(candidates))*100,3)
vote_percent_rd = round((len(votes_rd)/len(candidates))*100,3)
# print(vote_percent_cs)
# print(vote_percent_dg)
# print(vote_percent_rd)

# creating dictionary to hold % of votes as the key and candidate name
poll = {vote_percent_cs: "Charles Casper Stockham", vote_percent_dg: "Diana DeGette", vote_percent_rd: "Raymon Anthony Doane"}
# declaring variable for winner for finding the highest % of votes.
winner = max(vote_percent_cs, vote_percent_dg, vote_percent_rd)
# print(poll[winner])

# -------------------------------------------- PRINT SUMMARY ------------------------------------------------
print("Election Result")
print("-------------------------")
print(f"Total Votes:{len(total_votes)}")
print("-------------------------")
print(f"Charles Casper Stockham: {vote_percent_cs}% ({len(votes_cs)})")
print(f"Diana DeGette: {vote_percent_dg}% ({len(votes_dg)})")
print(f"Raymon Anthony Doane: {vote_percent_rd}% ({len(votes_rd)})")
print("-------------------------")
print(f"Winner: {poll[winner]}")
print("-------------------------")

# ----------------------------------------- OUTPUT SUMMARY -------------------------------------------------
# identify output file location
output_file = os.path.join("/Users/calebsteeves/Desktop/python-challenge/PyPoll/analysis/poll.txt")

# open output file and write to it.
with open(output_file, "w") as final_output:
    final_output.write("Election Result\n")
    final_output.write("-------------------------\n")
    final_output.write(f"Total Votes:{len(total_votes)}\n")
    final_output.write("-------------------------\n")
    final_output.write(f"Charles Casper Stockham: {vote_percent_cs}% ({len(votes_cs)})\n")
    final_output.write(f"Diana DeGette: {vote_percent_dg}% ({len(votes_dg)})\n")
    final_output.write(f"Raymon Anthony Doane: {vote_percent_rd}% ({len(votes_rd)})\n")
    final_output.write("-------------------------\n")
    final_output.write(f"Winner: {poll[winner]}\n")
    final_output.write("-------------------------\n")