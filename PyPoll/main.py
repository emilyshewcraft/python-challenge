#Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")