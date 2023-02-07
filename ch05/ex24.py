'''
conversion function
'''


def conversion_function(input_file, output_file):
    ''' reverses input file and writes to output file '''
    with open(input_file, 'rt', encoding='UTF-8') as reader:
        with open(output_file, 'wt', encoding='UTF-8') as writer:
            for line in reader:
                writer.writelines(''.join(line.strip()[::-1] + '\n'))
