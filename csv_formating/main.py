import csv

# Stores organised parts
parts = {}

input_file = 'faulty27022018.csv'
output_file = 'report.csv'

if __name__ == '__main__':

    with open(input_file, mode='rU') as csvFile:
        # Reads csv file, delimiter set to ','
        reader = csv.reader(csvFile, delimiter=',')
        for n, row in enumerate(reader):
            if not n:
                # Skip header row (n = 0).
                continue
            part = row[16]
            number = row[21]
            #last_comment = row[13]
            revision = row[11]
            if part not in parts:
                parts[part] = list()
            parts[part].append(number)
            parts[part].append(revision)
            #parts[part].append(last_comment)

        for key in sorted(parts.iterkeys()):
            print "%s: %s" % (key, parts[key])

        for key, value in parts.items():
            # print value
            counter = key, len([item for item in value if item])
            print(counter)

        csv = open(output_file, "w")
        column_title_row = "part name, part number, part revision, last comment\n"

        csv.write(column_title_row)

        # print("items = " + str(parts.viewitems()))
        # print("keys = " + str(len(parts.keys())))
        # print("values = " + str(parts.values()[1]))
        # print("number of values = " + str(len(parts.values()[1])))
        for key in range(len(parts.keys())):
            # print(str(parts.keys()[key]))
            row = str(parts.keys()[key]) + ","
            csv.write(row)
            #print(str(parts.values()[key]))
            for value in range(len(parts.values()[key])):
                # print(str(parts.values()[key][value]))
                if value % 2 == 0:
                    csv.write("\n")
                row = "," + str(parts.values()[key][value])
                csv.write(row)
            csv.write("\n")
