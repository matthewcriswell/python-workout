'''
prints some stuff 
'''
import glob
import json
import statistics

FILES = glob.glob('scores/*.json')


def print_grades_json(file):
    ''' calculate some stats from JSON formatted data and print it to the screen '''
    with open(file, 'rt', encoding='UTF-8') as in_file:
        contents = json.load(in_file)
    for i in {k for d in contents for k in d.keys()}:
        hamburger = [subject[i] for subject in contents]
        print(
            f"{i} min {min(hamburger)} max {max(hamburger)} average {statistics.mean(hamburger)}"
        )
    print("")


files = FILES
_ = [print_grades_json(stats_file) for stats_file in files]
