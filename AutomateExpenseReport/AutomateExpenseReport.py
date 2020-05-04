import csv

"""Script to Automate the expense report proccess as much as possible
"""

with open('expensereport.csv') as csvFile:
    csvReader = csv.reader(csvFile)

    for i in csvReader:
        