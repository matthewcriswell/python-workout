''' limited bowl '''

from typing import List
from dataclasses import dataclass, field


@dataclass
class Scoop():
    ''' define a scoop of icecream '''
    flavor: str


@dataclass
class Bowl():
    ''' define a bowl that only accepts 3 scoops'''

    capacity = 3
    contents: List[Scoop] = field(default_factory=list)

    def add_scoops(self, *my_scoops):
        ''' try to add scoops to the bowl '''
        for scoop in my_scoops:
            if len(self.contents) < self.capacity:
                self.contents.append(scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.contents)

@dataclass
class BigBowl(Bowl):
    ''' define a bigger bowl that accepts 5 scoops '''
    capacity = 5
    

s1 = Scoop('chocolate')
s2 = Scoop('chicken')
s3 = Scoop('beer')
s4 = Scoop('vanilla')
s5 = Scoop('rocky road')
b = Bowl()
b.add_scoops(s1, s2, s3, s4, s5)
bb = BigBowl()
bb.add_scoops(s1, s2, s3, s4, s5)

