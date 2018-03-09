"""
In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a 
world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. 
The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee 
records be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. 

The required conversions are as follows:

- The Name column should be split into separate First Name and Last Name columns.
- The DOB data should be re-written into DD/MM/YYYY format.
- The SSN data should be re-written such that the first five numbers are hidden from view.
- The State data should be re-written as simple two-letter abbreviations.
"""

import os
import csv

csv_files = [os.path.join('raw_data', 'employee_data1.csv'), os.path.join('raw_data', 'employee_data2.csv')]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

for file in csv_files:
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)

        final_output = []
        for row in csvreader:
            # Original values
            EmpID = row[0]
            Name = row[1] 
            DOB = row[2] 
            SSN = row[3] 
            State = row[4] 

            # Convert values into new required format
            fName, lName = Name.split()
            y, m, d = DOB.split("-")
            # Only last 4 digits revealed
            new_SSN = "***-**-" + SSN[-4:]
            new_State = us_state_abbrev[State]
            final_output.append([EmpID, fName, lName, m + "/" + d + "/" + y, new_SSN, new_State])

    # Write values in final_output list into new CSV
    with open(file[:-4] + "_new.csv", 'w', newline = '') as newcsvfile:
        newcsvwriter = csv.writer(newcsvfile, delimiter=',')
        newcsvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

        for row in final_output:
            newcsvwriter.writerow(row)
            
