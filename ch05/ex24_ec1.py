'''
conversion function
'''
import csv


def conversion_function(input_file, output_file):
    ''' 'encodes' input file and writes to output file '''
    with open(input_file, 'rt',
              encoding='UTF-8') as reader, open(output_file,
                                                'wt',
                                                encoding='UTF-8') as writer:
        outcsv = csv.writer(writer, delimiter=' ')
        for line in reader:
            outcsv.writerow([ord(char) for char in line])


def deconvert_function(input_file, output_file):
    ''' 'decodes' input file '''
    with open(input_file, 'rt',
              encoding='UTF-8') as reader, open(output_file,
                                                'wt',
                                                encoding='UTF-8') as writer:
        incsv = csv.reader(reader, delimiter=' ')
        for line in incsv:
            writer.write(''.join([chr(int(char)) for char in line]))
