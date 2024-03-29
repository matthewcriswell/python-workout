''' A zoo '''


class Animal:
    ''' base class for animals in a zoo '''

    def __init__(self, color):
        self._species = self.__class__.__name__
        self._color = color

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


class ZeroLeggedAnimal(Animal):
    ''' animals with no legs '''

    def __init__(self, color):
        super().__init__(color)
        self.num_legs = 0


class TwoLeggedAnimal(Animal):
    ''' animals with two legs '''

    def __init__(self, color):
        super().__init__(color)
        self.color = color
        self.num_legs = 2


class FourLeggedAnimal(Animal):
    ''' animals with four legs '''

    def __init__(self, color):
        super().__init__(color)
        self.num_legs = 4


class Snake(ZeroLeggedAnimal):
    ''' snake subclass '''

    def __init__(self, color):
        super().__init__(color)


class Sheep(FourLeggedAnimal):
    ''' sheep subclass '''

    def __init__(self, color):
        super().__init__(color)


class Wolf(FourLeggedAnimal):
    ''' wolf subclass '''

    def __init__(self, color):
        super().__init__(color)


class Parrot(TwoLeggedAnimal):
    ''' parrot subclass '''

    def __init__(self, color):
        super().__init__(color)


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
