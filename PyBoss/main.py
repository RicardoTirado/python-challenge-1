"""
In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). 
Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for 
accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

- The total number of months included in the dataset
- The total amount of revenue gained over the entire period
- The average change in revenue between months over the entire period
- The greatest increase in revenue (date and amount) over the entire period
- The greatest decrease in revenue (date and amount) over the entire period
"""

import os
import csv

csv_files = [os.path.join('raw_data', 'election_data_1.csv'), os.path.join('raw_data', 'election_data_2.csv')]
print(csv_files)
# def list_csv():
# if __name__ == "__main__":
#     list_csv()

