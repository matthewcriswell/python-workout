'''
Use a nested list comprehension to transform a list of dicts into a list of two-element (name-value) tuples, each of which represents one of the name-value pairs in one of the dicts. If more than one dict has the same name-value pair, then the tuple should appear twice.
'''

list_of_dicts = [{
    'name': 'matt',
    'hobby': 'gardening'
}, {
    'name': 'laura',
    'hobby': 'cooking'
}, {
    'name': 'damon',
    'hobby': 'mechanical projects'
}, {
    'name': 'tom',
    'hobby': '3d printing'
}, {
    'name': 'jolene',
    'hobby': 'lounging'
}, {
    'name': 'bill',
    'hobby': 'gardening'
}]

list_of_tuples = [items for item in list_of_dicts for items in item.items()]
set_of_tuples = set(list_of_tuples)
list_of_tuples = [tuple(item) for item in set_of_tuples]
print(list_of_tuples)
