''' A zoo '''


class Animal:
    ''' base class for animals in a zoo '''

    def __init__(self, species, color, num_legs):
        self._species = species
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
        return f'{self.color.capitalize()} {self.species}, {self.num_legs} legs'


class Sheep(Animal):
    ''' sheep subclass '''

    def __init__(self, color):
        super().__init__("sheep", color, 4)
        self._color = color


class Wolf(Animal):
    ''' wolf subclass '''

    def __init__(self, color):
        super().__init__("wolf", color, 4)
        self._color = color


class Snake(Animal):
    ''' snake subclass '''

    def __init__(self, color):
        super().__init__("snake", color, 0)
        self._color = color


class Parrot(Animal):
    ''' parrot subclass '''

    def __init__(self, color):
        super().__init__("parrot", color, 2)
        self._color = color
