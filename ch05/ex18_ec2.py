'''
this reads a TSV seperate file and attempts to sum its values
'''

with open('test.tsv', 'rt', encoding="UTF-8") as file:
    contents = file.readlines()

print(
    sum(
        int(row[0]) * int(row[1])
        for row in [row.split() for row in contents if len(row) > 1]
        if row[0].isdigit() and row[1].isdigit()))
