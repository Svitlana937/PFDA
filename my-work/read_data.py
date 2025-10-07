# Program to read data from a CSV file 
# Author: Svetlana Kozlovska
import csv
import os
print(f"Current working directory: {os.getcwd()}")

FILENAME = 'data.csv'
DATADIR = 'lab/'


# Link to documentation:
# https://docs.python.org/3/library/csv.html#csv.csvreader.__next__

header = csv.reader(open(DATADIR + FILENAME)).__next__()

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0   
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all subsequent rows
            total += int(line[1]) # 1 is becuase second column where we have numbers
        linecount += 1
    print(f"average is: {total/(linecount-1)}") # -1 because we do not count header row

