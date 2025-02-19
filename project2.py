### CSE 8A Project 2
### Author: Dani Nguyen
### Collaborations:

import csv
data = list(csv.reader(open("Ed Sheeran Dataset.csv")))

def average_col(col): #6, 8, 9, 11.
    total = 0
    for row in data[1:]:
        total += int(row[col])
    return total / len(data[1:])
