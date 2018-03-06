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
import glob
import csv

def list_csv():
    """ Create a list of CSV files in the current directory"""
    for file in (glob.glob('*.csv')): 
        with open(file, 'r') as f:
            content = csv.reader(f, delimiter=',')
            # Skip the header row
            next(content)
            content_list = list(content)

            total_months = len(content_list)
            total_revenue = 0
            
            greatest_revenue_decrease = 0
            greatest_revenue_decrease_month = ""

            greatest_revenue_increase = 0
            greatest_revenue_increase_month = ""

            for item in content_list:
                month = item[0]
                revenue = int(item[1])
                total_revenue += revenue

                if revenue < greatest_revenue_decrease:
                    greatest_revenue_decrease = revenue
                    greatest_revenue_decrease_month = month
                
                elif revenue > greatest_revenue_increase:
                        greatest_revenue_increase = revenue
                        greatest_revenue_increase_month = month

            final_output = "Source Data File: " + file +"\n\n" \
                        + "Financial Analysis\n----------------------------\n" \
                        + "Total Months: """ +  str(total_months) + "\n" \
                        + "Average Revenue Change: " + str(int(total_revenue / total_months)) + "\n" \
                        + "Greatest Increase in Revenue: " + greatest_revenue_increase_month + " (" + str(greatest_revenue_increase) + ")" + "\n"\
                        + "Greatest Decrease in Revenue: " + greatest_revenue_decrease_month + " (" + str(greatest_revenue_decrease) + ")\n\n"


            print(final_output)
            with open(file[:-4]+".txt", 'w+') as f:
                f.write(final_output)

if __name__ == "__main__":
    list_csv()

