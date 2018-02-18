import csv

# Stores organised parts
parts = {}

input_file = 'csv_test_inventory.csv'
output_file = 'report.csv'

if __name__ == '__main__':

    with open(input_file, mode='rU') as csvFile:
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

        for key in sorted(parts.iterkeys()):
            print "%s: %s" % (key, parts[key])

        for key, value in parts.items():
            # print value
            counter = key, len([item for item in value if item])
            print(counter)

        csv = open(output_file, "w")
        column_title_row = "part name, part number\n"

        csv.write(column_title_row)

        for part in sorted(parts):
            partname = part
            partnumber = parts[part]
            for items in partnumber:
                row = str(partname) + "," + str(items) + "\n"
                csv.write(row)
