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

