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
    output = "Election Results\n-------------------------\nTotal Votes: " \
            + str(total_votes) + "\n-------------------------\n"
    # print(output)
    str_list = []
    for key in candidate_votes:
        votes = candidate_votes[key]
        output += key + ": " + str(int(votes/total_votes)) + " (" + str(votes) + ")\n"
    print(candidate_votes)
    print(total_votes)
    output.join("-------------------------")
    print(output)


