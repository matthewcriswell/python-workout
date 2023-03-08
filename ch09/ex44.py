''' Animal cages '''


class Animal:
    ''' base class for animals in a zoo '''

    def __init__(self, color, num_legs):
        self._species = self.__class__.__name__
        self._color = color
        self._num_legs = num_legs

    @property
    def species(self):
        ''' the species of the animal '''
        return self._species

    @species.setter
    def species(self, value):
        ''' species setter, expects str '''
        if not isinstance(value, str):
            raise TypeError("Expected str")
        self._species = value

    @property
    def color(self):
        ''' the color of the animal '''
        return self._color

    @color.setter
    def color(self, value):
        ''' color setter, expects str '''
        if not isinstance(value, str):
            raise TypeError("Expected str")
        self._color = value

    @property
    def num_legs(self):
        ''' number of legs of the animal '''
        return self._num_legs

    @num_legs.setter
    def num_legs(self, value):
        ''' num_legs setter, expects int '''
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._num_legs = value

    def __repr__(self):
        return f'{self.color.capitalize()} {self.species.lower()}, {self.num_legs} legs'


class Sheep(Animal):
    ''' sheep subclass '''

    def __init__(self, color):
        super().__init__(color, 4)


class Wolf(Animal):
    ''' wolf subclass '''

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    ''' snake subclass '''

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    ''' parrot subclass '''

    def __init__(self, color):
        super().__init__(color, 2)


class Cage():
    ''' a container for Animal types '''

    cage_ids = set()

    def __init__(self, cage_id):
        self._cage_id = cage_id
        self.cage = []

    @property
    def cage_id(self):
        return self._cage_id

    @cage_id.setter
    def cage_id(self, value):
        if value in self.cage_ids:
            raise ValueError("Identifier collision")
        else:
            self._cage_id = value
            self.cage_ids.add(value)

    def add_animals(self, *args):
        for entry in args:
            if isinstance(entry, Animal):
                self.cage.append(entry)
            else:
                print(f"{entry} is not an Animal")

    def __repr__(self):
        output = f'Cage {self.cage_id}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.cage)
        return output


wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

print(c1)
print(c2)
