'''
run a function against an input file and write to an output file
'''


def transform_lines(my_func, infile, outfile):
    ''' map a function on an input file and write to an output file '''
    with open(infile,
              'rt', encoding='UTF-8') as in_f, open(outfile,
                                                    'wt',
                                                    encoding='UTF-8') as out_f:
        for line in in_f:
            out_f.writelines(my_func(line))
