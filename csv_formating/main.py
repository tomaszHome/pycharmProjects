import csv

# Stores organised parts
parts = {}

with open('csv_test_invertory.csv', mode='rU') as csvFile:
    # Reads csv file, delimiter set to ','
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
        counter = key, len([item for item in value if item])
        print(counter)

    report = 'report.csv'
    csv = open(report, "w")
    columnTitleRow = "part name, part number\n"

    csv.write(columnTitleRow)

    for part in parts:
        #print(parts.keys())
        partname = part
        print(partname)
        partnumber = parts[part]
        for items in partnumber:
            print(items)
            row = str(partname) + "," + str(items) + "\n"
            csv.write(row)









