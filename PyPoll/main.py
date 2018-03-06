"""
In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration 
isn't what it used to be.)

You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed 
of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes 
and calculates each of the following:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.
"""

import os
import csv

csv_files = [os.path.join('raw_data', 'election_data_1.csv'), os.path.join('raw_data', 'election_data_2.csv')]
for file in csv_files:
    print(file)
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')
        headers = next(csvreader, None)
        candidate_votes = {}
        rows = 0
        for row in csvreader:
            rows += 1
            candidate_name = row[2]
            # Increment the vote counts for this candidate, or add them to the dict with 1 vote
            candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1

    total_votes = sum(candidate_votes.values())
    results_list = []
    results = ""
    header = f"\nElection Results\n-------------------------\nTotal Votes: ({total_votes}) \n-------------------------\n"

    # Calculate results
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        results_list.append(f"{candidate}: {(100 * (votes/total_votes)):.2f}% ({votes})")
    results = "\n".join(results_list)
    
    # Find candidate with highest # of votes
    winner_list = [candidate for candidate in candidate_votes if candidate_votes[candidate] == max(candidate_votes.values())]
    winner = " and ".join(winner_list)
    footer = f"\n-------------------------\nWinner: {winner}\n-------------------------"
    final_text = header + results + footer
    print(final_text)

    # Write results into text file
    with open(file[:-4] + '_results.txt', 'w') as txtfile:
        txtfile.write(final_text)

