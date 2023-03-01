''' compose a class with other objects '''


class Scoop():
    ''' scoop of icecream '''

    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return self.flavor


class Bowl():
    ''' bowl of scoops '''

    def __init__(self):
        self.contents = []

    def add_scoops(self, *new_scoops):
        ''' add scoop objects '''
        for scoop in new_scoops:
            self.contents.append(scoop)

    def unique_scoops(self):
        ''' print unique scoops '''
        print(set(self.contents))

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.contents)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('strawberry')
b = Bowl()
b.add_scoops(s1, s2, s1, s3, s3, s1, s2, s2)
