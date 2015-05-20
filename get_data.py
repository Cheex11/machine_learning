import csv

start_times = []
end_times = []

with open('logtime.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        start_times.append(row[0])
        end_times.append(row[1])
print end_times
