'''
write a dict to a csv
'''
import csv


def dict_to_csv(mydict, outfile):
    ''' writes a dict to a CSV file '''
    with open(outfile, 'w', encoding='UTF-8') as file:
        out = csv.writer(file)
        for row in [[item, mydict[item],
                     type(mydict[item])] for item in mydict.keys()]:
            out.writerow(row)
