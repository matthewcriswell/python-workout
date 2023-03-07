''' A zoo '''


class Animal:
    ''' base class for animals in a zoo '''
    
    sound = ''

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
        return f'{self.sound} -- {self.color.capitalize()} {self.species.lower()}, {self.num_legs} legs'


class Sheep(Animal):
    ''' sheep subclass '''

    sound = 'Baa!'
    def __init__(self, color):
        super().__init__(color, 4)


class Wolf(Animal):
    ''' wolf subclass '''

    sound = 'Awwwoo!'
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    ''' snake subclass '''

    sound = 'Hssss'
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    ''' parrot subclass '''

    sound = 'Squawk!'
    def __init__(self, color):
        super().__init__(color, 2)

if __name__ == '__main__':
    print("Tests")
    wolf = Wolf('black')
    sheep = Sheep('white')
    snake = Snake('brown')
    parrot = Parrot('green')

    print(wolf)
    print(sheep)
    print(snake)
    print(parrot)
