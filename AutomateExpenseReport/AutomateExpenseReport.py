import csv

"""Script to Automate expense reports by assigning general ledger codes and descriptions 
as well as different codes depending on amounts based off merchants
"""

DicOfGLs = {
    'BESTBUY': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'APPLE': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'APPLE STORE': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'MICROCENTER': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'Amazon.com': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'AMZN MKTP US*': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'B&H PHOTO': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'TARGET': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'WALMART': {0: ['760.6500.00', 'IT SUPPLIES'], 1: ['760.7110.00', 'IT COMPUTER EXPENSE']},
    'VICTA': ['760.6500.00', 'IT SUPPLIES'],
    'MSFT': ['760.7100.00', 'SOFTWARE'],
    'MICROSOFT': ['760.7100.00', 'SOFTWARE'],
    'UPLOADFILES.IO': ['760.7100.00', 'SOFTWARE'],
    'AMZN Drive': ['760.7100.00', 'SOFTWARE'],
    'DROPBOX': ['760.7100.00', 'SOFTWARE'],
    'TeamViewer': ['760.7100.00', 'SOFTWARE'],
    'SMARTSHEET': ['760.7100.00', 'SOFTWARE'],
    'SERVER SCAN': ['760.7100.00', 'SOFTWARE'],
    'J2 EFAX SERVICES': ['760.7100.00', 'SOFTWARE'],
    'GOOGLE': ['760.7100.00', 'SOFTWARE'],
    'ZOHO-MANAGEENGINE': ['760.7100.00', 'SOFTWARE'],
    '2CO.COM': ['760.7100.00', 'SOFTWARE'],
    'TRELLO.COM': ['760.7100.00', 'SOFTWARE'],
    'SYNC.COM': ['760.7100.00', 'SOFTWARE'],
    'AT&T': ['760.4530.00', 'TELEPHONE IT'],
    '8X8': ['450.4530.00', 'TELEPHONE DIST.'],
    'NEXVORTEX': ['800.4530.00', 'G&A PHONE'],
    'CENTURYLINK': ['450.5360.00', 'INTERNET CHARGES- DISTRIBUTION'],
    'ADT SECURITY': ['450.5370.00', 'SECURITY DIST'],
    'EASYPOST': ['450.4552.03','FRT OUT ECOM'],
    'DNH*GODADDY.COM': ['850.5524.03','ECOM WEB'],
    'SHOPIFY': ['850.5524.03','ECOM WEB'],
    'HOTJAR SWIEQI': ['850.5524.03','ECOM WEB'],
    'ZONOS': ['850.5524.03','ECOM WEB'],
    'WAHOO\'S FISH TACOS': ['760.4500.00','MEALS & ENTERTAINMENT'],
    'IN N OUT BURGER': ['760.4500.00','MEALS & ENTERTAINMENT'],
    'SQ *THE BURNT GROUP': ['760.4500.00','MEALS & ENTERTAINMENT'],
    'WAZEN RESTAURANT': ['760.4500.00','MEALS & ENTERTAINMENT'],
    'PANDORA*INTERNET RADIO': ['800.4570.00','DUES/SUBSCRIPTIONS'],
    }
SpecialMerchants = [
    'BESTBUY',
    'APPLE',
    'APPLE STORE',
    'MICROCENTER',
    'Amazon.com',
    'AMZN MKTP US*',
    'B&H PHOTO',
    'TARGET',
    'WALMART'
    ]

with open(r'C:\Users\thech\Downloads\expensereport.csv', mode = 'r') as csvFile:
    csvReader = csv.reader(csvFile)

    with open(r'C:\Users\thech\Downloads\expensereport2.csv', mode = 'w', newline = '') as csvFile2:
        csvWriter = csv.writer(csvFile2, delimiter = ',', quotechar = '"')
       
        for key in DicOfGLs:
            for specialKey in SpecialMerchants:
                for line in csvReader:
                    if key in line[2]:
                        if key in SpecialMerchants:
                            if float(line[1]) > 1000.00:
                                line.append(DicOfGLs[key][1][0])
                                line.append(DicOfGLs[key][1][1])
                                line[1] = line[1].replace('-', '')
                                csvWriter.writerow(line)
                            else:
                                line.append(DicOfGLs[key][0][0])
                                line.append(DicOfGLs[key][0][1])
                                line[1] = line[1].replace('-', '')
                                csvWriter.writerow(line)
                        else:
                            line.append(DicOfGLs[key][0])
                            line.append(DicOfGLs[key][1])
                            line[1] = line[1].replace('-', '')
                            csvWriter.writerow(line)