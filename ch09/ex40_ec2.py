''' define Person class with a population attribute '''


class Person():
    ''' defines a person '''
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def __del__(self):
        Person.population -= 1
