# -*- coding: utf-8 -*-
"""E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path
from pathlib import Path 

# @TODO: Check the current directory where the Python program is executing from
print(f"Current working directory: {Path.cwd()}")

# @TODO: Set the path using Pathlib
file = Path('../Resources/Customer_traffic.txt')

# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open(file, 'r') as file:
    # @TODO: Parse the file line by line
    for line in file:

        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
        number = int(line)

        # @TODO: Sum the total and count of the numbers in the text file
        customer_total += number
        day_count += 1


# @TODO: Print out customer_total and day_count
print(f"Total Customers: {customer_total}")
print(f"Total days: {day_count}")


# @TODO: Calculate the average
daily_average = customer_total / day_count
print(f"Daily Average: {daily_average}")

# @TODO: Set output file name
output_file = Path('../Resources/output.txt')

# @TODO: Open the output path as a file object
with open(output_file, 'w') as file:
    # @TODO: Write daily_average to the output file, convert to string
    file.write(f"The total count of the numbers in the text file are {customer_total} and {day_count}, respectively. The average is {daily_average:.2f}") 