import csv

"""Script to Automate expense reports by assigning general ledger codes and descriptions 
as well as different codes depending on amounts based off merchants
"""

with open(r'C:\Users\thech\Downloads\expensereport.csv', mode = 'r') as csvFile:
    csvReader = csv.reader(csvFile)

    with open(r'C:\Users\thech\Downloads\expensereport2.csv', mode = 'w', newline = '') as csvFile2:
        csvWriter = csv.writer(csvFile2, delimiter = ',', quotechar = '"')
       
        for line in csvReader:
            line[1] = line[1].replace('-', '')
            csvWriter.writerow(line)