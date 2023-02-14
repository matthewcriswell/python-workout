'''
Each key will be a child’s name, and each value will be a list of strings representing their children (i.e., the family’s grandchildren). Thus the dict {'A':['B', 'C', 'D'], 'E':['F', 'G']} means that A and E are siblings; A’s children are B, C, and D; and E’s children are F and G
'''
from operator import itemgetter

FAMILY_TREE = {'A': ['B', 'C', 'D'], 'E': ['F', 'G']}
NAMES = {
    'A': {
        'name': 'Meryl',
        'age': 81
    },
    'B': {
        'name': 'Brita',
        'age': 25
    },
    'C': {
        'name': 'Cristina',
        'age': 30
    },
    'E': {
        'name': 'Irene',
        'age': 91
    },
    'D': {
        'name': 'Daniela',
        'age': 32
    },
    'F': {
        'name': 'Francine',
        'age': 42
    },
    'G': {
        'name': 'Georgia',
        'age': 21
    }
}

grandkids = [
    NAMES[child]
    for item in [FAMILY_TREE[item] for item in FAMILY_TREE.keys()]
    for child in item
]
grandkids_by_age = sorted(grandkids, key=itemgetter('age'))
print(*grandkids_by_age)
