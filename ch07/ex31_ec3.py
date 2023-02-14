'''
Assume that you have a list of dicts, in which each dict contains two name-value pairs: name and hobbies, where name is the person’s name and hobbies is a set of strings representing the person’s hobbies. What are the three most popular hobbies among the people listed in the dicts?
'''
from collections import Counter

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
}, {
    'name': 'sara',
    'hobby': 'lounging'
}, {
    'name': 'arnold',
    'hobby': 'working out'
}, {
    'name': 'woody',
    'hobby': 'chasing the ball'
}, {
    'name': 'tom',
    'hobby': 'lounging'
}]

hobbies_count = Counter()
for item in list_of_dicts:
    hobbies_count[item['hobby']] += 1

print(hobbies_count.most_common(3))
