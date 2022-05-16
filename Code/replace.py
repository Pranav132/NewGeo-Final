import csv

# Was used as a python file for formatting
# and performing random neccessary operations

# new file for output
f = open('check2.csv', 'a')

with open('check.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # skipping header
    for row in csv_reader:
        loc = row[5][14:]
        f.write('\n')
        line_count += 1
    print(f'Processed {line_count} lines.')
