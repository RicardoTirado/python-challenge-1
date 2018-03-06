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
        for row in csvreader:
            print(row)
# def list_csv():
# if __name__ == "__main__":
#     list_csv()

