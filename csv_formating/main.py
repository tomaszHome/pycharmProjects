import csv
from collections import Counter

parts = {}
numberList = {}

with open('csv_test_invertory.csv', mode='rU') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for n, row in enumerate(reader):
        if not n:
            # Skip header row (n = 0).
            continue
        part = row[2]
        number = row[3]
        if part not in parts:
            parts[part] = list()
        parts[part].append(number)

    print(parts)

    for key, value in parts.items():
        # print value
        print(key, len([item for item in value if item]))








