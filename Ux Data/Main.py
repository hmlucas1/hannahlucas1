import csv
from ntpath import join
with open ('Data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
                print(row) 


