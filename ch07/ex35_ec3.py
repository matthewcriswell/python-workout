'''
It’s sometimes useful to transform data from one format into another. Download a JSON-formatted list of the 1,000 largest cities in the United States from http://mng.bz/Vgd0. Using a dict comprehension, turn it into a dict in which the keys are the city names, and the values are the populations of those cities. Why are there only 925 key-value pairs in this dict? Now create a new dict, but set each key to be a tuple containing the state and city. Does that ensure there will be 1,000 key-value pairs?
'''

import json
with open('cities.json', 'rt') as in_f:
    cities = json.load(in_f)
city_pop = {city['city']:city['population'] for city in cities}
city_state_pop = {(city['state'],city['city']):city['population'] for city in cities}
