''' Animal cages '''


class Animal:
    ''' base class for animals in a zoo '''

    def __init__(self, color, num_legs, space_required):
        self._species = self.__class__.__name__
        self._color = color
        self._num_legs = num_legs
        self._space_required = space_required

    @property
    def space_required(self):
        ''' the amount of space an animal requires '''
        return self._space_required

    @space_required.setter
    def space_required(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._space_required = value

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
        super().__init__(color, 4, 25)

    def compat(self):
        return f'wolf'


class Wolf(Animal):
    ''' wolf subclass '''

    def __init__(self, color):
        super().__init__(color, 4, 40)

    def compat(self):
        return f'sheep'


class Snake(Animal):
    ''' snake subclass '''

    def __init__(self, color):
        super().__init__(color, 0, 3)

    def compat(self):
        return f'parrot'


class Parrot(Animal):
    ''' parrot subclass '''

    def __init__(self, color):
        super().__init__(color, 2, 2)

    def compat(self):
        return f'snake'


class Cage():
    ''' a container for Animal types '''

    cls_cage_ids = set()
    cls_max_animals = 5
    cls_max_size = 100
    cls_compat_matrix = {
        Wolf: [Wolf, Sheep],
        Sheep: [Wolf, Sheep],
        Snake: [Snake, Parrot],
        Parrot: [Snake, Parrot]
    }

    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.cage = []
        self._cage_used_volume = 0

    @property
    def cage_used_volume(self):
        ''' amount of space used '''
        return self._cage_used_volume

    @cage_used_volume.setter
    def cage_used_volume(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected Int')
        self._cage_used_volume = value

    @property
    def cage_id(self):
        ''' set cage identifier '''
        return self._cage_id

    @cage_id.setter
    def cage_id(self, value):
        if value in self.cls_cage_ids:
            raise ValueError("Identifier collision")
        self.cls_cage_ids.add(value)
        self._cage_id = value

    def add_animals(self, *args):
        ''' add number of animals to the cage '''
        for entry in args:
            if len(self.cage) >= self.cls_max_animals:
                raise ValueError("Too many animals")
            if self.cage_used_volume >= self.cls_max_size:
                raise ValueError("Not enough space")
            if len(self.cage) > 0:
                for item in self.cage:
                    if type(item) not in self.cls_compat_matrix[type(entry)]:
                        print(f'{item} not compatiple with {entry}')
            if isinstance(entry, Animal):
                self.cage.append(entry)
                self.cage_used_volume += entry.space_required
            else:
                print(f"{entry} is not an Animal")

    def __repr__(self):
        output = f'{self.__class__.__name__} {self.cage_id}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.cage)
        return output


class BigCage(Cage):
    ''' a bigger cage for Animals '''

    cls_max_animals = 10
    cls_max_size = 200


wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(parrot)
c2.add_animals(parrot)
c2.add_animals(snake)
print(c2)

print(c1)