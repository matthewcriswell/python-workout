''' beverage class '''
class Beverage():
    ''' create a beverage with a name and temp '''
    def __init__(self, name, temp):
        assert isinstance(name,str), "Expected string for name"
        self.name = name
        assert isinstance(temp,(int,float,complex)), "Expected int for temp"
        self.temp = temp
