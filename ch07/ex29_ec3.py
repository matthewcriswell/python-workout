'''
Define a list of five dicts. Each dict will have two key-value pairs, name and age, containing a person’s name and age (in years). Use a list comprehension to produce a list of dicts in which each dict contains three key-value pairs: the original name, the original age, and a third age_in_months key, containing the person’s age in months. However, the output should exclude any of the input dicts representing people over 40 years of age.
'''

NAMES = ['matt', 'jim', 'sara', 'bort', 'larry']
AGE = [39, 80, 31, 845, 65]
PEOPLE = [{
    'name': name,
    'age': age,
    'age_in_months': age * 12
} for name, age in zip(NAMES, AGE)]
YOUNGER_PEOPLE = [{
    'name': name,
    'age': age,
    'age_in_months': age * 12
} for name, age in zip(NAMES, AGE) if age < 40]
