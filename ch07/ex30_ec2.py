'''
Each key will be a child’s name, and each value will be a list of strings representing their children (i.e., the family’s grandchildren). Thus the dict {'A':['B', 'C', 'D'], 'E':['F', 'G']} means that A and E are siblings; A’s children are B, C, and D; and E’s children are F and G
'''

FAMILY_TREE = {'A': ['B', 'C', 'D'], 'E': ['F', 'G']}
NAMES = {
    'B': 'Brita',
    'C': 'Cristina',
    'D': 'Daniela',
    'F': 'Francine',
    'G': 'Georgia'
}

print([
    NAMES[child]
    for item in [FAMILY_TREE[item] for item in FAMILY_TREE.keys()]
    for child in item
])
