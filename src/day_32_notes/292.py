import pandas as pd
import csv

# HINT 2: Use pandas to read the birthdays.csv
pd.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

"""
birthdays_dict = {
    (month, day): data_row

}
"""

with open('birthdays.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('birthdays.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = dict(row[:2] for row in reader if row)

        print(mydict)
