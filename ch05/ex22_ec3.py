'''
create a csv file with random numbers and then sum them up
'''

import csv
from random import randrange

with open('test_sample.csv', 'w', encoding='UTF-8') as outfile:
    out = csv.writer(outfile)
    for item in [[randrange(10, 101) for i in range(0, 10)]
                 for x in range(0, 10)]:
        out.writerow(item)

with open('test_sample.csv', 'r', encoding='UTF-8') as infile:
    in_f = csv.reader(infile)

    row_sums = []
    for row in in_f:
        row_sums.append(sum([int(entry) for entry in row]))

print(sum(row_sums))
