import csv

with open('names.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
