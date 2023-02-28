''' implement a Scoop class '''


class Scoop():
    ''' scoop of ice cream object '''

    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops():
    ''' create some scoops '''
    flavors = ['chocolate', 'vanilla', 'strawberry']
    return [Scoop(flavor) for flavor in flavors]
