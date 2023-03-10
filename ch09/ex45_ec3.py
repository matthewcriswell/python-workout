''' Animal cages '''


class Zoo:
    ''' a collection of cages and their animals '''

    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        for cage in args:
            if isinstance(cage, Cage):
                self.cages.append(cage)
            else:
                raise ValueError("Item isn't a cage")

    def animals_by_color(self, color):
        output = []
        for cage in self.cages:
            for animal in cage.cage:
                if animal.color == color:
                    output.append(f'{repr(animal)}\n')
        return ''.join(output)

    def animals_by_legs(self, legs):
        output = []
        for cage in self.cages:
            for animal in cage.cage:
                if animal.num_legs == legs:
                    output.append(f'{repr(animal)}\n')
        return ''.join(output)

    def get_animals(self, **kwargs):
        output = []
        legs_output = []
        color_output = []
        valid_keys = ['color', 'legs']
        if len(kwargs) == 1:
            for item in kwargs:
                if item not in valid_keys:
                    raise ValueError(f"{item} not 'color' or 'legs'")
                if item == 'color':
                    output.append(self.animals_by_color(kwargs[item]))
                if item == 'legs':
                    output.append(self.animals_by_legs( kwargs[item]))
            return ''.join(output)
        else:
            for item in kwargs:
                if item == 'color':
                    color_output.append(self.animals_by_color(kwargs[item]).split('\n'))
                if item == 'legs':
                    legs_output.append(self.animals_by_legs(kwargs[item]).split('\n'))
                #output.append(list(set(color_output) & set(legs_output)))
            combined = set(*color_output) & set(*legs_output)
            #output = [i for i in color_output if i in legs_output] 
            #print(combined)
            output = list(combined)
        return '\n'.join(output)

    def number_of_legs(self):
        output = 0
        for cage in self.cages:
            output += cage.special_op()
        return output

    def __repr__(self):
        output = []
        for cage in self.cages:
            output.append(f'{repr(cage)}\n')
        return ''.join(output)


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

    cls_cage_ids = set()

    def __init__(self, cage_id):
        self._cage_id = cage_id
        self.cage = []
        self.cage_ids = Cage.cls_cage_ids

    def print_vals(self):
        print(self.cage_ids)

    @property
    def cage_id(self):
        return self._cage_id

    @cage_id.setter
    def cage_id(self, value):
        if value in self.cage_ids:
            raise ValueError("Identifier collision")
        else:
            self.cage_ids.add(value)
            self._cage_id = value

    def add_animals(self, *args):
        for entry in args:
            if isinstance(entry, Animal):
                self.cage.append(entry)
            else:
                print(f"{entry} is not an Animal")

    def special_op(self):
        leg_sum = 0
        for animal in self.cage:
            leg_sum += animal.num_legs
        return leg_sum

    def __repr__(self):
        output = f'Cage {self.cage_id}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.cage)
        return output


wolf = Wolf('black')
wolf2 = Wolf('green')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot, wolf2)

print(c1)
print(c2)

z = Zoo()
z.add_cages(c1)
z.add_cages(c2)

print(z)

print(z.animals_by_color('brown'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
print(z.get_animals(color='black', legs=4))
print(z.get_animals(color='green', legs=2))
print(z.get_animals(color='green'))
